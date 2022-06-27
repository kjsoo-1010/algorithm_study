#include <iostream>
#include <set>
using namespace std;

int main() {
	// your code goes here
	int n, temp;
	set<int> s;
	cin >> n;
	for (int i = 0; i<n; i++) {
		cin >> temp;
		s.insert(temp);
		//cout << i << " ";
	}
	set<int>::iterator iter;
	for (iter = s.begin(); iter!= s.end(); iter++) cout << *iter << " ";
	return 0;
}
