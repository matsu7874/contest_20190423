#include <iostream>
using namespace std;
int main() {
  int n;
  long k;
  unsigned long a[500101] = {};
  unsigned long mod = 1000000007;
  cin >> n >> k;
  if (k == 0) {
    cout << "0" << endl;
    return 0;
  }
  a[1] = 1;
  for (long i = 1; i < k; i++) {
    for (int j = 1; j <= n; j++) {
      a[i + j] += a[i];
      a[i + j] %= mod;
    }
  }
  cout << a[k] % mod << endl;
  return 0;
}