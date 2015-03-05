import random
import time

Scenarios = ['''
    --------
    |     XX
          XX
          XX
          XX
          XX
XXXXXXXXXXXX
'''
, '''
    --------
    |     XX
    O     XX
          XX
          XX
          XX
XXXXXXXXXXXX
'''
, '''
    --------
    |     XX
    O     XX
    |     XX
          XX
          XX
XXXXXXXXXXXX
'''
, '''
    --------
    |     XX
    O     XX
    |\    XX
          XX
          XX
XXXXXXXXXXXX
'''
, '''
    --------
    |     XX
    O     XX
   /|\    XX
          XX
          XX
XXXXXXXXXXXX
'''
, '''
    --------
    |     XX
    O     XX
   /|\    XX
   /      XX
          XX
XXXXXXXXXXXX
'''
, '''
    --------
    |     XX
    O     XX
   /|\    XX
   / \    XX
          XX
XXXXXXXXXXXX'''
]
words = ["one", "hi"]

def disp_hangman(strikes):
    print Scenarios[strikes]


def Hangman():
    WORD = random.choice(words)
    WORDLENGTH = len(WORD)
    INFO = []
    STRIKES = 0
    while STRIKES !=6:
        if STRIKES == 0:
            print "WELCOME TO HANGMAN!"
        if raw_input not in WORD:
            STRIKES += 1
            
    
    
    print "WELCOME TO HANGMAN!"
    disp_hangman(STRIKES)
    INFO.append("_ " * WORDLENGTH)
    print "Word: " ,INFO
    
Hangman()