# Discord-Bot
This is meant as a project to further understand python as well as the discord.py API in order to create my own discord bot. Below are some instructions as well as information on the features that I have implemented so far in this project.
*This project is something I work in my free time so be warned that there might be unneccessary comments and/or lines which I have yet to remove or fix.*
## ENV_PLACEHOLDER
This file is my enviornment file in order to keep my private tokens safe. Currently there are two enviornment variables in this project which are the ``PUT_YOUR_KEY_HERE`` and the ``TARGET-PERSON``.

Below is the information of what these variables do but **before continuing** be sure to ``pip install python-dotenv``. I used this package to organize and read my enviornment variables from the .env file.

### PUT_YOUR_KEY_HERE

Fairly self explanitory, this is meant to put your discord bot key which can be found in the discord developer portal. Replace the ``PUT_YOUR_KEY_HERE`` text with your key, this should be a string so be sure to wrap it in quotes.

### TARGET-PERSON

This enviorment variable is meant for the "your" event listed below. Replace the ``TARGET-PERSON`` text with a discord id of a person you wish to trigger this event every time they type any correct form of "your". *This should be an int so do not include any quotes around this number.*

An easy way to get someone's discord id is to type \@person'sID#1234 in a server which they are found in and discord should automatically display an arrangements of characters like <@!1231232131231231> when you send the message. Just copy the number and that is how you get a person's discord id.

##Test
