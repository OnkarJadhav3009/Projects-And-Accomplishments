#!/usr/bin/python
#
# Perform optical character recognition, usage:
#     python3 ./image2text.py train-image-file.png train-text.txt test-image-file.png
# 
# Authors: (insert names here)
# (based on skeleton code by D. Crandall, Oct 2020)
#
import sys
from PIL import Image, ImageDraw, ImageFont
import math

CHARACTER_WIDTH = 14
CHARACTER_HEIGHT = 25

TRAIN_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789(),.-!?\"' "


def read_data(fname):
    wordsList = []
    lettersList = []

    file = open(fname, 'r')
    for line in file:
        for word in line.split():
            if word.lower() not in ['adv', 'prt', 'adp', 'conj', 'adj', 'det', 'noun', 'num', 'pron', 'verb', 'x']:
                wordsList.append(word)
            wordsList.append(" ")
        wordsList.pop()

    for word in wordsList:
        for letter in word:
            lettersList.append(letter)

    return wordsList, lettersList


def load_letters(fname):
    im = Image.open(fname)
    px = im.load()
    (x_size, y_size) = im.size
    # print(im.size)
    # print(int(x_size / CHARACTER_WIDTH) * CHARACTER_WIDTH)
    result = []
    for x_beg in range(0, int(x_size / CHARACTER_WIDTH) * CHARACTER_WIDTH, CHARACTER_WIDTH):
        result += [["".join(['*' if px[x, y] < 1 else ' ' for x in range(x_beg, x_beg + CHARACTER_WIDTH)]) for y in
                    range(0, CHARACTER_HEIGHT)], ]
    return result


def load_training_letters(fname):
    letter_images = load_letters(fname)
    return {TRAIN_LETTERS[i]: letter_images[i] for i in range(0, len(TRAIN_LETTERS))}


def calcTransitionProbabilities(words, letters):
    initial_probabilities = {i: 0 for i in TRAIN_LETTERS}

    transition_probabilities = {
        i: {j: 0 for j in TRAIN_LETTERS} for i in TRAIN_LETTERS}

    for word in words:
        if word[0] in TRAIN_LETTERS:
            initial_probabilities[word[0]] += 1

    i = 0
    while i + 1 < len(letters):
        if letters[i] in TRAIN_LETTERS and \
                letters[i + 1] in TRAIN_LETTERS:
            transition_probabilities[letters[i]][letters[i + 1]] += 1
        i += 1

    for k, v in initial_probabilities.items():
        initial_probabilities[k] = (v + 1) / (len(words) + 2)

    rs = {}
    for k, v in transition_probabilities.items():
        rs[k] = sum(v.values())

    for k, v in transition_probabilities.items():
        for k_, v_ in v.items():
            transition_probabilities[k][k_] = (v_ + 1) / (rs[k] + 2)

    return initial_probabilities, transition_probabilities


def calcEmissionProbabilities(test_letters, train_letters):
    # Initialize the emission_probabilities dictionary as an empty dictionary.
    emission_probabilities = {l: {i: 0 for i in range(len(test_letters))} for l in train_letters}

    for l in train_letters:
        noise = 0.009
        for i in range(len(test_letters)):
            v = train_letters[l]
            c = test_letters[i]

            star = 0
            dots = 0
            for m in range(CHARACTER_HEIGHT):
                for n in range(CHARACTER_WIDTH):
                    if v[m][n] != c[m][n]:
                        dots += 1
                    else:
                        star += 1

            emission_probabilities[l][i] = (0.95 ** star) * (0.05 ** dots)

    return emission_probabilities


def sim_model(test_letters, train_letters, height, width):
    train_list = {}
    for l in range(0, len(test_letters)):
        train_list[l] = []
        for i in train_letters.keys():
            star_count = 0
            white_count = 0
            for j in range(0, height):
                for k in range(0, width):
                    if train_letters[i][j][k] == test_letters[l][j][k] == "*":
                        star_count += 1
                    elif train_letters[i][j][k] == test_letters[l][j][k] == " ":
                        white_count += 1
            similarity_score = (0.9 * star_count + 0.04 * white_count) / (height * width)
            train_list[l].append(similarity_score)
    return train_list


def viterbi(words, letters, test_letters, train_letters):
    initial_probs, transition_probs = calcTransitionProbabilities(words, letters)
    emission_probs = calcEmissionProbabilities(test_letters, train_letters)
    label_list = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789(),.-!?\"' ")
    state = []
    for tl in test_letters:
        p = []
        for l in label_list:
            if len(state) == 0:
                transition_prob = initial_probs[l]
            else:
                transition_prob = transition_probs[state[-1]][l]
            emission_prob = emission_probs[l][test_letters.index(tl)]
            s_prob = math.log(transition_prob) + math.log(emission_prob)
            p.append(s_prob)

        label = label_list[p.index(max(p))]
        state.append(label)

    string = "".join(state)

    return string


#####
# main program

if len(sys.argv) != 4:
    raise Exception("Usage: python3 ./image2text.py train-image-file.png train-text.txt test-image-file.png")

(train_img_fname, train_txt_fname, test_img_fname) = sys.argv[1:]
train_letters = load_training_letters(train_img_fname)
test_letters = load_letters(test_img_fname)
train_text = read_data(train_txt_fname)[0]
words = train_text
letters = read_data(train_txt_fname)[1]

# print(transition_probabilities)
# print(train_text)


## Below is just some sample code to show you how the functions above work. 
# You can delete this and put your own code here!

# Each training letter is now stored as a list of characters, where black
#  dots are represented by *'s and white dots are spaces. For example,
#  here's what "a" looks like:
# print("\n".join([ r for r in train_letters['a'] ]))
t = sim_model(test_letters, train_letters, 25, 14)
labels = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789(),.-!?\"' ")
string = ""
for i in t.keys():
    j = labels[t[i].index(max(t[i]))]
    string += j

print("Simple:", string)

# # Same with test letters. Here's what the third letter of the test data
# #  looks like:
# print("\n".join([ r for r in test_letters[2] ]))
hmm_String = viterbi(words, letters, test_letters, train_letters)

# The final two lines of your output should look something like this:

print("HMM:", hmm_String)
