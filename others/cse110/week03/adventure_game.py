# occasional double quotes are used for apostrophe sentences
# a key, a tip bag, and a tools bag is added as secret options, which can lead the user to unexpected endings
# multiple outcomes if entering the riddle scenario
# a random function is added for the lottery wheel

# constantly dying annoyed them, as some scenarios require secret options(using key, tip bag or tools bag) to pass

start = input("Welcome to Adventure 101. To start, please press 'ENTER'")
print('You woke up and found yourself in a dark forest, and it was raining and cold.')
print('Searching the bushes along the path, you feel that there is something crawling on your shoulder.')
print("Luckily, it is just the sound of raindrops. 'Plak!!!'")
beginning = input('Follow the SOUND or walk along the PATH? \n')

if beginning.lower() == 'sound':
    print('\nIt turns out, the sound is from a secret tunnel. As you search along the secret tunnel,')
    print('you have been approached by the guardian of the Gates of Wisdom. To proceed through the gates,')
    print('you must answer a riddle.')
    tunnel_checkpoint = input('Answer the RIDDLE, walk across the ROPE BRIDGE or crawl and reach the other side of the WALL? \n')

    if tunnel_checkpoint.lower() == 'riddle':
        print('\nHere is the riddle:')
        print("'In the kitchen cupboard, there are 3 jars containing different items.")
        print('Sugar is to the right of rice and flour is to the right of sugar.')
        print("What is in the middle?'")
        riddle_answer = input('RICE, FLOUR, or SUGAR? \n')
        
        if riddle_answer.lower() == 'sugar':
            print('\nCorrect! You are allowed to proceed through the Gates of Wisdom.')
            print('You have also received a Key and a Tools Bag, which may come in handy.')
            print('As you make a turn after passing the gate, a beacon of light is seen ahead.')
            print('Congratulations! You have made it out of the secret tunnel.')
            print("'Beep~ Beep~' The guardian offers you a ride.")
            tunnel_outlet = input('HOP ON or KEEP WALKING? \n')
            
            if tunnel_outlet.lower() == 'hop on':
                print('\nThe identity of the guardian is extremely mysterious, yet it seems like he is a nice guy.')
                print('A few minutes later, you have arrived at a hut. The door is locked,')
                print('but there is a box slicking out of the mailbox. ')
                mailbox = input('OPEN the mailbox? \n')
                
                if mailbox.lower() == 'open':
                    print('\nCongratulations! YOu have found a gift - a stack of cash.')
                
                # hidden option    
                elif mailbox.lower() == 'key':
                    print('\nCongratulations! You have found a secret gift - the hut turns out is full of fond')
                    print('memories with your loved one. Now, you finally remember who you are.')
                    
                else:
                    print('\nYou have been struck by lightning.')
            
            elif tunnel_outlet.lower() == 'keep walking':
                print('\nIt seems like it takes forever to get out of the forest.')
                print('Meanwhile, the rain is getting heavier, and the weather is getting colder.')
                print('Luckily, not far from here, there is a house.')
                house = input('Get INSIDE? \n')
                
                if house.lower() == 'inside':
                    print('\nIt is getting colder and colder, and it is too cold to stay outside.')
                    print('You have fainted due to the cold.')
                
                # secret option    
                elif house.lower() == 'tools bag':
                    print('\nTold you this would come in handy, here is a raincoat and a heat bag.')
                    house_with_tools = input('Continue walking to the HOUSE? \n')
                    
                    if house_with_tools.lower() == 'house':
                        print('\nThe house looks fancy from the outside.')
                        enter_house = input('Get INSIDE? \n')
                        
                        if enter_house.lower() == 'inside':
                            print('\nCongratulations! You found some fresh hot chocolate inside the house.')
                        
                        # secret option    
                        elif enter_house.lower() == 'key':
                            print('\nCongratulations! You have found a secret gift - a time capsule which holds your childhood memories.')
                            
                        else:
                            print('\nMaybe next time.')
                            
                    else:
                        print('\nThe owner saw you wandering in the cold, and invited you to join them for dinner.')
                    
                else:
                    print('\n2 police were patrolling near the house, and you were mistaken as a theif. You are arrested.')

            else:
                print('\nThe rain is getting heavier, and the weather is getting colder. You are frozen and died due to the cold.')

        elif riddle_answer.lower() in('rice', 'flour'):
            print('\nSeems like you got the wrong answer, but the guardian dropped a Tip Bag, which may come in handy.')
            riddle_failed_out = input('The only way out is across the ROPE BRIDGE or crawl to the other side of the WALL. \n')
            
            if riddle_failed_out.lower() == 'rope bridge':
                print('\nThe rope bridge is too weak and breaks as you are crossing. You died due to falling from heights.')
                
            elif riddle_failed_out.lower() == 'wall':
                print('\nLuckily, you are a rock climber. Climbing the wall is a piece of cake. But there are some markings on the wall.')
                cave = input("It says, 'A gift you seek is inside a CAVE, but only the bravest of the bravest is allowed to enter.' \n")
                
                if cave.lower() == 'cave':
                    print('\nYou have triggered traps as you enter the cave, and you are locked inside a cage.')
                
                # secret option
                elif cave.lower() == 'tip bag':
                    print('\nThere are multiple traps set along the entrance of the cave.')
                    evade = input('EVADE the triggers of the traps. \n')

                    if evade.lower() == 'evade':
                        print('\nCongratulations! You have reached the end of the secret tunnel and granted a wish.')

                    else:
                        print('\nYou triggered a switch as you were reading the tip, and you have been hit by a poisonous dart.')
                
                else:
                    print('\nYou are trapped inside the tunnel, as the tunnel is enchanted and its exits are constantly moving.')
                
            else:
                print('\nIt turned out the air inside the tunnel is radioactive and you have stayed too long inside the tunnel.')
                print('You died due to radiation.')
        
        else:
            print('\nThis is not in any of the choices provided. You must not proceed through the gates.')
            print('Unfortunately, you have triggered a trap as you were leaving.')
            print('You were shot by a poisonous dart.')

    elif tunnel_checkpoint.lower() == 'rope bridge':
        print('\nThe rope bridge is too weak and breaks as you were crossing.')
        print('Luckily, you grabbed on a branch as you fell.')
        bridge_broke = input('CLIMB back to the top? \n')
        
        if bridge_broke.lower() == 'climb':
            print('\nYou slipped as you were climbing, and you died unfortunately.')
            
        else:
            print('\nSuddenly, you woke up, and all of those was just a dream.')
    
    elif tunnel_checkpoint.lower() == 'wall':
        print('\nLuckily, you are a rock climber. Climbing the wall is a piece of cake. But there are some markings on the wall.')
        cave = input("It says, 'A gift you seek is inside a CAVE, but only the bravest of the bravest is allowed to enter.' \n")

        if cave.lower() == 'cave':
            print('\nYou have triggered traps as you enter the cave, and you are locked inside a dark room.')
        
        else:
            print('\nThe wall collapsed due to an unexpected earthquake. You are sqashed by the wall.')
        
    else:
        print('\nYou have approached a dead end and are trapped inside the tunnel.')

elif beginning.lower() == 'path':
    print('\nSuddenly, the path is getting darker and darker. As you struggle to see what is ahead.')
    print('You have come to a split end.')
    path_side = input('Take the path to the LEFT or to the RIGHT? \n')

    if path_side.lower() == 'left':
        print('\nAs the path is too dark, you cannot see what is ahead, and you slip and fell into a giant hole.')
        
    elif path_side.lower() == 'right':
        print('\nGlad you chose the right side!')
        right_shop = input('There is a STORE and a RESTAURANT not far away. \n')
        
        if right_shop.lower() == 'store':
            print('\nCongratulations! You are the 10th thousand customer of the day and you awarded $1000 gift coupons as a prize.')
            
        elif right_shop.lower() == 'restaurant':
            print('\nAfter a ong walk, you have decided to treat yourself with a slice of pepperoni pizza.')
            lottery_wheel = input('Somehow, anyone who orders a slice of pepperoni pizza will get the chance to spin the LOTTERY WHEEL. \n')
            
            if lottery_wheel.lower() == 'lottery wheel':
                import random
                list_lottery = [0, 1, 5, 10, 25, 50, 100]
                prize = random.choice(list_lottery)
                
                if prize == '0':
                    print('\nSorry! You won $0, thank you for spinning.')
                    
                else:
                    print(f'\nCongratulations! You have won ${prize}.')
                
            else:
                print('\nAlthough you did not find anything, it is glad that nothing big happened after a horrifying adventure.')
        
        else:
            print('\nAfter a long adventure, you have starved to death since you did not eat anything for the whole day.')
    
    else:
        print('\nA car bumped into you as you were standing in the middle of the road.')

else:
    print('\nYou accidentally found a secret path and it is a shortcut. Yet, you have come to a split end.')
    print('The 2 trails ahead have different colours.')
    trail_colour = input('Take the RED path or the GREEN path? \n')
    
    if trail_colour.lower() == 'red':
        print('\nIt turned out that you were followed by an assassin, and you were kidnapped.')
        
    elif trail_colour.lower() == 'green':
        print('\nYou discovered you were followed by someone.')
        reaction_green = input('RUN or COUNTER? \n')
        
        if reaction_green.lower() == 'run':
            print()
            map = input('You accidentally ran to a dock, and it turned out there was a TREASURE MAP hidden in a boat. \n')
            
            if map.lower() == 'treasure map':
                print('\nYou sailed across the river to ditch the assassin.')
                print('Congratulations! You have found a treasure chest.')
                
            else:
                print('\nYou were caught by the assassin and killed.')
        
        elif reaction_green.lower() == 'counter':
            print('\nYou were outpowered by the assassin and got killed.')
            
        else:
            print('\nIt turned out he was just an old friend, you two then went to a restaurant and had a good night.')
    
    else:
        print('\nYou think that this adventure is too dangerous and give up on searching for the treasure. You safely returned home.')