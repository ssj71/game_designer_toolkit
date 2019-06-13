#!/usr/bin/env python3
import sys
sys.path.insert(0, '../src')

from card_util import Card
from card_util import Deck

d = Deck()

d.build(Card("Cow",1,"Cows can eat a lot of grass"),5)
d.build(Card("Horse",3,"Horses are like cows but faster"),10)

d.shuffle()
hand = Deck(d.deal(5)).show()


d.card = []

d.build(Card("1/12",1/12),11)
d.build(Card("5/12",5/12),2)
d.build(Card("7/12",7/12),1)

d.build(Card("1/9",1/9),8)
d.build(Card("2/9",2/9),4)
d.build(Card("4/9",4/9),2)
d.build(Card("5/9",5/9),1)
d.build(Card("7/9",7/9),1)

d.build(Card("1/8",1/8),7)
d.build(Card("3/8",3/8),2)
d.build(Card("5/8",5/8),1)

d.build(Card("1/6",1/6),5)
d.build(Card("1/4",1/4),3)
d.build(Card("1/3",1/3),2)
d.build(Card("1/2",1/2),1)

d.shuffle()
hand = Deck(d.deal(10)).show()

