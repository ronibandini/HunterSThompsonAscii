# Routine to simulate typewriter in Python
# Roni Bandini @RoniBandini
# Argentina, Feb-022
# Usage: $sudo python3 typewriter.py 

import os
import sys
import time
import random
from random import randrange
from colorama import Fore, Back, Style

def typingPrint(text):

  for character in text:
    # reset color
    sys.stdout.write(Fore.WHITE)
    sys.stdout.flush()
    sys.stdout.write(character)

    myRand=randrange(25)

    if myRand==1:

        myErrorLetter=randrange(5)

        if myErrorLetter==1:
            sys.stdout.write('\b' + 'X')
        if myErrorLetter==2:
            sys.stdout.write('\b' + '.')
        if myErrorLetter==3:
            sys.stdout.write('\b' + 'P')
        if myErrorLetter==4:
            sys.stdout.write('\b' + '&')
        if myErrorLetter==5:
            sys.stdout.write('\b' + '+')

        sys.stdout.flush()
        time.sleep(random.uniform(0, 0.4))
        sys.stdout.write('\b' + character)
        sys.stdout.flush()
        time.sleep(random.uniform(0, 0.2))


    sys.stdout.flush()

    time.sleep(random.uniform(0, 0.2))

myline="We were somewhere around Barstow on the edge of the desert when the drugs began to take hold"

os.system("clear")
typingPrint(myline)
