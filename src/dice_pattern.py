#!/usr/bin/env python3

from math import comb
from math import factorial

# HOW TO USE THIS MODULE
#
# this is for analyzing different outcomes of rolling multiple dice
# the outcomes will match a pattern such as AAB for doubles with
# three dice. the function add_patterns() will combine multiple
# patterns to calculate the odds, such as AAB+AAA which you might
# want because 3 of a kind also includes doubles.
# there are some checks to make sure you are entering good data,
# but there are still plenty of ways to shoot yourself in the foot.
# For example: AAB and ABB are actually identical patterns and if
# you add both you will calculate double the actual probability.
#
# The method used here is just an implementation of the process
# explained at this blog post:
# https://graciesdad.wordpress.com/2009/08/30/farkle-odds/
# Thanks to the author for helping this make some sense
#
# Typical use is like any other python file. Easiest way is to open
# python in the directory containing this script and
# `import dice_pattern` then run `dice_pattern.pattern_prob("AAB")
# or `dice_pattern.add_patterns(("AAB","AAA"))`

#expects a pattern like AAABBCD with no white space
def pattern_prob(pattern, die=6):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    l = len(pattern)
    sets = []
    #translate to a count of sets e.g. 3 2 1 1
    for letter in letters[:l]:
        n = pattern.count(letter)
        if n == 0:
            break
        sets.append(n)
    if sum(sets) < l:    
        print("\nWarning! the pattern %s is missing characters!"%pattern, sets)
        print("Do you have equivalent patterns?")
    if sets[::-1]!=sorted(sets):
        print("\nWarning! the pattern %s is unordered!"%pattern, sets)
        print("Do you have equivalent patterns?")
    if len(sets) > die:
        print("\nWarning! the pattern %s has more characters than possible dice outcomes (%i)!"%(pattern,die), sets)

    countr = 1
    setcounts = []

    print("pattern rearrangements:",end=" ")
    left = l
    prev = 0
    for n in sets:
        if n != prev:
            setcounts.append(sets.count(n))
        prev = n
        if n == 1:
            if left > 1:
                print("%i!"%left,end="")
                countr *= factorial(left)
            break
        print("(%i %i)"%(left,n),end="")
        countr *= comb(left,n)
        left -= n
    print(" =",countr)

    counta = 1
    print("value assignments:",end=" ")
    left = die
    for n in setcounts:
        print("(%i %i)"%(left,n),end="")
        counta *= comb(left,n)
        left -= n
    print(" =",counta)

    count = counta*countr
    print("total: %i * %i = %i"%(countr,counta,count))
    print("probability: ",count/(die**l))
    return count

def add_patterns(patterns, die=6):
    l = len(patterns[0])
    tot = 0
    for pattern in patterns:
        if len(pattern) != l:
            print("\nWarning! patterns are not equal length!")
            print("These results will be nonsensical.")
        print(pattern)
        tot += pattern_prob(pattern, die)
        print()
    print("\ngrand total: ",tot)
    print("probability: ",tot/(die**l))
