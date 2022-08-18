#from graphics import *
#from random import randint, uniform
from time import sleep
from mygraphicsV2 import *

class Button:
    """A button is a labeled rectangle in a window.
    It is activated or deactivated with the activate()
    and deactivate() methods. The clicked(p) method
    returns True if the button is active and p is inside it."""

    def __init__(self, win, xcent, ycent, w2, h2, color, string):
        """Creates a rectangular button.
        w2 & h2 are half of the full width & height""" 
        
        self.rect = MyRectangle(xcent, ycent, w2, h2)
        self.rect.setFill( color )
        self.rect.draw(win)
        self.color = color # To make accessible to methods

        p = Point( xcent, ycent )
        self.string = string # To make accessible to methods
        self.label = Text(p, string) # Text object
        self.label.setSize( 9 )
        self.label.draw(win)
        self.active = False 
        self.deactivate()
        # if trace:
        #   print(string, 'Button created')

    def clicked(self, p):
        """Returns True if button active and p is inside"""
        if self.active and IsInRect(p, self.rect ):
          # Hightlight:
          self.rect.setWidth(5)
          self.rect.setFill('White')
          # if trace:
          #     print( self.string, 'Button clicked' )
          sleep(0.25)
          # Reset color:
          self.rect.setWidth(3)
          self.rect.setFill(self.color)
          return True
        else:
            # Either inactive or not inside
            return False

    def activate(self):
        """Sets this button to active."""
        self.label.setFill('DarkRed')
        self.rect.setWidth(3)
        self.active = True
        # if trace:
        #     print( self.string, 'Button activated' )

    def deactivate(self):
        """Sets this button to inactive."""
        self.label.setFill('DarkGrey')
        self.rect.setWidth(1)
        self.active = False
        # if trace:
        #   print( self.string, 'Button deactivated' )