import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

word_list = words.split()

start_words = []


def get_afters(word_list):
    afters = {}

    for i in range(len(word_list)):
        if i == len(word_list) - 1:
            break

        if word_list[i][0].isupper() or (word_list[i][0] == '"' and word_list[i][1].isupper()):
            start_words.append(word_list[i])
            
        if afters.get(word_list[i]) is None:
            afters[word_list[i]] = [word_list[i + 1]]
        else:
            afters[word_list[i]].append(word_list[i + 1])
    
    return afters


def construct_sentence(afters, start_words):
    current = random.choice(start_words)

    while current[-1] not in ('.', '?', '!'):
        if current[-1] == '"' and current[-2] in ('.', '?', '!'):
            break
        print(current, end=" ")
        current = random.choice(afters[current])
    print(current)


# TODO: construct 5 random sentences
# Your code here

construct_sentence(get_afters(word_list), start_words)
print('')
construct_sentence(get_afters(word_list), start_words)
print('')
construct_sentence(get_afters(word_list), start_words)
print('')
construct_sentence(get_afters(word_list), start_words)
print('')
construct_sentence(get_afters(word_list), start_words)

