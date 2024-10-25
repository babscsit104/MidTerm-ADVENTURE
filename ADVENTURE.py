# Barbara Manzanarez, ADVENTURE
# 

player = input("Type your name: ")
print("Welcome", player, "to this adventure!")

print("You wake up to find yourself in a cold, dark cave. The air is damp, and the faint echo of dripping water fills your ears. You have no memory of how you got here. \nAs you get up and dust yourself off, you notice two paths ahead:")
print("- To your left, a narrow tunnel leads deeper into darkness. The air is colder there, and you can faintly hear the sound of rushing water.")
print("- To your right, a wider passage seems to have some light coming from it. The source of the light is unclear, but you hear distant whispers echoing from within.")
print("You realize you must choose quickly before your courage fades away.")

answer = input("go left or go right? (left/right)")

if answer == "left":
    print("You decide to brave the narrow, dark tunnel, following the sound of rushing water.")
    print("You find a waterfall, leading to a river")

    answer = input("go to the waterfall or the river? (waterfall/river)")

    if answer == "waterfall":
        print("You go towards the waterfall and notice there's an opening being covered by it. You go inside.")
        print("It's not that deep, but you notice a treasure chest to the left, and right infront the little passage keeps going.")

        answer == input("open the chest or continue foward? (open/keep going)")

        if answer == "open":
            # MIMIC END
            print("You decide to open the chtes, after all it's been an adventure and you wouldn't mind getting some treasure out of the whole deal.")
            print("As you approch it, the chest seems to open on it's own and next thing you know, everything is black.")
            print("Sadly, it seems that the treasure wanted you more than you wanted it.")

        else: 
            print("You keeping foward, and encounter a weathered stone altar, with markings all over the walls. ")
            print("Curiosity gets the best of you, what would happen if..")

            answer = input("you desecrated the altar, or prayed on it? (desecrate/pray)")

            if answer == "desecrate":
                # CAVE END
                print("You're tired from being in the cave, from not yet finding a way out and in anger you decide to make the altar the target of your fury by grabbing chunks of rock and smashing the altar.")
                print("Rocks start falling around you. It seems the stability of the cave relied on the altar...which you destroyed")
                print("It seems you died this time by the cave collapsing on you, at least whatever god the altar belonged to isn't furious with you, right?")

            else:
                #GOD END
                print("You're tired from being in the cave, but that doesn't stop you from doing a little silly. You get on your knees infront of the altar and start to pray.")
                print("Suddenly, you are no longer in the cave. Only water as far as the eye can see, and a starry sky colored with pink and green.")
                print("The God the altar belonged to hear you pray, and decided to keep you. Welcome to your future, eternal beliver.")

    else: 
        print("You decide to follow the river, and get away from the harsh sounds that the waterfall creates")
        print("While walking, you feel something sticky...slimy crawl up your leg you look down and it seems to be a tentacle? with none of the suckers that octopi have.")

        answer = input("try to get rid of it, or allow it to take you? (fight it/follow it)")

        if answer == "fight it":
            # DROWNED END
            print("In a panic you shake your leg to try and make the tentacle let go of you, but  the tentacle just tightens around you leg and pulls-")
            print("Let's hope you know how to swim, cuz if not, I guess this is your end.")

        else:
            # TENTACLE * END (LOL)
            print("You have never seen something like this so, for best or for worse curiosity gets the best of you and with no fight, the tentacle grabs you and pulls you into the water")
            print("Weirdly, you can breath underwater, and thus the tentacle continues to pull you further and further down, where no longer the light reaches")
            print("All around you seems to move, but it is no longer water. The tentacle has pulled you all the way down to the core of it's existence")
            print("It wants you there, with it. How romantic of it, no?")


else:
    print("You choose to investigate the wider passage, drawn by the mysterious light and whispers.")
    print("At the end of the passage, you notice an adventurer sitting infront of a bonfire humming to himself, his weapon discarded to the side.")
    
    answer = input("talk with the adventurer or take his weapons? (talk/take)")

    if answer == "talk":
        print("You approch the adventurer, and sit down in the stone next to him. He takes a look at you and asks you if you want to join him.")

        answer = input("join the adventurer? (yes/no)")

        if answer == "yes":
            # FREEDOM END
            print("You accept his offer to join, and start making plans for where to go next")
            print("The adventurer wants to go back to town, after finding out you've been in the cave unconcious for an unknown period of time.")
            print("Touched by his compassion, and care you accept the trip to a town. Following the adventurer, you finally see the outside world in who knows how long...")
            print("Look's like it's a happy ending for all")

        else: 
            # STOLKHOM END
            print("You decline the offer to join. The adventurer nods in understanding, and goes to his sack to sleep. He has more adventuring to do later")
            print("But you don't, do you? That's why you want to stay in the cave.")
            
    else:
        # STEAL END
        print("You decide to take the weapon closest to you in a hurry. As soon as you get your hand meets the handle, the adventurer hits you on the head HARD and you pass out.")
        print("You didn't think you'd get away with it, did you?")