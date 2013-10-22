MCP23017-Control
================

Simple Python Tool for the MCP23017 I2C IO Expander.

-------------------

Based on Nathan Chantrell's https://github.com/nathanchantrell/Python-MCP230XX

Changed wsgi menu and added "push" button emulation for Remote Control Switch.

menu.py
-------

![menu.py](https://raw.github.com/bubbl/MCP23017-Control/master/img/mcp_menu.png)

Simple command line Python curses menu to control remote switches with keyboard. To run:

<code>> python menu.py</code>

Remember to sudo chmod +x mcp23017.py before running.

Keys **1-0** trigger MCP's ports to switch remote buttons. **Q** exits menu to console.

menu.py
-------

Python Library to interface with MCP23017 Port Expander. Altered that each port returns to LOW state after being triggered to HIGH.

mcp23017.wsgi
-------------

A web interface using Python and modwsgi. Can be controlled through the built in web form or via GET requests with optional JSON like responses. 

eg. to set output GPA1 high: 
http://rpi/mcp23017.wsgi?bank=a&output=1&state=high&mode=json

Response: {"GPA1":"HIGH"}

Requires python-smbus and apache with mod-wsgi. Note that you will need to make sure your web server has permissions for the i2c bus, eg. /dev/i2c-1
