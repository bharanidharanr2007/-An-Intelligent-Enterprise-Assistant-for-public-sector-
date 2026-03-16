from better_profanity import profanity

profanity.load_censor_words()

def check_profanity(text):

    if profanity.contains_profanity(text):
        return True

    return False
