import random
from itertools import combinations, accumulate
from collections import defaultdict, Counter

import re
with open('../resources/p185_numbermind.txt') as fp:
    known = [(a, int(b)) for a, b in (re.findall(r'\d+', line) for line in fp)]

known_ = [
  ('90342', 2),
  ('70794', 0),
  ('39458', 2),
  ('34109', 1),
  ('51545', 2),
  ('12531', 1),
] # 39542

# Improved solution modified from source by Henric E.

def fixInput(inp):
    codeLength = len(inp[0][0])
    allowed = []
    for i in range(codeLength):
        allowed.append(set(range(10)))
    guesses = []
    for cw, correct in inp:
        assert len(cw) == codeLength
        if correct > 0:
            guesses.append((correct, list(map(int, cw)), -1))
        else:
            for i, d in enumerate(map(int, cw)):
                allowed[i] = allowed[i] - set([d])
    return codeLength, allowed, guesses

def f(allowed, guesses, myGuess, posLeft):
    '''
    Try to put another digit into myGuess.
    Parameters:
       allowed:    List of sets of allowed digits in each position.
                   Only valid for positions not yet set (posLeft).
       guesses:    List of the guesses as ordered by fixInput().
       myGuess:    List of digits in each positions. Positions not
                   assigned yet has a '_' character. (Looked nice in trace
                   outputs).
       posLeft:    Set of positions left to assign.
    '''
    if len(guesses) == 0:
        # All guesses are now used.
        # There could be (== there is) positions (one positino) where
        # where no guess is right. In this case there could be (there is)
        # only one digit allowed, because the all other digits has been
        # guessed and are wrong.
        for pos in posLeft:
            if len(allowed[pos]) == 1:
                myGuess[pos] = list(allowed[pos])[0]

        # Hopefully all positions are filled in.
        # We cannot do better than this.
        yield myGuess

    else:
        # Check if there is enough valid positions for all the guesses
        # to get enough correct.
        # Put the guesses together with their possible positions
        # in a new lists to make the best choice in the next step.
        tmpGuesses = []
        for corrLeft, cw, lastPos in guesses:
            tmpPosLeft = [pos for pos in posLeft if cw[pos] in allowed[pos]]
            if len(tmpPosLeft) < corrLeft:
                return
            tmpGuesses.append((len(tmpPosLeft),corrLeft,tmpPosLeft,cw,lastPos))

        # Use the guess that has the least number of possible positions.
        guessToUse = min(tmpGuesses)
        guess = guessToUse[3]
        posToUse = sorted(p for p in guessToUse[2] if p > guessToUse[4])
        for pos in posToUse:
            digit = guess[pos]

            myGuess[pos] = digit
            nxtGuesses = []
            nxtAllowed = allowed[:]
            nxtPosLeft = posLeft - set([pos])

            for corrLeft, cw, lastPos in guesses:
                if cw[pos] == digit:
                    corrLeft -= 1
                    if corrLeft == 0:   # Guess used.
                        # Digits in other positions of the guess are
                        # not correct and therefor not allowed.
                        for p in nxtPosLeft:
                            nxtAllowed[p] = nxtAllowed[p] - set([cw[p]])
                    else:
                        if cw == guess:
                            lastPos = pos
                if corrLeft > 0:        # Guess still to use.
                    nxtGuesses.append((corrLeft, cw, lastPos))

            for r in f(nxtAllowed, nxtGuesses, myGuess, nxtPosLeft):
                yield r
            myGuess[pos] = '_'

def solve(inp):
    codeLength, allowed, guesses = fixInput(inp)

    for myGuess in f(allowed,
                     guesses,
                     ['_'] * codeLength,     # myGuess
                     set(range(codeLength))): # posLeft
        return ''.join(map(str, myGuess))

ans = solve(known)
print(ans)
