#!/usr/bin/env python3
import random
import twitter
import config

files = [
    'resources/austen.txt',
    'resources/cyborg_manifesto.txt',
    'resources/glove.txt',
    'resources/emily.txt',
    'resources/spaaace.txt',
    'resources/fungi.txt',
    'resources/doppler.txt',
    'resources/jane.txt',
    'resources/logic.txt',
    'resources/differential_equations.txt',
    'resources/ethereum.txt',
    'resources/georgette.txt'
]

api = twitter.Api(consumer_key=config.consumer_key,
                  consumer_secret=config.consumer_secret,
                  access_token_key=config.access_token_key,
                  access_token_secret=config.access_token_secret)

def get_files_content():
    text = ''
    for file in files:
        with open(file, 'r') as file:
            text += file.read()
    return text

def build_word_chain(text):
    text_list = text.split()
    word_chain = {}

    for i in range(len(text_list) - 3):
        prefix = (text_list[i], text_list[i + 1])
        suffix = text_list[i + 2]
        if prefix in word_chain:
            word_chain[prefix].append(suffix)
        else:
            word_chain[prefix] = [suffix]
    return word_chain

def markov(word_chain):
    prefixes = [
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
        'From my',
        'It has',
        'The only',
        'But since',
        'A higher',
        'For most',
        'So was',
        'Up the',
        'The two',
        'This question',
        'The form',
        'And as',
        'From this',
        'Nothing therefore'
    ]
    sentence = random.choice(prefixes)
    prefix = tuple(sentence.split())

    while True:
        suffix = random.choice(word_chain[prefix])
        if len(sentence) + len(suffix) + 1 >= 280:
            sentence += '.'
            break
        sentence += ' ' + suffix
        prefix = (prefix[1], suffix)

    return sentence

def main():
    file_content = get_files_content()
    word_chain = build_word_chain(file_content)
    tweet = markov(word_chain)
    status = api.PostUpdate(tweet)
    print(status)

if __name__ == "__main__":
    main()