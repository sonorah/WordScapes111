#Group17 Project

import random 
from graphics import * 
from ButtonClassV2 import * 

#Draws the graphic window
win = GraphWin('WordScapes 111',500,600)
win.setBackground( '#273c5c' )
win.setCoords( -100, -100, 100, 100 )


#draws letters on random spots of the window to make a backdrop
for i in 'abcdefghijklmnopqrstuvwxyz':
  a = randint (-100,100)
  b = randint (-100,100) 
  backdrop = Text (Point (a,b),i)
  backdrop.setTextColor('#ede7d8')
  backdrop.draw(win)



box = Rectangle (Point (-100,-50), Point (100, -68))
box.setFill('#ede7d8')
box.draw(win)

#Import images of pre-designed logo and crossword set-up
cross = Image( Point (0,-10), "cross.png")
cross.draw(win)
logo = Image( Point (0,70), "logo.png")
logo.draw(win)
confetti = Image (Point(-12,20), "conf.png")



#Draws the entry box for users to enter the words

entry1 = Entry(Point(-5, -80), 15)
entry1.draw(win)

#Draws the submission button for user to submit their answers after typing each word

submit1_but = Button(win, 50, -80, 15, 5, 'LightGreen', 'Try!' )
submit1_but.activate()
 
#Draws a help button 
help_but = Button(win, 70, 70, 10, 7, 'lightblue', 'Help')
help_but.activate()

#Draws a quit button 
quit_but = Button(win, 70, 50, 10, 7, 'pink', 'Quit')
quit_but.activate()

#Draws a clear button
clear_but = Button(win, 70, 90, 10, 7, 'lightyellow', 'Clear')
clear_but.activate()


#Reads the txt file of dictionary to a list
f = open("engmix.txt", 'r')
txt = f.read( )
f.close( )
wordList = txt.split()

#Adds all five-letter words from the wordList to five_list
five_list = []
third_word_opt = []

for word in wordList: 
  if len(word) == 5:
    five_list.append(word)

#Chooses three random words from five_list
word1 = random.choice(five_list)
word2 = random.choice(five_list)
word3 = random.choice(five_list)


#Condition for the horizontal word: its second and fourth letter must match with the third letters of the vertical words, correspondingly 
for word3 in five_list:
  word3 = word3 [0] + word1[2] + word3[1] + word2[2] + word3[4]
  if word3 in five_list:
    third_word_opt.append(word3)
  elif word3 not in five_list:
    pass
    
#Error checking for options of the horizontal word: there must be at least one word that satisfies the condition
if third_word_opt==[]:
  pass
else: 
  word3 = random.choice(third_word_opt)  

#Split the three words into a list of unique letters, with the same letter only appears once
letterbank = []
list1 = list(word1)
for i in list1:
  if i not in letterbank:
    letterbank.append(i)
for i in list(word2):
  if i not in letterbank:
    letterbank.append(i)
  else:
    pass
for i in list(word3):
  if i not in letterbank:
    letterbank.append(i)
  else:
    pass
  
print (word1, word2, word3)
print ("Your letters:", str(letterbank))

#Prints out the letters for user input
blurb = Text(Point(0, -55), 'Your letters are:')
blurb.setFace('courier')
blurb.setSize(10)
blurb.draw(win)
chars = Text(Point(0, -60), str(letterbank))
chars.setFace('courier')
chars.setSize(10)
chars.draw(win)


#Adds the text of each letter in the first vertical word in a list called PRINT1 
PRINT1=[]
a = -15
b = 22
for i in range (5):
  i=Text(Point(a,b-14*i),word1[i])
  i.setFace('courier')
  i.setSize(20)
  PRINT1.append(i)

  
#Adds the text of each letter in the second vertical word in a list called PRINT2 
PRINT2=[]
c= 15
d= 22
for i in range (5):
  i = Text(Point(c, d-14*i), word2[i])
  i.setFace('courier')
  i.setSize(20)
  PRINT2.append(i)
#Adds the text of other three letters of the horizontal word in a list called PRINT3 
PRINT3=[]
e=-30
f=-7
for i in range (3):
  i = Text(Point(e+i*30, f), word3[int(2*i)])
  i.setFace('courier')
  i.setSize(20)
  PRINT3.append(i)

def Print(list):
  """Print(list) is a function that draws each item from a list"""
  for i in list:
    i.draw(win)

def Unprint(list):
  """Unprint(list) is a function that undraws/clears each item in a list"""
  for i in list:
    i.undraw()
    
#After clicking the submission button, if the user input is the same as the pre-chosen word, it will be printed onto the crossword; otherwise it would be considered as a wrong answer and cleared from the entry box

score = 0
while True: 
  p = win.checkMouse()
  
  if p and submit1_but.clicked(p):
    try1 = entry1.getText()
    
    for c in try1:
      if try1 == word1:
        print ("Good job")
        Print(PRINT1)
        entry1.setText('')
        confetti.draw(win)
        score += 10
        print ('Score:',score,'/30')
        confetti.undraw()
        break
      elif try1 == word2:
        Print(PRINT2)
        entry1.setText('')
        confetti.draw(win)
        score += 10
        print ('Score:',score,'/30')
        confetti.undraw()
        break
      elif try1 ==word3:
        Print(PRINT3)
        entry1.setText('')
        confetti.draw(win)
        score += 10
        print ('Score:',score,'/30')
        confetti.undraw()
        break
      elif try1 != word1:
        entry1.setText('')
        pass
  #When the help button is clicked, it gives clueless users a hint--prints out the two vertical words and lets the users guess the horizontal one
  elif p and help_but.clicked(p):
        Print(PRINT1)
        Print(PRINT2)
        
    #break
  elif p and clear_but.clicked(p):
        Unprint(PRINT1)
        Unprint(PRINT2)
        Unprint(PRINT3)

        pass
  #When the quit button is clicked, it allows the user to quit the game by closing the graphic window
  elif p and quit_but.clicked(p):
        break
  
  
print ('Score:',score,'/30')    
win.close()