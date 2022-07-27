import turtle
import random

def tree(t, trunkLength):
    if trunkLength < 5:     #check for base case
        return
    else:
        rNum1 = random.randrange(15, 46)
        rShrink = random.randrange(5, 26)
        t.forward(trunkLength)
        t.right(30)
        tree(t, trunkLength - rShrink)
        t.left(60)
        tree(t, trunkLength - rShrink)
        t.right(30)
        t.backward(trunkLength)

t = turtle.Turtle()
t.left(90)
trunkLength = 50
tree(t, trunkLength)
