#!/usr/bin/env python
from random import shuffle
from random import choice

from time import sleep
import curses, os #curses is the interface for capturing key presses on the menu, os launches the files
import sys

'''
def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    return type('Enum', (), enums)


Suite = enum(hearts=1,
             diamonds=2,
             clubs=3,
             spades=4)

Number = enum(ace=1,
              two=2,
              three=3,
              four=4,
              five=5,
              six=6,
              seven=7,
              eight=8,
              nine=9,
              ten=10,
              jack=11,
              queen=12,
              king=13
              )
'''
Suite = ['hearts', 'diamonds', 'clubs', 'spades']
Number = ['ace','two','three','four','five','six','seven',
          'eight','nine','ten','jack','queen','king']

class Card:
    def __init__(self, suite=None, number=None):
        self.suite = suite
        self.number = number
        self.numVal = { 
                        "one":    1,
                        "two":    2,
                        "three":  3,
                        "four" :  4,
                        "five" :  5,
                        "six"  :  6,
                        "seven":  7,
                        "eight":  8,
                        "nine" :  9,
                        "ten"  : 10,
                        "jack" : 10,
                        "queen": 10,
                        "king" : 10
                      }

    def __str__(self):
        e = "%s of %s" % (self.number, self.suite)
        return e

class Deck:
    def __init__(self):
        self.deck = []
        self.points = 21
    def append(self, *cards):
        for c in cards:
            self.deck.append(c)

    def value(self):
        v = 0
        ace = 0
        for c in self.deck:
            if c.number is 'ace':
                ace += 1
            else:
                v += c.numVal[c.number]
            if ace is not 0:
                if v + 10*ace < self.points:
                    v += 10 * ace
                elif v + 1*ace < self.points:
                    v += 1 * ace
        return v

    def shuffle(self):
        shuffle(self.deck)

    def lastCard(self):
        return self.deck[-1]

    def draw(self):
        if len(self.deck) is 0:
            return None

        i = choice(self.deck)
        self.deck.remove(i)
        return i

    def __str__(self):
        e = ''
        for i in self.deck:
            e += ("%s of %s\n" % (i.number, i.suite))
        e = e[:-1]
        return e

class DealerDeck(Deck):
    def __init__(self):
        Deck.__init__(self)
        for i in Suite:
            for j in Number:
                self.deck.append(Card(i,j))

class User:
    def __init__(self):
        self.name = ""
        self.deck = Deck()
        self.hand = Deck()

    def draw(self, deck):
        self.hand.append(deck.draw())
        self.hand.append(deck.draw())

    def hitme(self, deck):
        self.hand.append(deck.draw())
        return self.hand.lastCard()

class Dealer(User):
    def __init__(self):
        User.__init__(self)
        self.deck = DealerDeck()
        self.deck.shuffle()
        pass

class Human(User):
    def __init__(self):
        User.__init__(self)
        self.purse = 100
        pass

class Poker:
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.human = Human()
        self.players = []

    def dealRound(self):
        self.dealer.draw(self.dealer.deck)
        self.human.draw(self.dealer.deck)

    def humanHitme(self):
        return self.human.hitme(self.dealer.deck)

    def didHumanWin(self):
        if self.human.hand.value() > self.deck.points:
            return False
        if self.human.hand.value() > self.dealer.hand.value():
            return True
        return False

    def playRound(self, human=""):
        if human[0] == 'h':
            c = self.humanHitme()
            print "Got a %s" % c
        elif human[0] == 'f':
            if self.didHumanWin():
                print "You won!"
            else:
                print "You lost!"
            return False

        if self.bustedHand() is False:
            return False

        return True

    def strongestHand(self, *hands):
        best = Deck()
        for h in hands:
            if h.value() > best.value():
                best = h
        return best

    def bustedHand(self):
        if self.human.hand.value() > self.deck.points:
            print "you're busted!"
            return False
        else:
            print "You're still in the game!"
            return True

def main():

    while True:
        print "quit (q) or start game (s): "

        x = sys.stdin.read(2)
        if x[0] == 's':
            p = Poker()
            p.dealRound()
            while True:
                print "Your hand is %s" % (p.human.hand.value())
                print "Hit me (h) or fold (f)"
                y = sys.stdin.read(2)

                if p.playRound(y) is False:
                    break

        elif x[0] == 'q':
            break

if __name__ == "__main__":
    main()
