"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    return 'un' + word

def make_word_groups(vocab_words):
    return (' :: ' + vocab_words[0]).join(vocab_words)


def remove_suffix_ness(word):
    if 'iness' in word:
        test = word.split('i')
        return test[0] + 'y'
        
    if 'iness' not in word:
        test = word.split('n')
        return test[0]

        

def adjective_to_verb(sentence, index):
    sntnc = sentence[:-1]
    word = sntnc.split()
    return word[index]+'en'



# to print out the return value.

add_prefix = add_prefix_un('happy')
make_group = make_word_groups('auto')
remove_suffix = remove_suffix_ness('heaviness')
make_verb = adjective_to_verb('Look at the bright sky.', -2)


# Output
print('| Add the prefix un to a word:', add_prefix, 
      '| add prefixes to word group:', make_group, 
      '| Remove a suffix from a word:', remove_suffix, 
      '| Extract and transform a word:', make_verb, )

