#!/usr/bin/env python
from random import shuffle
from random import choice
import random

from time import sleep
import os
import sys


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
            if c is None:
                continue
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

    def reset(self):
        self.deck = []

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
        self.purse = 100

    def bet(self, betAmt):
        if betAmt > self.purse:
            return False
        self.purse -= betAmt
        return True

    def resetHand(self):
        self.hand.reset()

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

class Poker:
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.human = Human()
        self.players = []
        self.won = 'won'
        self.lost = 'lost'
        self.busted = 'busted'
        self.playable = 'playable'
        self.pot = 0

    def resetRound(self):

        self.dealer = Dealer() #reset the dealer deck, too
        self.human.resetHand()
        self.dealRound()

    def dealRound(self):
        self.dealer.draw(self.dealer.deck)
        self.human.draw(self.dealer.deck)

    def humanHitme(self):
        return self.human.hitme(self.dealer.deck)

    def dealerHitme(self):
        return self.dealer.hitme(self.dealer.deck)

    def didDealerWin(self):
        if self.dealer.hand.value() > self.deck.points:
            return False
        if self.dealer.hand.value() > self.human.hand.value():
            return True
        return False

    def dealerHitMeDecide(self):
        if self.dealer.hand.value() < 17:
            self.dealerHitme()
            return True
        return False

    def didHumanWin(self):
        if self.human.hand.value() > self.deck.points:
            return False
        if self.human.hand.value() > self.dealer.hand.value():
            return True
        return False

    def playRound(self, human=""):
        c  = None
        flag = None
        if human[0] == 'h':
            c = self.humanHitme()

        if self.dealerHitMeDecide() is False:
            if self.didHumanWin() is True:
                self.human.purse += self.award()
                flag = self.won

        if human[0] == 's':
            if self.didHumanWin() is False:
                self.dealer.purse += self.award()
                flag = self.lost
            else:
                self.human.purse += self.award()
                flag = self.won

        if self.bustedHand(self.human.hand) is True:
            self.dealer.purse += self.award()
            flag = self.busted

        if self.bustedHand(self.dealer.hand) is True:
            self.human.purse += self.award()
            flag = self.won

        if flag is None:
            flag = self.playable
        return (c,flag)

    def strongestHand(self, *hands):
        best = Deck()
        for h in hands:
            if h.value() > best.value():
                best = h
        return best

    def award(self):
        purseWinner = self.pot
        self.pot = 0
        return purseWinner

    def bet(self, betAmt):
        if self.human.bet(betAmt) is False:
            return False
        self.pot += betAmt * 2
        self.dealer.bet(betAmt)
        return True

    def bustedHand(self, hand):
        if hand.value() > self.deck.points:
            return True
        else:
            return False

def main():

    while True:
        print "quit (q) or start game (s): "

        x = sys.stdin.read(2)
        if x[0] == 's':
            p = Poker()
            p.dealRound()
            while True:
                print "Your hand is \n%s" % (p.human.hand)
                print " ( %s ) " % (p.human.hand.value())
                print "Your purse is %s" % (p.human.purse)
                print "Hit me (h) or stand (s) or bet (b ### )"
                #y = sys.stdin.read(2)
                y = raw_input("")
                if len(y) is 0:
                    print "Type something\n"
                    continue

                if y.split()[0] is 'b':
                    if len(y) < 2:
                        print "Bet something\n"
                        continue

                    f = p.bet(int(y.split()[1]))
                    if f is False:
                        print "Can't bet that much"
                    continue

                if p.pot is 0:
                    f = p.bet(1)
                    if f is False:
                        print "Can't bet that much -- you're broke!"
                        break
                    
                c, flag = p.playRound(y.split()[0])

                if c != None:
                    print "You got a %s" % (c)
                if flag is 'won':
                    print "You won!"
                    print "Dealer had\n%s" % (p.dealer.hand)
                    p.resetRound()
                elif flag is 'lost' or flag is 'busted':
                   if flag is 'busted':
                       print "You're busted!"
                   print "Dealer had\n%s" %(p.dealer.hand)
                   print "You lost!"
                   if p.human.purse is 0:
                       print "You're broke!"
                       break

                   p.resetRound()

                print "\n----\n"

        elif x[0] == 'q':
            break

def findBestStrategy():
    l = [0 for i in range(14)]
    cmd = {'hitme': 'h', 'stand':'s'}

    best = 0
    l = [0 for i in range(1000)]
    for i in range(1000):
            p = Poker()
            p.dealRound()
            j = 0

            while True:
                h = p.human.hand.value()
                if p.pot is 0:
                    f = p.bet(1)
                    if f is False:
                        break
                if h < 17:
                    c, flag = p.playRound(cmd['hitme'])
                else:
                    c, flag = p.playRound(cmd['stand'])

                if flag == 'won' or flag == 'lost' or flag == 'busted':
                    if flag == 'won':
                        j += 1                        
                    p.resetRound()
                if p.human.purse == 0:
                    print "%s" % (j)
                    if j > best:
                        best = j
                    break
                else:
#                    print "%s, %s" % (j, p.human.purse)
                    pass
                
    pass
if __name__ == "__main__":
    #main()
    findBestStrategy()
