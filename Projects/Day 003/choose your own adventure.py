print('''
   ___------~~~~~~~~~~~----__         .:.         __----~~~~~~~~~~~------___
 ~~ ~--__          ......====\\~~    .:::.    ~~//====......          __--~ ~~
         ~\ ...::::~~~~~~  //|||    .:::::.    |||\\  ~~~~~~::::... /~
        -~~\_            //  |||***.(:::::).***|||  \\            _/~~-
             ~\_        // *******.:|\^^^/|:.******* \\        _/~
                \      / ********.::(>: :<)::.******** \      /
                 \   /  ********.::::\\|//::::.********  \   /
                  \ /   *******.:::::(o o):::::.*******   \ /
                   /.   ******.::::'*|V_V|***`::.******   .\
                     ~~--****.:::'***|___|*****`:.****--~~
                           *.::'***//|___|\\*****`.* 
                           .:'  **/##|___|##\**    .
                          .    (v(VVV)___(VVV)v)
                          ''')

print("Welcome to Dragons Dungeon.")
print("Your mission is to find your way through and survive.") 
player_name = input("Enter your name to begin your adventure: ")

print(f"welcome {player_name} your are a Knight tasked to find the dragon heart (a unique gem the dragon gurards fiercly.) Your kings belives this will bring piece and prosperity to the land")
print("you have been riding for days to the mountain where the dragon lives.")

choice1 = input("as you get close to the mountain you see 2 cave entrances. What cave wil you choose Left or right? ").lower

if choice1 == "left":
    print("as you walk forward the floor gives way beneath you! you fall and hit you head after what seems like hours you wake and find a unlit torch and a tunnle leading one way.")
else:
    print("you choose wrong and spring a trap that fires arrows in your chest. your dead body becomes a delightful snack for the dragon.")

print("you light the torch and begin walking down the tunnel till you come to a clearing where a crevace is blocking your way. as you look for a way across you see a old rope that you can use to swing across. There is also a wooden bridge that looks old and sturdy.")
choice2 = input("you are at an impass will you choose the rope or the bridge? ").lower

if choice2 == "rope":
    print("you chose wisely and swing across the crevace with little effort.")
else:
    print("you start to cross the bridge before you could reach halfway it crumble under your feet and you fall to your death.")


print("after you catch your breath you see a crack in the wall where you can shimy through. As you get close to the other side you see something shining in the distance.")
print("after exiting the crack you see a giant dragon sleeping and sitting slightly off to the side you see the Dragon heart")
print("you decide to make a run for it and grab the gem! The dragon wakes from hearing you armor clanging the dragon see you and takes a swipe at you with its tail")
print("the tail fly's by just missing you knowing you dont have much time you run even harder")
print("The dragon turns and start to move toward you")
print("you come to a wall with 3 caves. you have just a few secounds before the dragon gets to you")

choice3 = input("quickly choose a cave: left, middle, or right? ").lower

if choice3 == "left":
    print("you run forward and slide down the slippery rock falling into water where the weight of you armor drags you to ther bottom and you drown")
elif choice3 == "right":
    print("you were only able to go 10 feet as you turn back you see the dragon at the entrace right before you are burn to death from dragon fire")
else:
    print("you chose wisely and make it out and climb down the mountain to your horse")



print("you ride back to the castle as fast as you can and present the Gem to you king.")
print("as you catch your breath you hear a screeching sound in the distance. The dragon has tracked you back to the castle")
print("A great deal of fear falls over you and the rest of the kingdom as you hear scream from the people")
print("The End")