import numpy as np
f = []
for i in range(5000):
	c = np.random.rand(4)
	f.append(np.concatenate((c, c, c, c), axis=0))

data = np.array(f)
with open('embeds', "w") as f:
	for line in data:
		f.write(' '.join(map(str, line)) + '\n')