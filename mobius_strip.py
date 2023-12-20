import numpy as np
import matplotlib.pyplot as plt
import matplotlib.tri as mtri
import subprocess
Ns = np.linspace(5, 100, 20)
Ms = np.linspace(5, 100, 20) + 1
t = []
t1 = []
for i in range(20):
	N, M = int(Ns[i]), int(Ms[i])
#	print(N, M, N * M)
	t.append(N * M)
	t1.append(2)
	continue
	a = np.linspace(0, 2.0 * np.pi,N)
	b = np.linspace(-0.5, 0.5, M)
	a, b = np.meshgrid(a, b)
	a, b = a.flatten(), b.flatten()
	# This is the Mobius mapping, taking a, b pair and returning an x, y, z
	x = (1 + 0.5 * b * np.cos(a / 2.0)) * np.cos(a)
	y = (1 + 0.5 * b * np.cos(a / 2.0)) * np.sin(a)
	z = 0.5 * b * np.sin(a / 2.0)
	data = []
	for i in range(N * M):
		data.append([x[i], y[i], z[i]])
	data = np.array(data)
	with open('embeds', "w") as f:
		for line in data:
			f.write(' '.join(map(str, line)) + '\n')
	process = subprocess.Popen('python3 a.py', shell=True, stdout=subprocess.PIPE)
	process.wait()
	answer = None
	with open('a_transfer', 'r') as f:
		answer = int(f.readline())
	print(N, M, N * M, answer)
print(t)
print(t1)
	
	