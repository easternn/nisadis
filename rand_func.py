import numpy as np
import matplotlib.pyplot as plt
import matplotlib.tri as mtri
import subprocess

sample_sizes = [10, 50, 100, 1000, 5000, 10000, 15000]

for n in sample_sizes:
	data = []
	for j in range(n):
		a = np.random.rand(5)
		x_1 = a[0] * a[1]
		x_2 = a[1] * a[2]
		x_3 = a[2] * a[3]
		x_4 = a[3] * a[4]
		
		x_5 = a[0] + a[1]
		x_6 = a[1] + a[2]
		x_7 = a[2] + a[3]
		x_8 = a[3] + a[4]
		
		x_9 = a[0] * np.cos(a[1])
		x_10 = a[1] * np.cos(a[2])
		x_11 = a[2] * np.cos(a[3])
		x_12 = a[3] * np.cos(a[4])
		data.append([x_1, x_2, x_3, x_4, x_5, x_6, x_7, x_8, x_9, x_10, x_11, x_12])
	data = np.array(data)
	with open('embeds', "w") as f:
		for line in data:
			f.write(' '.join(map(str, line)) + '\n')
	process = subprocess.Popen('python3 a.py', shell=True, stdout=subprocess.PIPE)
	process.wait()
	answer = None
	with open('a_transfer', 'r') as f:
		answer = int(f.readline())
	print(n, answer)
	
	