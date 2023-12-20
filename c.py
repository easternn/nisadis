import nltk
from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize
import string
from nltk import bigrams
import numpy as np
import os
import subprocess
from tqdm import tqdm

VEC_SIZE = 8
INPUT = 'a_transfer'
__path = os.path.dirname(__file__)

def normalize_text(text):
	sentences = text.replace('!', '.').replace('?', '.').split('.')
	tokens = [[word.lower() for word in word_tokenize(sentence) if word.isalpha()] for sentence in sentences]
	return tokens
	
def count_words(tokens):
	ans = 0
	for sentence in tokens:
		ans += len(sentence)
	return ans

def train_model(text, path, is_new=False, vec_size=VEC_SIZE):
	tokens = normalize_text(text)
	total_words = count_words(tokens)
	if is_new:
		model = Word2Vec(tokens, vector_size=vec_size, window=5, min_count=1, workers=4)
		model.save(path)
	else:
		model = Word2Vec.load(path)
		model.train(tokens, total_examples=len(tokens), epochs=1)
	return total_words

def get_bigrams(text, path):
	tokens = normalize_text(text)
	bigram_tokens = [list(bigrams(sentence)) for sentence in tokens]
	bigram_vectors = {}
	model = Word2Vec.load(path)
	for sentence in bigram_tokens:
		for word1, word2 in sentence:
			if word1 in model.wv.key_to_index and word2 in model.wv.key_to_index:
				vector1 = model.wv[word1]
				vector2 = model.wv[word2]
				bigram_vector = np.concatenate((vector1, vector2))
				bigram_vectors[f"{word1} {word2}"] = bigram_vector
	return bigram_vectors


def create_and_train(path, files, vec_size=VEC_SIZE):
	print('*** Start training new model {}'.format(path))
	created = False
	total_words = 0
	for p in tqdm(files):
		abs_file_path = os.path.join(__path, p)
		with open(abs_file_path, 'r') as f:
			data = f.read()
			if created:
				total_words += train_model(data, path, is_new=False, vec_size=vec_size)
			else:
				total_words += train_model(data, path, is_new=True)
			created = True
	model = Word2Vec.load(path)
	vocab_len = len(model.wv)
	print('*** Model {} is trained! Total words: {} Vocabulary size: {}'.format(path, total_words, vocab_len))
	

def get_bigrams_global(path, files, n):
	bigram_vectors = {}
	for p in files:
		abs_file_path = os.path.join(__path, p)
		with open(abs_file_path, 'r') as f:
			data = f.read()
			new_bigram_vec = get_bigrams(data, path)
			bigram_vectors.update(new_bigram_vec)
	arr = np.array(list(bigram_vectors.values()))
	print(arr.shape)
	idx = np.random.randint(arr.shape[0], size=n)
	return arr[idx, :]

def get_path_to_files(folder):
	mypath = os.path.join(__path, folder)
	filenames = next(os.walk(mypath), (None, None, []))[2]
	ans = []
	for filename in filenames:
		if filename[0] == '.':
			continue
		ans.append(os.path.join(folder, filename))
	return ans

def dump_data(data):
	with open('embeds', "w") as f:
		for line in data:
			f.write(' '.join(map(str, line)) + '\n')

def calc_dimensions(models, model_paths, sample_sizes):
	dimensions = {}
	for model in tqdm(models):
		dimensions[model] = []
		paths = get_path_to_files(model_paths[model])
		for sample_size in tqdm(sample_sizes):
			sample = get_bigrams_global(model, paths, sample_size)
			dump_data(sample)
			process = subprocess.Popen('python3 a.py', shell=True, stdout=subprocess.PIPE)
			process.wait()
			answer = None
			with open(INPUT, 'r') as f:
				answer = int(f.readline())
			print("Model: {}; Sample size: {} TDE: {}".format(model, sample_size, answer))	
			dimensions[model].append(answer)
	return dimensions

def plot_results():
	pass
		
def main():
#	eng_fiction_paths = get_path_to_files('eng_fiction')
#	create_and_train('model_eng_fiction', eng_fiction_paths)
#	
#	eng_tales_paths = get_path_to_files('eng_tales')
#	create_and_train('model_eng_tales', eng_tales_paths)
#
#	rus_fiction_paths = get_path_to_files('rus_fiction')
#	create_and_train('model_rus_fiction', rus_fiction_paths)
#
#	eng_nonfiction_paths = get_path_to_files('eng_nonfiction')
#	create_and_train('model_eng_nonfiction', eng_nonfiction_paths)
#	
#	rus_nonfiction_paths = get_path_to_files('rus_nonfiction')
#	create_and_train('model_rus_nonfiction', rus_nonfiction_paths)
#
#	eng_paths = get_path_to_files('eng')
#	create_and_train('model_eng', eng_paths)
#	
#	rus_paths = get_path_to_files('rus')
#	create_and_train('model_rus', rus_paths)
#
#	fiction_paths = get_path_to_files('fiction')
#	create_and_train('model_fiction', fiction_paths)
#
#	nonfiction_paths = get_path_to_files('nonfiction')
#	create_and_train('model_nonfiction', nonfiction_paths)

	models = ['model_eng_tales', 'model_rus_fiction']
	model_paths = {
		"model_eng_fiction": "eng_fiction",
		"model_eng_tales": "eng_tales",
		"model_rus_fiction": "rus_fiction",
		"model_eng_nonfiction": "eng_nonfiction",
		"model_rus_nonfiction": "rus_nonfiction",
		"model_rus": "rus",
		"model_eng": "eng",
		"model_nonfiction": "nonfiction",
		"model_fiction": "fiction"
	}
	sample_sizes = [10, 100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 10000, 15000]
	dimensions = calc_dimensions(['model_rus', 'model_eng', 'model_fiction', 'model_nonfiction'], model_paths, sample_sizes)
	print(dimensions)

main()

