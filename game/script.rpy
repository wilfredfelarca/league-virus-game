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

    # sequence 1 start
    
    """
    If you are witnessing this broadcast, there is an active anomaly within your area
    Remain indoors
    
    Lock and Board up all entrances
    
    Keep a weapon nearby at all occasions
    
    DO NOT RESPOND TO VOICES ASKING YOU TO PLAY \"League of Legends\"
    
    Even if the voice is someone you know
    """
    
    d""" 
    Good Evening
    
    You may not know me
    
    But I'm the head of the League Infection Group Monitoring Association
    
    L.I.G.M.A for short
    
    If you are watching this, then you are within the vicinity of an anomaly called a \"League Player\"
    
    """
  
    d """
    These anomalies can be categorized to three mutations:
    
    Casual Players (Threat Level: 2/5)
    
    Ranked Players (Threat Level: 4/5)
    
    Yasuo Players (Threat Level: 5/5)
    """
    
    d """
    All anomalies share attributes such as:
    
    Hunched backs
    
    Raspy voices
    
    Short
    """
    
    d """
    When in the vicinity of a League Player, remain calm
    
    Engage in conversation not in relation to the parasite
    
    topics such as family, music, and art are encouraged
    """
    
    # sequence 1 end
    
    jump interview
    
    label interview:
    
    # sequence 2 start
    
    w "Please state your name"
    
    m "Mon Kennedy"
    
    w "And what is your relation with the infected?"
    
    m "Colleague"
    
    w """
    You reported that this friend of yours has been displaying potential anomaly behavior?
    
    May you elaborate on that, please
    """
    
    m """ 
    Sure...
    
    At first, I assumed Cole was just burnt out...
    
    She'd snap over the smallest things or look exhausted, but all of us in the office did
    
    So I paid it no mind until...
    """
    
    "*Mon takes a deep breath and returns to their testimony*"
    
    m """ 
    Then... she started acting weird.
    
    Missing meetings. Clocking in late. Submitting unfinished reports
    
    I got worried so I decided to visit their apartment
    
    I thought they were going through something rough since her and her girlfriend Iuno broke up but-
    
    Oh god...
    """
    
    "*rubs their head temples"

    m """
    I was too late
    
    She was hunched over a laptop... playing support.
    
    The in game timer saying \"14:41\"
    
    if I only knew earlier I could've-
    """    
    
    w """ 
    So the threat level was low...
    
    What happened next?
    """
    
    m """
    She turned around and asked \"Mon, play league of legends\"
    
    I didn't know what to do, that laptop looked like it was attached to them!
    
    When I said no, they started showing me the characters, the animations, the story and
    """
    
    "*footage corrupts*"
    
    "*suddenly cuts to a news broadcast*"
    
    # sequence 2 end
    
    jump infection
    
    label infection:
    
    "*Show an interview area between the two*"
    
    # This ends the game.

    return
