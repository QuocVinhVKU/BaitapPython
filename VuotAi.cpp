// #include <iostream>
// #include <math.h>
// #include <algorithm>
// #include <map>

// using namespace std;
// long a[100001];
// int main() {
// 	ios_base::sync_with_stdio(0);
// 	int n;
// 	long k, result, mmax = 0, ssum = 0;
// 	cin >> n >> k;
// 	for (int i = 0; i<n; i++){
// 		cin >> a[i];
// 		mmax = max(mmax, a[i]);
// 		ssum += a[i];
// 	}
// 	if (mmax > k) mmax = k;
// 	cout << ssum - mmax + 1;
// }