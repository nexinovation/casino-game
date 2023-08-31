import random
from turtle import *
import time
setup(width = 500, height = 200, startx = -200, starty = -600)
#these set up random functions, graphics, time delays, and makes a canvas

#alright! Let's get coding some core pieces of our slot machine!

bank = 1500
#let's make this our starting amount for wagering

#now we need to make 3 shapes for our slot machine:
shape1 = Turtle()
shape2 = Turtle()
shape3 = Turtle()
#This makes 3 graphics objects called "turtles" to act as our 3 shapes
#I would like to align them north (default is east  ---->)
shape1.setheading(90)
shape2.setheading(90)
shape3.setheading(90)

#Now, I want to pick up the pen so they don't leave a line as they move:
shape1.up()
shape2.up()
shape3.up()

#Now I would like to move them and space them apart:
shape1.goto(-100,0)
shape3.goto(100,0)

#let's see what that looks like
#looks good!
#Now let's make a list for our shapes
shapelist = ["square", "circle", "triangle"]
#We will be picking this later on in the program

#Now I want to make a loop to continue playing:
keep_playing = "true"
#Think of this as an on/off switch for the game

while keep_playing == "true":
    #here I told the player how many points they have. This code was copied from Brian Fediuk’s Youtube Channel: https://www.youtube.com/watch?v=9KBLD0A0k1o
    print ("You have",bank,"points to wager.")
    #Here I am asking them to type in their wager and converting it to an integer
    wager = int(input("What is your wager?"))
    if wager > bank:
        #Let's make sure you don't wager more than you have!
        continue
        #this will bring you back to the top of the loop
    bank = bank - wager
    for i in range(3):
        shape1.shape(shapelist[i])
        time.sleep(0.1)
        shape2.shape(shapelist[i])
        time.sleep(0.1)
        shape3.shape(shapelist[i])
        time.sleep(0.1)
        #This allows us to "grab" the responding shape from the shapelist
        #Let's also add a small delay between the shape changes
    #now that we have a working visual, let's check it out!
        #works great!
    #Time to randomly choose and assign the shapes from the shapelist. This code was copied from Brian Fediuk’s Youtube Channel: https://www.youtube.com/watch?v=9KBLD0A0k1o
    result1 = random.choice(shapelist)
    shape1.shape(result1)
    result2 = random.choice(shapelist)
    shape2.shape(result2)
    result3 = random.choice(shapelist)
    #oops, silly typo. My bad!
    #let's test again
    shape3.shape(result3)
    #this chooses a random shape from shapelist and assigns it to each shape
    #let's test it out! This code was copied from Brian Fediuk’s Youtube Channel: https://www.youtube.com/watch?v=9KBLD0A0k1o
    #tiny error, but we're back on track!

    #okay, now time to determine the winning combinations.
#I'm going to be efficient in this coding (also lazy)
    #first, determine if all 3 results are the same
    if result1 == result2 and result2 == result3:
        #then, if the results are squares, do this:
        if result1 == "square":
            #give them a winning message
            print ("WINNER 3 SQUARES!")
            #multiply their wager times 5
            wager = wager * 5
            #put the increased wager winnings back into the bank
            bank = bank + wager
        elif result1 == "circle":
            print ("WINNER 3 CIRCLES!")
            wager = wager * 15
            bank = bank + wager
        elif result1 == "triangle":
            print ("WINNER 3 TRIANGLES!")
            wager = wager * 25
            bank = bank + wager
            #one thing to note here:
            #these payouts are not fair at all and will almost guarantee
            #that the people playing the game win a lot
            #change the wagers appropriately to reflect "casino" style play
        #in the event that not all 3 shapes match, default to this message:
        else:
            print ("Sorry! You lose!")
        #let's try it out again!
            #okay, let's wrap it up with asking them if they want to keep playing This code was copied from Brian Fediuk’s Youtube Channel: https://www.youtube.com/watch?v=9KBLD0A0k1o
    #ask them an input about playing more
    prompt = input("Would you like to keep playing?")
    #if the answer is No or NO or no, set that "switch" to off
    if prompt == "no" or prompt == "NO" or prompt == "No":
        keep_playing == "false"








