title = "my hobbies"
sentence = "I like to hike, bake, and read."

old_word = "hike"
new_word = "ride"

def capitalize_title(title):

    return title.title()
    
def check_sentence_ending(sentence):


    return sentence.endswith('.')


def clean_up_spacing(sentence):


    return sentence.strip(' ')


def replace_word_choice(sentence, old_word, new_word):

    return sentence.replace(old_word, new_word)


# to print out the return value.

capital = capitalize_title(title)
ending = check_sentence_ending(sentence)
spacing = clean_up_spacing(sentence)
replace = replace_word_choice(sentence, old_word, new_word)


# Output
print('|capitalised sentence:', capital, 
      '| does sentence have ending?:', ending, 
      '| clean up spacing:', spacing, 
      '| replace with word of choice:', replace, )