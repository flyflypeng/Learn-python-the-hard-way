# -*- coding: utf-8 -*-
import sys

def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None

vocab = {
    'north':'direction',
    'south':'direction',
    'east':'direction',
    'west':'direction',
    'down':'direction',
    'up':'direction',
    'left':'direction',
    'right':'direction',
    'back':'direction',
    'go':'verb',
    'stop':'verb',
    'kill':'verb',
    'eat':'verb',
    'door':'noun',
    'bear':'noun',
    'princess':'noun',
    'cabinet':'noun',
    'the':'stop',
    'in':'stop',
    'of':'stop',
    'from':'stop',
    'at':'stop',
    'it':'stop',
    }

def scan(stuff):
    # space character is the default split character for the split function
    words = stuff.split()

    # sentence list stores the final result
    sentence = []

    for word in words:
        # first, we process numbers
        val = convert_number(word)
        if val != None:
            sentence.append(('number', val))
            continue

        if word in vocab:
            sentence.append((vocab[word], word))
            continue

        if not word in vocab:
            sentence.append(('error', word))
            continue

    return sentence

# try:
#     while True:
#         stuff = raw_input("> ")
#         results = scan(stuff)
#
#         print results
# except EOFError:
#     pass
