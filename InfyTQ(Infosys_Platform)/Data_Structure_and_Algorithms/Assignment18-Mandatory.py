"""
Mary is a kindergarten teacher. She has given a task to the children after teaching them a list of words.
The task is to find the unknown words (other than the words they already know) from the given text.
Write a python function which accepts the text and the known list of words and returns the set of unknown words found.

Return -1 if there are no unknown words.

Estimated Time: 20 minutes

Sample Input	                                            Expected Output
Text: "the sun rises in the east"
Vocabulary: ["sun","in","east","doctor","day"]	            {'rises', 'the'}
"""


def find_unknown_words(texts, vocab):
    texts = texts.lower().split(' ')
    res = set(texts).difference(set(vocab))
    return res if len(res) != 0 else -1


text = "The sun rises in the east and sets in the west."
vocabulary = ["sun", "in", "rises", "the", "east"]
unknown_words = find_unknown_words(text, vocabulary)
print("The unknown words in the file are:", unknown_words)
