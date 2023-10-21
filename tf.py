import random

# Define lists of adjectives and nouns to use in the insult
adjectives = ["villainous", "misanthropic", "miscreant", "pribbling", "rump-fed", "maggot-pie", "dankish", "spongy", "clapper-clawed", "flap-dragon", "beef-witted", "loggerheaded", "gorbellied", "plume-plucked", "bottle-bodied", "swag-bellied", "roguish", "boil-brained", "toad-spotted", "fusty", "canker-blossom", "scurvy-knave", "lily-livered", "scurilous", "fustilarian", "hasty-witted", "saucy", "mewling", "craven", "bootless", "spleeny"]
nouns = ["knave", "scoundrel", "vagabond", "wretch", "varlet", "miscreant", "rascal", "reprobate", "villain", "rapscallion"]

# Create a Markov chain to generate the insult
def generate_insult(adjectives, nouns, max_words=8):
    random.shuffle(adjectives)
    selected_adjectives = adjectives[:-1]
    random.shuffle(selected_adjectives)
    
    random.shuffle(nouns)
    selected_noun = nouns[0]
    
    insult = "Thou art a"
    remaining_words = max_words - 2  # Account for "Thou art" and the noun
    
    for adjective in selected_adjectives:
        if remaining_words > 0:
            insult += " " + adjective
            remaining_words -= 1
    
    insult += " thou " + selected_noun + "!"
    
    return insult

# Generate a random insult
random_insult = generate_insult(adjectives, nouns)
print(random_insult)
