#!/usr/bin/python3

import os
import csv
import time

os.system("rm assassins*.csv")
os.system("cp copyAssassins.csv assassins0.csv")
os.system("chmod 700 assassins0.csv")

# Reset version number back to 0
vf = open('version', 'w')
vf.write('0')

inputFile = open('assassins0.csv', 'r')
r = csv.reader(inputFile)

lines = list(r)

lines = lines[1:]

i = 0
while i < len(lines):
    time.sleep(1)

    zid = lines[i][1]
    email = zid + "@unsw.edu.au"
    
    subject = "Assassins"
    
    myself = lines[i][0]
    killcode = lines[i][2]

    if i == len(lines) - 1:
        name = lines[0][0]
        weapon = lines[0][6]
        room = lines[0][5]
        wordkill = lines[0][7]
    else:
        name = lines[i + 1][0]
        weapon = lines[i + 1][6]
        room = lines[i + 1][5]
        wordkill = lines[i + 1][7]

    message = f"Welcome {myself}, your private killcode is {killcode}.\n\nYou may think this is a game. You would be wrong...\n\nThis 'game' sends screams down the halls, leaves participants without the ability to leave their room and ends friendships.\n\nDo you have what it takes?\n\nYour first target is {name}, kill them with a {weapon} or with the word kill {wordkill}. They were last seen near {room}.\n\nOnce you have killed your target pry their killcode from their brains and enter it at http://cgi.cse.unsw.edu.au/~z5207765/assassins.cgi\n\nDo NOT enter your own killcode into the portal unless you give up. Do NOT share your killcode with anyone, you can't trust anyone...\n\nGood luck."

    os.system(f'./email.sh "{message}" "{subject}" "{email}"')
    
    i += 1
