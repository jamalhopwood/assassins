# Assassin

This repo contains the code required to automate the game of assassins. It is predominantly written in python, using cgi for displaying the webpage and a small amount of shell scripting for automated emails.

## Manual Labour

The host of the game must collect the following information on participants: name, zid and room number.
This information must be stored in a csv file (easily created with microsoft excel) in the following format.

|name|zid |killcode|kills|alive|room|weapon|word|
|:--:|:--:|:------:|:---:|:---:|:--:|:----:|:--:|
|    |    |        |     |     |    |      |    |

### Killcode

The killcode will be a unique string of characters which is entered into the webpage to kill that target. eg. If Jim's killcode is "HFJ48eNs87", then when HFJ48eNs87 is entered into the webpage, Jim will be considered dead. You can google 'random string generator' to generate these strings for you.

### Kills

Set all fields in kills to 0 initially

### Alive

Set all fields in alive to 1 initially

### Weapon and Word

Come up with your own fun weapons and word kills.

## Setting up the directory

Clone or otherwise download all the files in this repo onto your cse account under the folder 'public_html' and also copy accross the csv file you made (call the csv file 'copyAssassins.csv')

Chmod the files you have copied to remove almost all permissions by typing `chmod 700 *` into your terminal (make sure only the files you downloaded and the csv file are in your cwd when you do this).

Chmod assassins.cgi so it can be read by the public by typing `chmod 755 assassins.cgi` into your terminal.

## Starting the game

To start the game and send out the initial email, type `python3 start.py` into the terminal. This will email everyone in the game their targets, killcode, weapons etc. and the game will begin.

## Checks

Try googling 'http://cgi.cse.unsw.edu.au/~z0000000/assassins.cgi' where 0000000 is your zid. If this works then everything should hopefully be all good! Otherwise you're going to have to trouble shoot.

## Trouble Shooting

Make sure all your chmods are correct to allow permission for only assassins.cgi.
Make sure your csv file is configured correctly and called 'copyAssassins.csv'.
After you ran `python3 start.py`, a new file called 'assassins0.csv' should have appeared in the directly, make sure that is present (if not then there is something going wrong in start.py)
`cat version` and make sure a '0' with no new line is the only character inside.

Hopefully some of those suggestions can kick start your brain into figuring out what is wrong.