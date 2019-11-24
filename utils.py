import numpy as np
import matplotlib.pyplot as plt
from Formal_Gramar_Word_Generator import grammar_word_generator as wg
import itertools
import os

def genImages(words, orientation="L", name="test", alphabet_words=None):
	if not os.path.exists("out/"+name):
	    os.makedirs("out/"+name)
	if alphabet_words is None:
		alphabets = list(itertools.combinations(words, 2))
	else:
		alphabets = list(itertools.combinations(alphabet_words, 2))

	images = []
	k = 0
	for word in words:
		for alphabet in alphabets:
			out = []
			for letter in word:
				if orientation == "L":
					out.append(alphabet[int(letter)])
				else:
					out.append(alphabet[int(abs(int(letter)-1))])


			out = toImage(out)
			images.append(out)
			plotImage(out, name="out/"+name+"/"+str(k)+".png")

			k += 1
	return images

def toImage(I):
	matrix = np.zeros((len(I), len(I[0])))

	for i in range(len(I)):
		for j in range(len(I[i])):
			matrix[i][j] = int(I[i][j])

	return matrix

def plotImage(out, name="out/test.png", block=False):
	fig, ax = plt.subplots()
	img = ax.imshow(out, interpolation='nearest')
	img.set_cmap('hot')
	ax.set_yticks([])
	ax.set_xticks([])
	margin = 0
	#ax.set_xlim(-margin, len(out) + margin)
	#ax.set_ylim(-margin, len(out[0]) + margin)
	ax.set_frame_on(True)
	plt.savefig(name, bbox_inches='tight')
	plt.show(block=block)
