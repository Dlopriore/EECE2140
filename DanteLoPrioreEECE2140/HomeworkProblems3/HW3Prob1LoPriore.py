# Dante LoPriore
# March 17, 2023
# PS3: Problem 1

# Purpose: to produce a function that translates words from the english language 
# to pig latin using the given algorithms to form those phrases.

# allows user to input a phrase to translate into pig latin
english_phrase = input("Please enter a phrase to translate into pig latin: ")
#english_phrase = 'the ape jump'

# String -> String
# to produce the pig latin translation of the given english word using the grammatical standards 
# seen in pig latin to help form the final encoded word.
def pig_latin_translation(given_english_phrase):

    #initalize the variable used to store the pig latin words and phrases 
    full_translated_pig_latin_word = ""
    full_translated_pig_latin_phrase = ""

    # to split up each word into a list by using the spacing as it will tokenize the phrase into words
    given_english_phrase = given_english_phrase.lower()
    individual_english_words_t = given_english_phrase.split(' ')

    # to remove additional spaces in the phrase
    individual_english_words = [mem for mem in individual_english_words_t if mem]

    # iterates through each character in the word to form the true pig latin translation for that specific word
    for given_english_word in individual_english_words:

        # to determine whether the first character of the word has a vowel and the given word is greater than or equal to 2 letters 
        # since their are seperate rules to follow if that case is true 
        if not (given_english_word[0] in ('a', 'e', 'o', 'u', 'i'))  and (len(given_english_word) >= 2):
            # produces the pig latin translation of the word does not start with a vowel

            # translation includes adding the first letter to the end of the word and adding “ay” at the end of the word
            split_first_english_term = given_english_word[1:] + given_english_word[0]
            full_translated_pig_latin_word = split_first_english_term + 'ay'
        else:
            # produces the pig latin translation of the word does start with a vowel

            # to determine whether the given word is greater than or equal to 2 letters 
            if(len(given_english_word) >= 2):
                # translation includes adding “ay” at the end of the word
                full_translated_pig_latin_word = given_english_word + "ay"
            else:
                full_translated_pig_latin_word = given_english_word

        # concates the translated pig latin words together 
        # to form the fully translated pig latin sentences
        full_translated_pig_latin_phrase += full_translated_pig_latin_word + " "
    
    # outputs the final translated pig latin phrase
    return full_translated_pig_latin_phrase

# prints the full pig latin translation 
final_result = "The pig latin translation your inputed english word is: " + pig_latin_translation(english_phrase)
print(final_result)

