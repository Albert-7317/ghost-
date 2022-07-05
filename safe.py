#### fake virus ####
import sys, os, time, random
#creates loading bars

def loadingCheck(check, complete):
    len = random.randint(15, 60)
    for i in range(0, len):
        x = '#' * i
        z = '-' * (len - i)
        y = check + ': [' + x + z + ']'
        print(y, end='\r')
        time.sleep(random.random())
    print(y)
    print(complete[:-1])

def getWord(fileChoice, fileSize):
    count = 0
    stop = random.randint(0, fileSize)
    with open(fileChoice, 'r') as f:
        for line in f:
            if count == stop:
                return line
            count += 1

def troll():
    with open('trollface.txt', 'r') as f:
        for line in f:
            print(line[:-1])

def createList():
    sentaceLen = random.randint(1, 3)
    sentance = ''
    for i in range(0, sentaceLen):
        sentance += getWord('wordlist.txt', 73)[:-1] + ' '
    return sentance

check = ['Installing', 'Uninstalling', 'Removing', 'Taking a break', 'Deleting', 'Breaking', 'Moving', 'Copying', 'Pasting']

while True:
    print('Your installation and configuration will begin shorty, please do not close the terminal while it is configuring, doing so may cause irreversable damage to your computer.')
    time.sleep(random.randint(0, 2))
    for i in range(0, 1000):
        
        print(createList())

        randomTroll = random.randint(0, 3)
        if randomTroll == 0:
            troll()

        randomProgress = random.randint(0, 1)
        if randomProgress == 0:
            for i in range(0, random.randint(0, 3)):
                print(getWord('singleline.txt', 11)[:-1])
                complete = getWord('complete.txt', 2)
                time.sleep(0.5)
                loadingCheck(check[random.randint(0, len(check)-1)], complete)
    

    
    break
