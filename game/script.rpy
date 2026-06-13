# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define i = Character(_("Infected"), color="#33ccbb")
define d = Character(_("Doctor Milo"), color="#5b9c5a")
define w = Character(_("Wilfred"), color="#a755b3")
define m = Character(_("Mon"), color="#e780c8")
define l = Character(_("Louie"), color="#f6ff00")
# define p = Character(_("Placeholder"), color="#fffff")



# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene static bg with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    scene warning bg with fade

    # sequence 1 start
    
    
    "If you are witnessing this broadcast, there is an active anomaly within your area."
    scene home instructions bg with fade
    "Remain indoors."
    scene home instructions b bg 
    "Lock and board up all entrances."
    scene home instructions c bg 
    "Keep a weapon nearby at all occasions."
    scene home instructions d bg with fade
    "DO NOT RESPOND TO VOICES ASKING YOU TO PLAY \"League of Legends\". "
    "Even if the voice is someone you know..."
    
    scene black with fade
    scene sq1_drmilo_a with fade
    d "Good evening."
    d "You may not know me,"
    scene sq1_drmilo_b
    d "But I'm the head of the League Infection Group Monitoring Association,"
    d "L.I.G.M.A for short."
    scene proximity league bg with fade
    d "If you are watching this, then you are within the vicinity of an anomaly called a \"League Player\". "
    
    scene variants bg
    d "These anomalies can be categorized to three mutations:"
    d "Casual Players (Threat Level: 2/5)"
    d "Ranked Players (Threat Level: 4/5)"
    d "Yasuo Players (Threat Level: 5/5)"
    
  
    d "All anomalies share attributes such as:"
    scene similiar a with fade
    d "Hunched backs"
    scene similiar b with dissolve
    d "Raspy voices"
    scene similiar c with dissolve
    d "Short"
   
    scene proximity league bg with fade
    d "When in the vicinity of a league player, remain calm."
    d "Engage in conversation not in relation to the parasite."
    scene engage conversation bg 
    d "topics such as family, music, and art are encouraged."
    
    
    # sequence 1 end
    
    jump interview
    
    
    
    label interview:
    
    # sequence 2 start

    scene black with fade
    
    w "Please state your name."
    
    m "Mon Kennedy."
    
    w "And what is your relation with the infected?"
    
    m "Colleague."
    
    scene sq2_interview_e with fade
    w "You reported that this friend of yours has been displaying potential anomaly behavior?"
    w "May you elaborate on that, please."
    
    scene sq2_interview_a with dissolve
    m "Sure..."
    m "At first, I assumed Cole was just burnt out..."
    scene sq2_interview_c with dissolve
    m "She'd snap over the smallest things or look exhausted, but all of us in the office did."
    m "So I paid it no mind until..."
    
    scene black with fade
    # "*Mon takes a deep breath and returns to their testimony*" 
    
    
    m "She started acting... weird."
    m "Missing meetings, Clocking in late, Submitting unfinished reports..."
    scene cole apartment bg with fade
    m "I got worried so I decided to visit their apartment."
    m "I thought they were going through something rough since her and her girlfriend Iuno broke up but..."
    m "Oh god..."
    
    
    # "*rubs their head temples" removes this since this is just direction

    scene cole playing league bg with fade
    m "I was too late."
    m "She was hunched over a laptop... playing support."
    m "The in game timer saying \"14:41\"... "
    m "if I only knew earlier I could've-"
        
    scene sq2_interview_d with fade
    w "So the threat level was low..."
    w "What happened next?"
    
    scene sq2_interview_c with dissolve
    m "She turned around and asked \"Mon, play league of legends\". "
    scene sq2_interview_b with dissolve
    m "I- I didn't know what to do! that keyboard and mouse looked like it was attached to them!"
    m "When I said no, they started showing me the characters, the animations, the story and-"

    scene static bg with pixellate
    #"*footage corrupts*"
    
    # "*suddenly cuts to a news broadcast*"
    
    # sequence 2 end
    
    jump infection
    
    
    
    label infection:
    
    # sequence 3 start
    
    #"*Show an interview area between the two*"\
    
    scene sq3_podcast_a with pixellate
    l "Welcome chat to the \"ThemPodcasts\". "
    l "I'm your host Louie and today we have a special guest."
    scene sq3_podcast_b
    l "Please welcome Doctor Milo of L.I.G.M.A.!"
    
    d "It's good to be here."
    scene sq3_podcast_a
    l "I don't wanna dance around the issue's Doctor, so let's try to break the ice."
    l "What are your thoughts on these \"League Defenders\" stating that playing League of Legends is a \"New Era of Esports\". "
    
    scene sq3_podcast_c
    d "They are either blind to the current epidemic and choose to spew harmful rhetoric,"
    d "Or have started showing early signs of infection."
    
    scene sq3_podcast_b
    l "You're quite sure, mind tell the viewers then at home what the signs of infection are?"
    
    scene sq3_podcast_d with pixellate #*cut to a presentation
    
    "Stage 1) Actively seeking external Media"
    "The infected has grown an insatiable need to consume media surrounding the \"league of Legends\" IP such as... "
    "Arcane"
    "2XKO"
    "KDA, Heartsteel and Pentakill"
    "Goons to the characters"
    
    scene sq3_podcast_e with fade
    "Stage 2) The Queue"
    "The infected had downloaded the client and is queueing for casual games, slowly secluding themselves from the world."
    "Do note they are highly dangerous in hordes as they will invite you to join in their \"Lobby\". " 
    
    scene sq3_podcast_f with fade
    "Stage 3) Ranked Player"
    "A point of no return; will often be heard muttering about \"LP\" and \"Placements\" whilst in the lobby."
    "Will STOP playing characters they love and resign to playing \"Meta picks\". "
    
    scene sq3_podcast_g with fade
    "Final Stage) Yasuo Players"
    "They auto lock Yasuo"
    
    
    scene sq3_podcast_b with fade # "*Cut back to the interview*"
    l "Those are quite drastic."
    scene sq3_podcast_a
    l "But with something so futile and symptoms being often mixed with anti-social behavior..."
    l "What are we gonna do now?"
    
    scene sq3_podcast_c
    d "I... don't know."
    
    scene static bg with fade
    
    # sequence 3 end
    
    jump look
    
    label look:
    
    # sequence 4 start
    
    scene sq4_kys with pixellate
    "In the event of an encounter with a league player, follow the K.Y.S protocol-"

    # "*Inserts a ccv footage of the detective and the victim watching the infected by the other side of the glass*"
    scene static bg with fade

    scene sq4_a with fade
    i "How... to capture... the... baron... buff..."
    
    w "She seems to show late stages of transformation."
    w "If you don't mind, may you repeat to me the last moments before you reported the infection?"
    
    scene sq4_b with dissolve
    m "Right..."
    
    # "*Cut to a scene where it shows Mon by the door frame as the infected charges at them*"
    
    scene sq4_c with dissolve
    m "It happened so quickly, they wouldn't stop yapping about \"Sona\" and started showing me cinematics of her."
    m "Their eyes look strained, their frame shaking and their voice hoarse..."
    m "But I sat there and listened."
    
    scene sq4_shooketh_d with vpunch
    w "-!"
    
    # "*Cut back to the cctv footage of Wilfred and Mon chatting at the room*"
    
    scene sq4_kys with dissolve
    "The K.Y.S protocol."
    scene sq4_kys_k with pixellate
    "KNOW THE SYMPTOMS."
    scene proximity league bg
    "When in the vicinity of the infected and/or infected area, check your symptoms."
    scene sq4_kys_symps with dissolve 
    "Follow the relating symptoms on screen:"
    
    # "*Show symptoms that Doctor Milo was talking about*"

    scene sq4_kys_hotline 
    "If you show any signs of infection then call the L.I.G.M.A Hotline 6769-0420-911."
    
    # "*cuts back to Mon and Wilfred via glitching*"

    scene sq4_c with pixellate
    w "You what...?"
    
    m "To be fair,"
    m " Sylas is pretty hot and the KDA skins serve so much."
    
    w "If you really like the visuals of the characters, you should try 2XKO-"
    
    scene sq4_e with vpunch
    "-!?"
    
    i "Do you like Sylas?"
    i "He's pretty simple to learn in midlane, you can join my lobby and we can play a bot match-"
    
    # "*Wilfred shines his phone with a picture of grass*"
    
    scene sq4_h with vpunch
    w "GET BACK!"
    
    scene sq4_f with vpunch
    i "AAAAAAAAAAAAHHH!"
    
    scene sq4_kys with fade
    # TODO: Cole I have Shizuku merch I genuinely havent given u lol finish this one
    "The K.Y.S Protocol"
    scene sq4_kys_y
    "YELL FOR HELP"
    scene proximity league bg
    "When in close contact with an infected league player, do not hesitate to yell for help."
    scene sq4_kys_help
    "Sometimes even directly yelling at them can help neutralize the threat for a short period of time,"
    scene sq4_kys_help_b
    "So one can easily extract themself from the situation at hand."
    
    # "*glitch back to the cctv footage of detective wilfred and victim mon*"
    
    scene sq4_e with fade
    w "I don't think there's any saving for these \"people...\". "
    w "They're in too deep... I fear not even touching grass could save them..."

    # WE DONT HAVE EDITED IMAGES OF THIS FUCK
    scene sq4_i with vpunch
    m "WHAT?!"
    m "Then what about our friends, our families, who've been infected?"
    m "We can't just abandon them!"
    m "Besides, what if the virus spreads even wider and reaches more people?"
    m "It's not safe out there anymore, anyone could get infected."
    m "And I sure as hell don't want to be part of that... crowd..."
    
    scene black
    "*BANG BANG*"
    
    # "*As the pair looked back at the window, a sudden crack was now visible.*"
    
    scene sq4_f with fade
    i "Please... play... league... of.... legends..."
    i "Join... us..."
    
    scene sq4_i with vpunch
    m "Is this our cue to leave?"
    
    # "*Before both of them could react, the window shattered due to the excessive banging of the infected.*"
    # "*One of the infected flopped on the floor, muttering erratically about being restricted from the game for saying some bad, bad words...*"
    
    scene sq4_f with vpunch
    i "They're all #*&@#&*!!! Now... I can't... play..."
    i "HELP ME PLEASE, GOD HELP ME..."
    
    scene sq6_g with hpunch
    w "RUN!!!"
    
    scene sq4_runaway with hpunch
    m "Wha- I'll try!"
    
    scene sq4_kys with fade
    "The K.Y.S Protocol"
    scene sq4_kys_s
    "SECLUDE YOURSELF FROM THE INFECTED"
    "As much as possible, do not interact with the infected yourselves."
    scene engage conversation bg
    "By doing so, you are putting yourself at a higher risk of contracting the infection."
    "Instead, find an empty room with a lockable door and seclude yourself from the infected."
    "Whatever you do, do Not let them in under any circumstances."
    scene sq4_kys
    "The K.Y.S protocol."
    "Remember, to Keep Yourself Safe."
    
    
    # sequence 4 end
    
    jump attempt
    
    label attempt:
    
    # sequence 5 start
    scene sq5_d with fade
    # "*Cut to a messy study*"
    # "*Cut to Doctor Milo having a chat with Louie via video call*"
    
    scene sq5_a with dissolve
    l "Alright, we can schedule you for Tuesday 9:00PM, gotcha?"
    
    d "Yeah... I'll have my new discovery before that..."
    
    l "Alright, thanks... By the way,"
    l "How's it like being infected? AHAHA-!"
    
    scene sq5_b
    d "Fuck you."
    
    scene sq5_c with fade
    # "*Milo hangs up as lay back at their chair*"
    
    d "No, this isn't it..."
    
    # "*flash photo of a messy desk filled with papers and scribbles*"
    scene sq5_d with fade 
    d "All of these leads are incompatible with the virus..."
    d "There's slight aversions to it but not outright reversing of the symptoms."
    
    #"*Shows a close up of a framed photo of Milo and a potted plant*"
    scene sq5_e
    d "Whenever I show them pictures of nature, it does nothing but temporarily terrify them, so exposure therapy's a no go"
    d "Though... taking a closer look may help us to understand this..."
    
    #"*cut to Doctor Milo opening their computer to the website of the league of legends*"
    
    scene sq5_h with dissolve
    d "Maybe... just maybe... If I learnt more about the source of where this virus is coming from,"
    scene black with fade
    d "then maybe..."
    scene sq5_i with fade
    d "I can get to the bottom of it."
    
    scene black with fade
    "*Hours passed by*"
    
    scene sq5_milo league_c with dissolve
    d "Huh... Warwick... Rengar..."
    d "Not bad... I...."
    d "I perhaps see the appeal to this... monstrosity..."
    
    # "*show the infected tied up in the corner*"
    
    scene sq5_f with vpunch
    i "See...! You get it...!"
    i "You want to try how Warwick plays in a game? If you lend me your laptop-"
    
    scene sq5_milo league_b with vpunch
    d "NOT gonna happen."
    
    scene black with fade
    "*A few more hours later... "
    # but to Milo hunched over the laptop*"
    
    scene sq5_milo league_a with dissolve
    d "Yeah, I got nothing."
    scene sq5_milo league_c
    d "Warwick's hot though"
    scene sq5_milo league_c with vpunch
    d "-!?"
    d "What... What time is it?"
    
    #"*Doctor Milo turns to look at the clock on their desk,*"
    #"*Shocked to find out it's been 6 hours ever since they started researching information about League of Legends*"
    
    scene sq5_milo league_e with dissolve
    d "IT'S BEEN 6 HOURS? OH, THIS IS BAD..."
    d "THIS IS REALLY BAD... I've consumed too much... What if..."
    
    # "*Pushes away from their table and stands, letting some items fall*"
    scene sq5_g with fade
    d "What if I'm next?..."
    d "No... I can't... I..."
    
    scene black with fade
    
    d "I can't be next..."
    
    scene static bg with fade
    # "*cut back to Mon and Wilfred*"
    
    # sequence 5 end
    
    jump end
    
    label end:
    
    # sequence 6 start
    
    "*BANG BANG BANG*"
    
    m "W-What do we do, detective?!... They know we're in here, we're trapped!..."
    
    i "Come... Out... We know... You wanna... play league..."
    i "Join the lobby!... Hop on League!"
    i "League is fun!... You both won't regret it, trust us!"
    
    w "There's no point in fighting it anymore, Mon."
    w "We can't escape this..."
    w "Like what the philosopher Euridel Bo has said,"
    w " \"Everyone has tried league at least once in their lives.\" "
    w "And it's not always guaranteed they end up infected like the others."
    
    m "Wait... You're so right, I've played league once when I was 13 and it never stuck..."
    
    w "You... what?"
    
    m "It... It never stuck... Maybe"
    
    "*cut to the door*"
    
    m "Just maybe... there is a cure."
    
    "*cut to the door slamming open*"
    "*Fade out to show a monitor that held all the tapes we watched*"
    "*Cut to a first person POV who's been watching these tapes*"
    "*As they turn to the side, showing all the infected watching them watch the tapes*"
    "Fades to black"
    "THE END"
    
    # sequence 6 end     
    
    # This ends the game.

    return
