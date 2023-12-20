import matplotlib.pyplot as plt
import numpy as np

sample_sizes = [10, 100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 10000, 15000]
vec_size = 8
n = 2

#eng_fiction:
#	113922 bigrams
#eng_tales:
#	99737 bigrams
#rus_fiction:
#	79356 bigrams


eng_fiction_dimensions = [5, 8, 9, 9, 9, 9, 9, 9, 9, 10, 10]
eng_tales_dimensions = [4, 7, 9, 9, 9, 9, 10, 10, 10, 10, 10]
eng_nonfiction_dimensions = [6, 8, 9, 9, 9, 9, 9, 9, 9, 9, 10]
rus_fiction_dimensions = [4, 8, 9, 10, 10, 10, 10, 10, 10, 10, 10]
rus_nonfiction_dimensions = [6, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10]

#plt.title('Brito estimator for english texts. n= {}. vec_size = {}. L = 200'.format(n, vec_size))
#plt.xlabel('Sample size')
#plt.ylabel('Topological dimension')
#plt.plot(sample_sizes, eng_tales_dimensions, color='blue', label='English fairy tales')
#plt.plot(sample_sizes, eng_fiction_dimensions, color='red', label='English fiction')
#plt.plot(sample_sizes, eng_nonfiction_dimensions, color='green', label='English non-fiction')
#plt.grid(axis='x', color='0.95')
#plt.grid(axis='y', color='0.95')
#plt.legend()
#plt.show()

#plt.title('Brito estimator for russian texts. n= {}. vec_size = {}. L = 200'.format(n, vec_size))
#plt.xlabel('Sample size')
#plt.ylabel('Topological dimension')
#plt.plot(sample_sizes, rus_fiction_dimensions, color='blue', label='Russian fiction')
#plt.plot(sample_sizes, rus_nonfiction_dimensions, color='red', label='Russian non-fiction')
#plt.grid(axis='x', color='0.95')
#plt.grid(axis='y', color='0.95')
#plt.legend()
#plt.show()

#plt.title('Brito estimator for russian texts. n= {}. vec_size = {}. L = 200'.format(n, vec_size))
#plt.xlabel('Sample size')
#plt.ylabel('Topological dimension')
#plt.plot(sample_sizes, rus_fiction_dimensions, color='blue', label='Russian fiction')
#plt.plot(sample_sizes, rus_nonfiction_dimensions, color='red', label='Russian non-fiction')
#plt.grid(axis='x', color='0.95')
#plt.grid(axis='y', color='0.95')
#plt.legend()
#plt.show()

rus_dimensions = [4, 8, 9, 10, 10, 10, 10, 10, 10, 10, 10]
eng_dimensions = [4, 8, 9, 9, 9, 9, 9, 9, 9, 10, 10]
fiction_dimensions = [5, 8, 9, 9, 9, 9, 9, 9, 9, 9, 10]
nonfiction_dimensions = [5, 8, 9, 9, 9, 10, 10, 10, 10, 10, 10]

#plt.title('Brito estimator for russian language vs english language. n= {}. vec_size = {}. L = 200'.format(n, vec_size))
#plt.xlabel('Sample size')
#plt.ylabel('Topological dimension')
#plt.plot(sample_sizes, rus_dimensions, color='blue', label='Russian')
#plt.plot(sample_sizes, eng_dimensions, color='red', label='English')
#plt.grid(axis='x', color='0.95')
#plt.grid(axis='y', color='0.95')
#plt.legend()
#plt.show()

plt.title('Brito estimator for fiction vs nonfiction. n= {}. vec_size = {}. L = 200'.format(n, vec_size))
plt.xlabel('Sample size')
plt.ylabel('Topological dimension')
plt.plot(sample_sizes, fiction_dimensions, color='blue', label='Fiction')
plt.plot(sample_sizes, nonfiction_dimensions, color='red', label='Nonfiction')
plt.grid(axis='x', color='0.95')
plt.grid(axis='y', color='0.95')
plt.legend()
plt.show()

#x = [30, 110, 240, 420, 650, 930, 1260, 1640, 2070, 2550, 3080, 3660, 4290, 4970, 5700, 6480, 7310, 8190, 9120, 10100]
#y = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
#plt.title('Brito estimator for 2D mobius strip in 3D')
#plt.xlabel('Sample size')
#plt.ylabel('Topological dimension')
#plt.plot(x, y, label='L = 200')
#plt.plot(x, y, label='L = 500')
#plt.grid(axis='x', color='0.95')
#plt.grid(axis='y', color='0.95')
#plt.legend()
#plt.show()

#x = [10, 50, 100, 1000, 5000, 10000, 15000]
#y = [4, 7, 7, 7, 7, 7, 7]
#y_1 = [2, 6, 6, 7, 7, 7, 7]
#plt.title('Brito estimator for 5D manifold in 12D')
#plt.xlabel('Sample size')
#plt.ylabel('Topological dimension')
#plt.plot(x, y, label='L = 200')
#plt.plot(x, y_1, label='L = 500')
#plt.grid(axis='x', color='0.95')
#plt.grid(axis='y', color='0.95')
#plt.legend()
#plt.show()
