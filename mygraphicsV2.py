# JORourke
# mygraphicsV2.py: Various graphics functions to
# augment Zelle's graphics.py

from graphics import *
from random import randint
# For tracing function calls:
trace = True

def RandColor():
  """Returns a random color string"""
  r = randint(0,255)
  g = randint(0,255)
  b = randint(0,255)
  color = color_rgb( r, g, b )
  return color

def MyRectangle( xcent, ycent, w2, h2 ):
    """Rectangle centered on (xcent,ycent), with 'radii' half-width w2 and half-height h2.
    Returns rectangle object."""
    # Construct p1 & p2
    # Construct p1 & p2, LL, UR
    p1 = Point( xcent-w2, ycent-h2 )
    p2 = Point( xcent+w2, ycent+h2 )
    rect = Rectangle( p1, p2 )
    return rect

def MyOval( xcent, ycent, w2, h2 ):
    """Oval centered on (xcent,ycent), with 'radii'
    half-width w2 and half-height h2.
    Returns oval object."""
    # Construct p1 & p2, LL, UR
    p1 = Point( xcent-w2, ycent-h2 )
    p2 = Point( xcent+w2, ycent+h2 )
    oval = Oval( p1, p2 )
    return oval

def IsInRect( p, rect ):
    """Is point p inside the rectangle?
       Both p and rect are graphics objects.
    """
    # Extract the pt coords:
    x,y = p.getX(),p.getY()

    # Extract the rect corners:
    p1 = rect.getP1()
    x1,y1 = p1.getX(),p1.getY()
    p2 = rect.getP2()
    x2,y2 = p2.getX(),p2.getY()

    # Inside the rect when between both x&y.
    # Make no assumption about p1 & p2, so need to 
    # check several between possibilities.
    if ((x1 <= x <= x2) or (x1 >= x >= x2)) and ((y1 <= y <= y2) or (y1 >= y >= y2)):
        if trace:
        #print('IsInRect')
          return True
    else:
        return False

def IsInCirc( p, circ ):
    """Is point p inside the circle?
       Both p and circ are graphics objects.
    """
    # Extract the pt coords:
    x,y = p.getX(),p.getY()

    # Extract the circ data:
    r = circ.getRadius()
    pcent = circ.getCenter()
    xc,yc = pcent.getX(),pcent.getY()
    
    # Pythagorean Theorem:
    if (xc-x)**2 + (yc-y)**2 <= r*r:
        if trace:
            print('IsInCirc')
        return True
    else:
        return False

def MoveObjTo( obj, xnew, ynew):
  """obj: line,rectangle,circle,oval"""
  pcent = obj.getCenter()
  xc,yc = pcent.getX(),pcent.getY()

  dx,dy = xnew-xc,ynew-yc
  obj.move(dx,dy)
  # No return: obj has been moved

def BallHitWin(circ, winwidth, sx, sy):
  """Reflects sx,sy if outside of +/-winwidth.
      Angle of incidence = angle of reflection.
      Accomplished by negating speeds.
  """
  pcent = circ.getCenter()
  xc,yc = pcent.getX(),pcent.getY()
  xnew, ynew = xc,yc

  # If outside, reset to boundary,
  # as well as reflect speed.
  w = winwidth # Just for conciseness
  if xc > w:
      xnew = w
      sx = -sx
  elif xc < -w:
      xnew = -w
      sx = -sx

  if yc > w:
      ynew = w
      sy = -sy
  elif yc < -w:
      ynew = -w
      sy = -sy

  # If reflection, then move:
  if (xnew != xc) or (ynew != yc):
      MoveObjTo( circ,xnew,ynew )

  # Need to return new speeds:
  return sx,sy


def BallHitRect(circ, rect, sx, sy):
  """Reflects sx,sy if hits.
      Angle of incidence = angle of reflection.
      Accomplished by negating speeds.
      Returns hit,sx,xy. hit boolean if hit.
  """
  hit = False
  ccent = circ.getCenter()
  cx,cy = ccent.getX(),ccent.getY()
  r = circ.getRadius()

  rcent = rect.getCenter()
  x0,y0 = rcent.getX(),rcent.getY()
  p1 = rect.getP1()
  x1,y1 = p1.getX(),p1.getY()

  w2,h2 = abs(x0-x1),abs(y0-y1)

  if (x0-w2-r <= cx <= x0+w2+r) and (y0-h2-r <= cy <= y0+h2+r):
    # Ball has hit rect
    hit = True
    # Reflect from closest side of rect:
    # cy to top,bot; cx to right,left.
    if min(abs(cy-(y0+h2+r)),abs(cy-(y0-h2-r))) <= min(abs(cx-(x0+w2+r)),abs(cx-(x0-w2-r))): 
      sx,sy = sx,-sy
    else:
      sx,xy = -sx,sy
  
  return hit,sx,sy


def WrapObj(obj, w):
    """Wrap the coords if outside +/- w.
    Assumes window coords are (-w,-w,+w,+w)
    Move obj to wrapped coords.
    """
    wrap = False # True if wraps
    
    # Extract the object center coords:
    pcent = obj.getCenter()
    xc,yc = pcent.getX(),pcent.getY()

    # Initialize new coords to old (in case no wrapping):
    xnew,ynew = xc,yc

    # Note: Full width of window is 2*w.
    # Wrap x, horiz:
    if xc > w:
        xnew = xc - 2*w
        wrap = True
    elif xc < -w:
        xnew = xc + 2*w
        wrap = True

    # Wrap y, vertical
    if yc > w:
        ynew = yc - 2*w
        wrap = True
    elif yc < -w:
        ynew = yc + 2*w
        wrap = True

    # If wrapping, then move:
    if wrap:
        MoveObjTo(obj,xnew,ynew)
