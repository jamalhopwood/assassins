#!/usr/bin/python3

print("Content-Type: text/html")
print("")

import cgi
import cgitb
import os

cgitb.enable()

# Retrieve killcode from form
form = cgi.FieldStorage()
killcode = form.getvalue('killcode')

print("</div>")

print("</body></html>")

import csv

# Did we make a change to the csv file?
changingFile = False

# Open a different csv file depending on how many people are alive
# Each time someone dies, the new csv is saved in a new file
# This way if everything gets fucked we can open the csv files
# and everything should be okay
versionFile = open('version', 'r')

# Get the version number, a string which starts at 0 and is iterated by 1
for version in versionFile:
    continue

# Open latest version of csv
inputFile = open('assassins' + version + '.csv')
r = csv.reader(inputFile)

# Read csv into 2D array
lines = list(r)

inputFile.close()

# Loop through csv file to figure out
# How many people are left alive
numberAlive = 0
for line in lines:
    if line[4] == '1':
        numberAlive += 1

# Print out HTML for website
print(f'''<!DOCTYPE html>
    <html lang="en" class="gr__getbootstrap_com">
        <head>
        
            <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        
            <title>Kill Confirm</title>

            <link rel="canonical" href="https://getbootstrap.com/docs/4.3/examples/sign-in/">
            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
            <link rel="stylesheet" href="signin.css">
            
        </head>
        
        <body class="text-center" data-gr-c-s-loaded="true" background="https://i.imgur.com/xhiRfL6.jpg">
        
            <img class="mb-4" src="https://i.imgur.com/6b6psnA.png" alt="" width="72" height="72">

            <h6 class="text-white">{numberAlive} of 53 remain</h6>
            <h2 class="text-white">ENTER KILLCODE</p>
            <p id="profile-name" class="profile-name-card"></p>

            <form  class="form-signin">
                <input name="killcode" id="inputPassword" class="form-control form-group" placeholder="kill code" required autofocus>
                <button class="btn btn-lg btn-primary btn-block btn-signin" type="submit">Confirm</button>
            </form>
        </body>
    </html>
    ''')

# Search csv for target using killcode entered by assassin
# Edit the entry for that target in the 2D array
def determineAssassin(lines, index):
    # Deal with wrapping around list
    if index < 0:
        index = len(lines) - 1

    # Search backwards
    while lines[index][4] != '1':
        index -= 1
        
        # Deal with wrapping around list
        if index < 0:
            index = len(lines) - 1
    
    # Return row in csv
    return lines[index]

# Similar to determineAssassin but loops the other way
def determineNewTarget(lines, index):
    if index > len(lines) -1:
        index = 0
    
    while lines[index][4] != '1':
        index += 1
        
        if index > len(lines) -1:
            index = 0

    return lines[index]

index = 0

# Find the target being killed
for line in lines:
    target = line
    
    # If the killcode matches and the target is alive
    if line[2] == killcode and int(line[4]) != 0:
        line[4] = 0
        changingFile = True
        
        # Grab assassin and new target from csv
        assassin = determineAssassin(lines, index - 1)
        newTarget = determineNewTarget(lines, index + 1)

        # increase kill count of assassin
        assassin[3] = str(int(assassin[3]) + 1)
        
        break

    index += 1

if changingFile:
    # Open new csv file (for versioning)
    outputFile = open('assassins' + str(int(version) + 1) + '.csv', 'w')
    os.system("chmod 700 " + "assassins" + str(int(version) + 1) + ".csv")
    writer = csv.writer(outputFile)

    # Write 2D array to new file
    writer.writerows(lines)
    
    outputFile.close()

    # Update what version we are up to
    versionFile = open('version', 'w')
    versionFile.write(str(int(version) + 1))
    versionFile.close()

    # Email assassin new details
    # welldone = ['Well done agent.", "Top stuff.", ""
    message = f"Your kill has been confirmed. Well done agent.\n\nYour next target is {newTarget[0]}, who was last seen near room {newTarget[5]}.\nYour assigned weapon is {newTarget[6]} and your word kill is {newTarget[7]}\n\n"
    subject = "Assassins"
    
    # Concat the assassins email
    zid = assassin[1]
    email = zid + "@unsw.edu.au"

    # For some reason you cant run the command directly from here
    # my guess is something to do with cgi
    # So i outsources the emailing to a shell script and run that instead
    # os.system(f'echo "{message}" | mail -s "{subject"} "{email}"')
    os.system(f'./email.sh "{message}" "{subject}" "{email}"')

