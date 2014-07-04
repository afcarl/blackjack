#!/usr/bin/env python
from random import shuffle

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

class Deck:
    def __init__(self):
        self.deck = []
        for i in Suite:
            for j in Number:
                self.deck.append(Card(i,j))

    def shuffle(self):
        shuffle(self.deck)

    def __str__(self):
        e = ''
        for i in self.deck:
            e += ("%s of %s\n" % (i.number, i.suite))
        e = e[:-1]
        return e

def main():
    d = Deck()
    d.shuffle()

if __name__ == "__main__":
    main()
