

# WordNets


## General Information
WordNets is a game we made as the final project of course CSC111, inspired by the game Wordscapes.  
WordNets is a crossword-type game, in which the user use a set of given letters to form the maximal amount of English words that then fit into a crossword puzzle. 


## Files included in the project
1.main.py  
2.ButtonClassV2.py  
3.graphics.py  
4.mygraphicsV2.py  
5.engmix.txt  
6.cross.png  
7.logo.png
8.conf.png
9.README.md (this file!)


## Instruction for users (AKA how to run the code)
After hitting the 'run' button, the program will run and open a graphic window that displays the graphic design of the game, and prints out the given letter for user input above the crossword graphics. At the same time, the program will choose three five-letter words that fit the setup of the puzzle (two random five-letter words for the two vertical words, and a horizontal word whose second and fourth letter must match with the third letters of the vertical words, correspondingly).  

The user are expected to type in their guesses regarding each of the three five-letter words in the entry box, and click the green button next to the entry box labeled "Try" when finish typing. If they are correct (their inputs match with the pre-chosen words in the program), they will be printed onto the crossword, otherwise will be cleared from the entry box.  

In the case that the user are clueless, clicking the 'Help' button would be a nice choice;) After clicking the button, the two vertical words will be printed and the user will only need to guess the horizontal word in the middle of the crossword. When clicking the 'Quit' button, the user will be able to quit the game with the graphic window closed.
 

## Structure of the code

We used a class written by Professor O'Rourke called ButtonClassV2 to create buttons, graphic module to design graphics, read a txt file into a string, created loops that select letters and words according to pre-set conditions, and animation loop that draws all the text when conditions are satisfied. 

To build the game, we started with the graphic features, drew an entry box that hold the user-input for words for the puzzle, four buttons with functions of submission, help(hint), clearing text, and quitting the game, and imported a logo we designed.

Essentially, the game read an english dictionary into a list and only kept the five-letter words in our word list *five_list*. Then, after randomly choosing two five-letter words from *five_list* as the two vertical words in the crossword, we used a for-loop with chained conditionals to select all words that satisfies the condition for the horizontal word (whose second and fourth letter must match with the third letters of the vertical words, correspondingly)and added them into *third_word_opt*.   

Next, the game compared user inputs with the pre-chose words using a for-loop with chained conditionals. We used loops intensively for selection of letters and words. Once the 'Try!' button is clicked, an infinite animation while-loop will be triggered, searching the user input in the chosen words, and print them out once being matched. There is also a score-keeping system, with an addition of 10 points with every matching.  

There were also other buttons that can be triggerd by clicking. When the help button is clicked, it gives clueless users a hint--prints out the two vertical words and lets the users guess the horizontal one; when the clear button is clicked, it triggered three functions that undraws the text (set text to empty string); and when the quit button is clicked, it allows the user to quit the game by closing the graphic window.
