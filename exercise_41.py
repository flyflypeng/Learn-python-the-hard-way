import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
        "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)":
        "class %%% has-a __init__ that takes self and *** parameters.",
    "class %%%(object):\n\tdef ***(self, @@@)":
        "class %%% has-a function named *** that takes self and @@@ parameters.",
    "*** = %%%()":
        "Set *** to an instance of class %%%.",
    "***.***(@@@)":
        "From *** get the *** function, and call it with parameters self, @@@.",
    "***.***":
        "From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# load up the words from the website
for word in urlopen(WORD_URL):
    WORDS.append(word.strip())


def convert(snippet, phrase):
    # select the class names from WORDS
    class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count("%%%"))]
    # select the other names from WORDS
    other_names = random.sample(WORDS, snippet.count("***"))

    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        # randomly produce the total number of parameters
        param_count = random.randint(1, 3)
        # concatenation the parameters into a String and append it into list
        param_names.append(', '.join(random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        # copy sentence into result
        result = sentence[:]

        # fake class names:
        for word in class_names:
            result = result.replace("%%%", word, 1)

        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results


# keep going until they hit CTRL-D
try:
    while True:
        # get the all keys in the dict of PHRASES
        snippets = PHRASES.keys()
        # shuffle the snippets randomly
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                # give the comment first and then give the answer
                question, answer = answer, question

            print question

            raw_input("> ")
            print "ANSWER: %s\n\n" % answer
# if you press CTRL-D, python will raise the EOFError, the we end of the this program
except EOFError:
    print "\nBye"
