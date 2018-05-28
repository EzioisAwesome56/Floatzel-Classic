# floatzel bot 8ball.py
# copyright EzioisAwesome56 2017-2018
# repsonses file for the 8ball command
import random

# responses for ask again later
later = ["Im dying on the inside, try again later", "I don't like you, ask again when you have my respect", "Eating pant, please try again",
"What was that?! I CANT FUCKING HEAR YOU! Please try again", "Kill yourself and try again"]

# responses for yes
yes = ["Of course its yes you dipshit", "Its not that fucking hard to figure out that its true", "Fuck you, its yes",
"Let me answer this question with another question: is saltypepper gay? (Spoiler: yes!)", "YOUR MOM IS FUCKING GAY, also the answer is yes but thats not fucking important"]

# repsonses for no
no = ["Fuck off mr wrongface", "Kill yourself you wrong-ass person!", "The fucking answer is no", "you wouldn\'t be GAY if this was right", "Jump off a cliff moron, its WRONG!"]

def numb():
    return random.randint(0, 4)

def ballaskagain():
    number = numb()
    return later[number]

def ballyes():
    number = numb()
    return yes[number]

def ballno():
    number = numb()
    return no[number]