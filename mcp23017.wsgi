#!/usr/bin/python

# A basic Python and modwsgi interface to the MCP23017 I2C IO Expander
# Built in web form or use GET requests, add &mode=json for JSON like responses
# By Nathan Chantrell http://nathan.chantrell.net
# GNU GPL V3
#
# Added import from time, altered html view and auto setting to low of ports.
# Bart Bania http://www.bartbania.com/

from wsgiref.simple_server import make_server
from cgi import parse_qs, escape
import smbus
import sys
import getopt
from time import sleep

bus = smbus.SMBus(1) # For revision 1 Raspberry Pi, change to bus = smbus.SMBus(1) for revision 2.

address = 0x20 # I2C address of IO Expander
bus.write_byte_data(0x20,0x00,0x00) # Set all of bank A to outputs 
bus.write_byte_data(0x20,0x01,0x00) # Set all of bank B to outputs 

# The HTML used to build the full web page option
html = """
<html>
<body backgroud="blue">
   <form method="get" action="mcp23017.wsgi" name="form">
    <br />
      <p>
         <input name="state" type="hidden" value="high">
         <b>
         <input name="output" type="radio" value="0"> LAMPKA NOCNA&nbsp;&nbsp;&nbsp;|
         <input name="output" type="radio" value="1"> YAMAHA&nbsp;&nbsp;&nbsp;|
         <input name="output" type="radio" value="2"> NUMBER 3&nbsp;&nbsp;&nbsp;|
         <input name="output" type="radio" value="3"> NUMBER 4&nbsp;&nbsp;&nbsp;|
         <input name="output" type="radio" value="4"> NUMBER 5 
         <br /><br /></b>
      </p>
      <p>
      <b>--------------------------------------</b>
      </p>
      <p>
         <input name="bank" type="radio" value="b"> <b>ON</b>
         <input name="bank" type="radio" value="a"> <b>OFF</b> <br />
      </p>
      <p>
         <input type="submit" value="ZMIEN"><br />
      </p>
      </form>
<br />
<br />
<br />
<br />
<br />
<br />
<br />
   <p>
      Bank: %s<br>
      Output: %s<br>
      State: %s<br>
      Debug: %s
      </p>
   </body>
</html>
"""

# HTML for the minimal JSON response (activated with &mode=json in the query string)
htmlshort = """{"%s%s":"%s"}"""

def application(environ, start_response):

   # Get the query string variables
   d = parse_qs(environ['QUERY_STRING'])
   bank = d.get('bank', [''])[0] 
   output = d.get('output', ['8'])[0] 
   state = d.get('state', [''])[0] 
   mode = d.get('mode', [''])[0]

   # Escape user input
   bank = escape(bank)
   output = int(escape(output))
   state = escape(state)
   mode = escape(mode)

   # Set the correct register for the banks
   if bank == "a" :
    register = 0x12
   elif bank == "b" :
    register = 0x13
   else:
    register = 0

   # Read current values from the IO Expander
   value =  bus.read_byte_data(address,register)

   # Shift the bits for the register value, checking if they are already set first
   if state == "high":
    if not (value >> output) & 1 :
     value += (1 << output)
   elif state == "low":
    if (value >> output) & 1 :
     value -= (1 << output)
   else:
     state = "none"

   # Quick sanity check
   if (0 <= output < 8) and register != 0 and state != "none":
    # Looks OK, now write to the IO expander
    bus.write_byte_data(address,register,value)
    sleep(0.25)
    bus.write_byte_data(address,register,0)
    if mode == "json" : # minimal mode
     response_body = htmlshort % (bank.upper(), output, state.upper())
    else: # otherwise show full web page
     response_body = html % (bank.upper(), output, state.upper(), value)
   elif mode == "json" :
    response_body = "SYNTAX ERROR"
   else:
    response_body = html % ("n/a", "n/a", "n/a", value)

   # Show the HTML page
   status = '200 OK'
   response_headers = [('Content-Type', 'text/html'),
                       ('Content-Length', str(len(response_body)))]
   start_response(status, response_headers)
   return [response_body]
