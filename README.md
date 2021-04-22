# Static_testing_PDA


Corrections for functions written below functions:


### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

#There are two things that need to be imported at the top of the file. So, 
import unittest and src the card.py class needs to be imported so it needs to look the following way:

import unittest
from src.card.py import *

```python

class CardGame: #put in brackets (unittest, Testcase):

  def check_for_ace(self, card):
    if card.value = 1:
      return True
    else
      return False
      
On line 26 it needs to be double == signs  and after else a : (colon) is required.

# dif needs to be changed to def and card needs to be changed to card1 
  dif highest_card(self, card1 card2):
  if card1.value > card2.value:
    return card
  else:
    return card2
  
#the variable total needs to be equal to something, so it cannot just stand there empty. Indentation needs to be fixed 

def cards_total(self, cards):
  total
  for card in cards:
    total += card.value
    return "You have a total of" + total
  
```
# Static_And_Dynamic_Testing
