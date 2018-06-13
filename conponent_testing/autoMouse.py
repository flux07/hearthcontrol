'''
A quick text to make sure we can move your mouse around in Python.
When this script runs, it should move your mouse to the center of the screen.
'''

#pip install PyUserInput
#Also has some dependances, explained here:
#https://github.com/SavinaRoja/PyUserInput/wiki/Installation
#main repo:
#https://github.com/PyUserInput/PyUserInput
from pymouse import PyMouse

m = PyMouse()

x_dim, y_dim = m.screen_size()


m.move(x_dim/2,y_dim/2)

print "Done!"
