#!/usr/bin/env python3
from random import shuffle

class Card:
    name = "Generic"
    description = "none"
    value = 0
    def __init__(self, name, value=0, description="none"):
        self.name = name
        self.value = value
        self.description = description


class Deck:
    name = "Generic"
    card = []
    def __init__(self, cards=[]):
        self.card = cards
    def shuffle(self):
        shuffle(self.card)
    def build(self, card, num=1):
        for i in range(num):
            self.card.append(card)
    def deal(self, num):
        hand = []
        for i in range(num):
            hand.append(self.card.pop())
        return hand
    def show(self, num=0, value=False):
        if num==0:
           num = len(self.card)
        if value:
            for i in range(num):
                print(self.card[i].name + " " + str(self.card[i].value), end=", ")
        else:
            for i in range(num):
                print(self.card[i].name, end=", ")
        print()




