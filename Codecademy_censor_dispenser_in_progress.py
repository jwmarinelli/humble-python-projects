 # These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

def censor_this(text, string):
    censored_text = text.replace(string, '#' * len(word))
    return censored_text
print(censor_this(email_one, 'learning algorithms'))

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

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]
