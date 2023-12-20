#include <stdio.h>
#include <vector>
#include <math.h>

int n, dim;
const double INF = 1e9;
std::vector<std::vector<double> > points;
std::vector<bool> used;
std::vector<double> min_e;
std::vector<int> sel_e;
std::vector<int> deg;

double dist(int i, int j) {
	double sum = 0;
	for (int k = 0; k < dim; ++k) {
		sum += (points[i][k] - points[j][k]) * (points[i][k] - points[j][k]);
	}
	return std::sqrt(sum);
}

void read_data() {
	scanf("%d %d", &n, &dim);
	used.assign(n, false);
	min_e.assign(n, INF);
	sel_e.assign(n, -1);
	points.resize(n);
	deg.assign(n, 0);
	for (int i = 0; i < n; ++i) {
		points[i].resize(dim);
		for (int j = 0; j < dim; ++j) {
			double x;
			scanf("%lf", &x);
			points[i][j] = x;
		}
	}
}

int main() {
	freopen("input", "r", stdin);
	freopen("output", "w", stdout);
	read_data();
	min_e[0] = 0;
	for (int i = 0; i < n; ++i) {
		int v = -1;
		for (int j = 0; j < n; ++j) {
			if (!used[j] && (v == -1 || min_e[j] < min_e[v]))
				v = j;
		}
		if (min_e[v] == INF) {
			exit(1);
		}
		used[v] = true;
		if (sel_e[v] != -1) {
    		++deg[v];
    		++deg[sel_e[v]];
		}
		for (int to = 0; to < n; ++to) {
			double d = dist(v, to);
			if (d < min_e[to]) {
				min_e[to] = d;
				sel_e[to] = v;
			}
		}
	}
	long long sum = 0;
	for (int i = 0; i < n; ++i) {
		sum += (long long)deg[i] * (long long)deg[i];
	}
	printf("%lld %d\n", sum, n);
	return 0;
}