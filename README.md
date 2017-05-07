# My project's README
A python program to change what screen your tablet is mapped to. Usually invoked by a button on the tablet.
Linux is currently the only OS supported.
You will need to install screeninfo with pip for it to work. I currently do not have an automated install script for that. You will need to install it for python3 since that is what this code uses

```
#!bash

pip install screeninfo
```

Example of key binding:

In a startup script issue the command

```
#!bash
xsetwacom --set <id or name of device pad (of "type: PAD") here> button 2 key XF86WWW
```

Then have your system run wiss.py when you press that button