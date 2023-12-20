import numpy as np
import subprocess
from scipy.stats import norm
from tqdm import tqdm

EMBEDS_PATH = 'embeds'
MST_INPUT = 'input'
MST_OUTPUT = 'output'
MST_COMMAND = './a'
OUTPUT = 'a_transfer'
SEED = 2343232
L_GLOBAL = 200

def mst_stat(data=None, random=False, n=None, dim=None):
	if random:
		assert(n is not None)
		assert(dim is not None)
		data = np.random.rand(n, dim)
	else:
		assert(data is not None)
	
	n = data.shape[0]
	dim = data.shape[1]
	header = str(n) + " " + str(dim)
	with open(MST_INPUT, "w") as f:
		f.write(header + '\n')
		for line in data:
			f.write(' '.join(map(str, line)) + '\n')
	process = subprocess.Popen(MST_COMMAND, shell=True, stdout=subprocess.PIPE)
	process.wait()
	assert(process.returncode == 0)
	with open(MST_OUTPUT, "r") as f:
		line = f.readline()
		sumdeg, n = tuple(map(int, line.split()))
	return sumdeg / n	
	
def normalize(a):
	return list(map(float, a.strip().split()))
	
def estimate_normal(dim, L, n):
	mu = 0
	sigma = 0
	stats = []
	for j in range(1, L + 1):
		stat = mst_stat(random=True, n=j, dim=dim)
		stats.append(stat)
		mu += stat
	mu /= L
	for stat in stats:
		sigma += (stat - mu) ** 2
	sigma = sigma * n / (L - 1)
	return mu, sigma
	
def read_embeds(embeds_path):
	stat = None
	n = None
	dim = None
	with open(embeds_path, "r") as f:
		lines = f.readlines()
		lines = [normalize(line) for line in lines]
		lines = np.array(lines, dtype=float)
		n = lines.shape[0]
		dim = lines.shape[1]
		assert(n > 0)
		assert(dim > 0)
		stat = mst_stat(data=lines)
	return n, dim, stat

def main(embeds_path):
	np.random.seed(SEED)
	n, dim, stat = read_embeds(embeds_path)
	F = np.arange(1, dim + 1)
	p = []
	for i in tqdm(F):
		mu, sigma = estimate_normal(i, L_GLOBAL, n)
		p.append(norm.pdf(stat, loc=mu, scale=np.sqrt(sigma / n)))
	sum_p = np.sum(np.array(p))
	ans = 0
	for i in range(len(F)):
		ans += (F[i] * p[i]) / sum_p
	with open(OUTPUT, 'w') as f:
		f.write(str(round(ans)) + '\n')

if __name__ == "__main__":
	main(EMBEDS_PATH)