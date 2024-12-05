'''
This is a prototype model of 'JamAI'

Everything within this project is an entirely dedicated programming model surrounding the useage of Jam and his superiority

'''

from tkinter import*
from random import*

print('JamAI v1.00')
jam = ['JAM IS', 'Jam is']
jam2 = ['such a LUCIOUS INDIVIDUAL', 'is SOOOOOO beautiful ong', 'love, life, and purpose']
jam3 = ['in all of the right ways.', 'because he takes me to Greggs.', 'AND I want him to spread Tescos Jam all over me.', 'and I am currently locked inside St Marks reception as I speak.']
jampart1 = ['I would also like him to take Logan', 'He is easily better than Ally in every way possible', 'PLEASE CAN JAM TAKE ME TO SPOONS']
jampart2 = ['BECAUSE I REALLY WANT TO GET DRUNK', 'so we can get pissed at Carousell', 'speaking off I heard scene was doing a sale on cocktails']
jampart3 = ['so I can accend to obtain the long lost penguin plushie.', 'By the way, I collapsed drunk alongside the Brayford one time.', 'OH LOGIEBOYYY!!!']

def pick(words):
    num_words = len(words)
    num_picked = randint(0, num_words-1)
    word_picked = words[num_picked]
    return word_picked
while True:
    print(pick(jam), pick(jam2), pick(jam3), pick(jampart1), pick(jampart2), pick(jampart3))
    input()

