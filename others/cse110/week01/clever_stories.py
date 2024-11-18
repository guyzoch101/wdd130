#the variables 'sound', 'movie', and 'random' are the self-added part and the part after 'right in front of my family.' is the self-added part
#these are added to create the extended ending of the whole story is just a dream, or is it?
adjective = input('Enter an adjective: ')
animal = input('Enter an animal: ')
verb_alpha = input('Enter a verb: ')
verb_beta = input('Enter another verb: ')
verb_gamma = input('One more verb please (last verb, I promise): ')
exclamation = input('Enter an exclamation: ')
print()
#additional parts
sound = input('Put down a sound that pops up in your mind: ')
movie = input('Enter your favourite movie: ')
random = input('Write down any word or phrase: ')

print()
print('The other day, I was really in trouble. It all started when I saw a very')
print(f'{adjective.lower()} {animal.lower()} {verb_alpha.lower()} down the hallway. "{exclamation.capitalize()}!" I yelled. But all')
print(f'I could think to do was to {verb_beta.lower()} over and over. Miraculously,')
print(f'that caused it to stop, but not before it tried to {verb_gamma.lower()}')
print('right in front of my family.')
#additional parts
print(f'"{sound.capitalize()}~"')
print('"Phew, luckily it was just a dream."')
print(f'Suddenly, I heard some noise in the living room , it was the very {adjective.lower()} {animal.lower()}, watching {movie.title()}. ')
print(f'"{random.upper()}!" The {adjective.lower()} {animal.lower()} shouted.')