"""
Write a python function to generate and return the list of all possible sentences created from the given lists of
Subject, Verb and Object.
Note: The sentence should contain only one subject, verb and object each.

Sample Input :
subjects=["I", "You"]
verbs=["Play", "Love"]
objects=["Hockey","Football"]

Expected Output :
I Play Hockey
I Play Football
I Love Hockey
I Love Football
You Play Hockey
You Play Football
You Love Hockey
You Love Football
"""


def generate_sentences(subjects, verbs, objects):
    result = []
    for i in subjects:
        for j in verbs:
            for k in objects:
                result.append(i + " " + j + " " + k)

    return result


sub = ["I", "You"]
verb = ["love", "play"]
obj = ["Hockey", "Football"]
print(generate_sentences(sub, verb, obj))
