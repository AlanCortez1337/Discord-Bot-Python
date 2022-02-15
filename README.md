# Discord-Bot
This is meant as a project to further understand python as well as the discord.py API in order to create my own discord bot. Below are some instructions as well as information on the features that I have implemented so far in this project.
*This project is something I work in my free time so be warned that there might be unneccessary comments and/or lines which I have yet to remove or fix.*
## ENV_REPLACE
This file is my environment file in order to keep my private tokens safe. Currently there are two environment variables in this project which are the ``PUT_YOUR_KEY_HERE`` and the ``TARGET-PERSON``.

Below is the information of what these variables do but **before continuing** be sure to ``pip install python-dotenv``. I used this package to organize and read my environment variables from the .env file.

### PUT_YOUR_KEY_HERE

Fairly self explanatory, this is meant to put your discord bot key which can be found in the discord developer portal. Replace the ``PUT_YOUR_KEY_HERE`` text with your key, this should be a string so be sure to wrap it in quotes.

### TARGET-PERSON

This enviroment variable is meant for the "your" event listed below. Replace the ``TARGET-PERSON`` text with a discord id of a person you wish to trigger this event every time they type any correct form of "your". *This should be an int so do not include any quotes around this number.*

An easy way to get someone's discord id is to type \@person'sID#1234 in a server which they are found in and discord should automatically display an arrangements of characters like <@!1231232131231231> when you send the message. Just copy the number and that is how you get a person's discord id.
## MAIN.PY

This is where all the gross and "not-so-fun" parts are stored. We have our traditional *on_ready* alert, unique command prefix, unload, load, reload functions. Fairly self explanatory but if you are new the load functions are meant to update specific cog files in real time when we call them without needing to restart the entire bot.

**PLANS FOR FUTURE RELEASES::**
- react with a 👍 when we call any of the load commands
- require permission to call any of the load commands
- include more catches for errors
- possibly change the long annoying command prefix
- possibly change the status

## Cogs

So if you are familiar with discord.py API, cogs is an organizational tool to store commands or events in their own file for ease of use. Below are the current three cogs I have made for this project.

### **EVENTS.PY**

The purpose of ``EVENTS.PY`` is to have a category to store all the event listeners. So not necessarily commands which the user has to call in order for something uncharacteristically goofy to occur. Inside of this file there are currently two working commands, *ANNOYING "YOUR" EVENT* and *RANDOM EMOJI REACTION EVENT*.

#### *ANNOYING "YOUR" EVENT*

The motivation behind this "middle-finger" of an event is that I wanted to annoy a specific friend on discord and always send a rather comical gif each type a message of his included any form of "your". To do this I created a regex pattern to detect if any message has an *acceptable* form of the word "your" inside of it. If it does then it would then check if the ``TARGET-PERSON`` sent it, and if so they automatically send the gif.

However, during this development I wanted everyone else on the server to be annoyed at me. So I decided to include an opportunity for everyone else that is not the ``TARGET-PERSON`` to experience this event. My solution was to implement a random 1/20 chance of the gif sending each time a person sent any form of "your" using the *random library*.

#### *RANDOM EMOJI REACTION EVENT*

Well for this one there really is not an elaborate reason for making this feature, I just wanted to have my bot react to a message using an emoji. To do this I used the *random library* to create a 1/20 chance of reacting to any message with the 😳 and another 1/20 chance to react with 😨.

**PLANS FOR FUTURE RELEASES::**
- react to certain sent messages with a specific emoji
- custom server emoji integration

### **RANDOM.PY**

``random.py`` is meant to store all the commands that rely on python's *random library*. Initially this included *RANDOM EMOJI REACTION EVENT* from ``events.py`` however I felt as if it is in a better in that file. This file currently has two commands: *INDECISIVE CHOICE COMMAND* and *ROLL FOR ME*.

#### *INDECISIVE CHOICE COMMAND*

Have you ever been indecisive about what you choose next? Well this command solve that problem. Reading the entire message after the command prefix, this command will break up each option between the white space and randomly select from list of options inputted.

**How to call it:**``mister please choose option1 option2 option3``

#### *ROLL FOR ME*

This command takes in a number and then randomly outputs a number created by python's *random library*. However what makes this special is that it can either take in a dice number or a whole number. Rolling a whole number is fairly self explanatory, and there really is nothing different from other implementations. But what makes the dice roll special is that it took inspiration from the TTRPG D&D and sort of is meant to replicate rolling those dice.

**How to call it:**``mister please roll d[die number equivalent to D&D dice]`` or ``mister please roll [number]``

**PLANS FOR FUTURE RELEASES:**
- make the option to roll multiple dice at once. *ex: mister please roll 3d8*
- have the bot edit its message multiple times to show that it is "calculating" a random number
- display an image of the die
- output an error message when the user calls a negative number, as well as other edge cases

### **MISC.PY**

``misc.py`` was probably one of my first cogs when I started understanding cogs, so the old commands in this folder currently do not exist or work since they were either deleted for moved. Future releases will have commands to call from this cog.
