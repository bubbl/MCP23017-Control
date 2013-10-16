MCP23017-Control
================

Simple Python Tool for the MCP23017 I2C IO Expander

-------------------

Based on Nathan Chantrell's https://github.com/nathanchantrell/Python-MCP230XX

Changed wsgi menu and added "push" button emulation for Remote Control Switch.

mcp23017.wsgi
-------------

A web interface using Python and modwsgi. Can be controlled through the built in web form or via GET requests with optional JSON like responses. 

eg. to set output GPA1 high: 
http://rpi/mcp23017.wsgi?bank=a&output=1&state=high&mode=json

Response: {"GPA1":"HIGH"}

Requires python-smbus and apache with mod-wsgi. Note that you will need to make sure your web server has permissions for the i2c bus, eg. /dev/i2c-0

To do: Extend to cater for input as well as output and report on the current state of the outputs.
