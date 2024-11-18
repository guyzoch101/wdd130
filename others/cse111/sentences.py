# Tristan Wong
# 1/30/2024
# This program is about generating simple English sentences
# Additional part includes generating an extra prepositional phrase

# random library for generating random words from a list
import random

def main():
    
    # manually entering values for parameters to execute the make_sentence function to generate the 6 required sentences
    sentence_a = make_sentence(quantity = 1, tense = 'past')
    sentence_b = make_sentence(quantity = 1, tense = 'present')
    sentence_c = make_sentence(quantity = 1, tense = 'future')
    sentence_d = make_sentence(quantity = 2, tense = 'past')
    sentence_e = make_sentence(quantity = 2, tense = 'present')
    sentence_f = make_sentence(quantity = 2, tense = 'future')
    print(sentence_a)
    print(sentence_b)
    print(sentence_c)
    print(sentence_d)
    print(sentence_e)
    print(sentence_f)
    
    pass


def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity is 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity is 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    
    if quantity == 1:
        determiner_list = ["a", "one", "the"]
    else:
        determiner_list = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    determiner = random.choice(determiner_list)
    return determiner


def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity is 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"

    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    
    # returns a noun
    if quantity == 1:
        noun_list = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    else:
        noun_list = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]

    noun = random.choice(noun_list)
    return noun


def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
    
    if tense == 'past':
        verb_list = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    elif tense == 'present':
        if quantity == 1:
            verb_list = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
        else:
            verb_list = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    elif tense == 'future':
        verb_list = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
    
    verb = random.choice(verb_list)
    
    return verb


def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """
    
    preposition_list = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on", "onto", "out",
        "over", "past", "to", "under", "with", "without"]
    
    preposition = random.choice(preposition_list)
    
    return preposition


def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed
    of three words: a preposition, a determiner, and a
    noun by calling the get_preposition, get_determiner,
    and get_noun functions.

    Parameter
        quantity: an integer that determines if the
            determiner and noun in the prepositional
            phrase returned from this function should
            be single or pluaral.
    Return: a prepositional phrase.
    """
    
    # Generate the preposition
    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    
    prepositional_phrase = preposition + ' ' + determiner + ' ' + noun
    
    return prepositional_phrase


def make_sentence(quantity, tense):
    """Build and return a sentence with three words:
    a determiner, a noun, and a verb. The grammatical
    quantity of the determiner and noun will match the
    number in the quantity parameter. The grammatical
    quantity and tense of the verb will match the number
    and tense in the quantity and tense parameters.
    """
    
    # Generate the determiner / article
    determiner = get_determiner(quantity)
    
    # Generate the noun
    noun = get_noun(quantity)
    
    # Generate an extra prepositional phrase
    preposition_add = get_preposition()
    determiner_add = get_determiner(quantity)
    noun_add = get_noun(quantity)
    
    extra_prepositional_phrase = preposition_add + ' ' + determiner_add + ' ' + noun_add
    
    # Generate the verb
    verb = get_verb(quantity, tense)
    
    # Generate the prepositional phrase
    prepositional_phrase = get_prepositional_phrase(quantity)
    
    sentence = determiner.capitalize() + ' ' + noun + ' ' + extra_prepositional_phrase + ' ' + verb + ' ' + prepositional_phrase + '.'
    
    return sentence

# start main function
main()