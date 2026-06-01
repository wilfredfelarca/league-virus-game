# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define i = Character("Infected")
define d = Character("Doctor Milo")
define w = Character("Wilfred")
define m = Character("Mon")
define l = Character("louie")



# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.
    
    "If you are witnessing this broadcast, there is an active anomaly within your area"
    
    "Remain indoors"
    
    "Lock and Board up all entrances"
    
    "Keep a weapon nearby at all occasions"
    
    "DO NOT RESPOND TO VOICES ASKING YOU TO PLAY \"League of Legends\""
    
    "Even if the voice is someone you know"
    
    d "Good Evening"

    d "You may not know me"
    
    d "but I'm the head of the League Infection Group Monitoring Association"

    d "L.I.G.M.A for short"
    
    d "If you are watching this, then you are within the vicinity of an anomaly called a \"League Player\""
    
    d "These anomalies can be categorized to three mutations:"
    
    d "Casual Players (Threat Level: 2/5)"
    
    d "Ranked Players (Threat Level: 4/5)"
    
    d "Yasuo Players (Threat Level: 5/5)"
    
    d "All anomalies share attributes such as:"
    
    d "Hunched backs"
    
    d "Raspy voices"
    
    d "Short"
    
    d "When in the vicinity of a League Player, remain calm"
    
    d "Engage in conversation not in relation to the parasite"
    
    d "topics such as family, music, and art are encouraged"
    
    jump interview
    
    label interview:
    
    "sequence 2 start"
    
    
    # This ends the game.

    return
