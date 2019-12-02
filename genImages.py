from Formal_Gramar_Word_Generator import grammar_word_generator as wg
import itertools
import numpy as np
import matplotlib.pyplot as plt
import os

from utils import *

name = "anbn"
size = (10, 10)

#rules = [wg.Rule("S -> 0'B'|1'A'"), wg.Rule("A -> 0|0'S'|1'A''A'"), wg.Rule("B -> 1|1'S'|0'B''B'")]
#rules = [wg.Rule("S -> 'A''B'"), wg.Rule("A -> 1|1'A'"), wg.Rule("B -> 0|0'B'")]
rules = [wg.Rule("S -> 'A'"), wg.Rule("A -> 01|01'A'")]

g = wg.WordGenerator(rules)
words = g.generate_words(size[0])
words.sort(reverse=True)

alphabet_words = g.generate_words(size[1])
alphabet_words.sort(reverse=True)
if len(alphabet_words) == 1:
	alphabet_words = [alphabet_words[0], alphabet_words[0]]


genImages(words, alphabet_words=alphabet_words, orientation="R", name=name+str(size))