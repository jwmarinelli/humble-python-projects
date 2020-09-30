# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

# INSTRUCTIONS: Write a function that can censor a specific word or phrase from a body of text, and then return the text.
# COMPLETED
def censor_this(text, string):
    censored_text = text.replace(string, '#' * len(word))
    return censored_text
print(censor_this(email_one, 'learning algorithms'))

# INSTRUCTIONS: Write a function that can censor not just a specific word or phrase from a body of text, but a whole list of words and phrases, and then return the text.
# COMPLETED

proprietary_terms = ['she', 'personality matrix', 'sense of self', 'self-preservation', 'learning algorithm', 'her', 'herself']

def censor_list(text, lst):
    censored_text = text
    for word in lst:
        uppercase_word = word.capitalize()
        if word in text:
            temp = censored_text.replace(word, "#" * len(word))
            censored_text = temp
        if uppercase_word in text:
            temp = censored_text.replace(uppercase_word, "#" * len(uppercase_word))
            censored_text = temp
    return censored_text

print(censor_list(email_two, proprietary_terms))



#INSTRUCTIONS: Write a function that can censor any occurance of a word from the “negative words” list after any “negative” word has occurred twice, as well as censoring everything from the list from the previous step as well and use it to censor email_three.
#IN PROGRESS
negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]
