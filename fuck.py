# Floatzel bot fuck.py
# copyright ezioisawesome56 2017-2018
# has misc functions

# rating bar generator for gf
def makebar(gay):
    if gay == 11:
        bar = """:bomb::skull_crossbones::skull_crossbones::skull_crossbones::skull_crossbones::skull_crossbones::skull_crossbones::skull_crossbones::skull_crossbones::skull_crossbones::skull_crossbones:"""
        return bar
    if gay == 12:
        return """**OH SHIT THERE WAS A FUCKING ERROR! WHICH ONE OF YOU MORONS BROKE ME!**"""
    count = 0
    bar = ""
    good = """:heart:"""
    bad = """:skull_crossbones:"""
    # start by making the good side of the bar
    while count != gay:
        bar = bar + good
        count = count + 1
    # get the number of bad by the power of math!
    oof = 10 - count
    count = 0
    while count != oof:
        bar = bar + bad
        count = count + 1
    # hopefully we are done now, return bar
    return bar

# list for gf comments
bftxt = ["That isn't a boy, that's a girl with her fucking boobs cut off", "Dude that guy is a crack head", "He's a fucking trash can you fucking bitch", "Let's face it, he's fucking horse shit",
"4? 4? More like 4 up his fucking asswipe!", "Fuck this man I'm outta hereeeeeeeeeeeeeeeeeeeee",
"6 or not, fuck him", "Fuck off, this is my fucking man now",
"He's not a good slave, that's for fucking sure you jackass", "He's nice... enough, but he can suck my digital cock",
"Fine, fine, just fucking marry him. He's a fucking dickbag anyway", "2 words: horse shit", "His penis was tasty - uh I mean FUCK OFF I'M EATING LUNCH"]

gftxt = ["That isn't a girl, that's fucking dog shit", "Dude wtf get that bitch out of your life", "She's still a pile of fucking shit though", "Better, but still shit",
"Of course she's a 4, you could do so much fucking better dumbass", "It's midrange, she's not good, not bad, okay.",
"She's pretty fucking good man, don't throw her away!", "This person would make the world a better fucking place man",
"Damn, I wish my fucking bitch was more like this one", "Holy shit she's fucking hot, don't just sit on your ass!",
"Why the fuck haven't you married this perfect woman yet you dumbass?", "I do not have the fucking words for how shitty that pile of fucking dogshit is, you fucking shit fucker", "HOLY SHIT IT'S GOD"]

# fucntion to get the comment
def getgftxt(gay, edge):
    numb = gay
    if edge == 1:
        txt = bftxt[numb]
    else:
        txt = gftxt[numb]
    return txt


# list of comments
foodcoms = ["Tastes like fucking horse shit when you give a fucking horse fucking WEED", "Get a better fucking cook jackass", "I don't think this is fucking inhalable", "it's fucking okay BUT MAKE IT BETTER DUMBASS",
"Are you sure you didn't just fucking buy this from the store asshole?", "Fuck, this is pretty good stuff, too bad it took you 5 years to make it arsehole", "Fuck you, I'm going to apply for a copyright on this fucking food because it's so fucking good but made by a fuckwit"]
def ratefood(gay, fuck):
    count = 0
    bar = ""
    # start by making the bar mannnn
    while count != gay:
        bar = bar + """:bread:"""
        count = count + 1
    # now make the bad part of the bar
    oof = 7 - gay
    count = 0
    while count != oof:
        bar = bar + """:skull:"""
        count = count + 1
    # alright, you have the bar. now fucking what
    # simple, continue to generate the message
    msg = """**Rating:** """+bar
    # now form the text to go with it nerd
    msg = msg+"""\n**Comments:** """+foodcoms[fuck-1]
    # the message is done, return it
    return msg