#!/usr/bin/env python3
import random
from pprint import pprint

files = [
    'resources/austen.txt',
    'resources/cyborg_manifesto.txt',
    'resources/glove.txt',
    'resources/emily.txt',
    'resources/spaaace.txt',
    'resources/fungi.txt',
    'resources/doppler.txt',
    'resources/jane.txt'
]

input_ = ''

for file in files:
    with open(file, 'r') as file:
        input_ += file.read()

# TODO: make the rest into functions

input_list = input_.replace('“', '').replace('”', '').split()

# Fill the parts dictionary with prefixes (pairs of words) mapping to lists of
# possible suffixes
parts = {}

for i in range(len(input_list) - 3):
    prefix = (input_list[i], input_list[i + 1])
    suffix = input_list[i + 2]
    if prefix in parts:
        parts[prefix].append(suffix)
    else:
        parts[prefix] = [suffix]

# Build the sentence
sentence_starts = [
    'I am',
    'He is',
    'They found',
    'So my',
    'It is',
    'Unlike the',
    'The second',
    'To think',
    'For the',
    'In this',
    'There was',
    'Meanwhile, the',
    'Such as',
    'As this',
    'But fortunately',
    'It appears',
    'As to',
    'A case',
    'The affinity',
    'In all',
    'A common',
    'The reason',
    'On that',
    'From my'
]
sentence = random.choice(sentence_starts)
prefix = tuple(sentence.split())

while True:
    suffix = random.choice(parts[prefix])
    if len(sentence) + len(suffix) + 1 >= 280:
        sentence += '.'
        break
    sentence += ' ' + suffix
    prefix = (prefix[1], suffix)

print(sentence)
