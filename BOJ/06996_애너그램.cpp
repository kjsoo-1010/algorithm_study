#include <iostream>
#include <string>
#include <set>
using namespace std;

int main() {
	int n;
	cin >> n;
	for (int i = 0; i<n; i++) {
		string s1, s2;
		cin >> s1 >> s2;
		multiset<char> m1, m2;
		if (s1.length() == s2.length()) {
			for (int i = 0; i<s1.length(); i++){
				m1.insert(s1[i]);
				m2.insert(s2[i]);
			}
			if (m1 == m2) cout << s1 << " & " << s2 << " are anagrams."<< endl;
            else cout << s1 << " & " << s2 << " are NOT anagrams."<< endl;
		}
		else cout << s1 << " & " << s2 << " are NOT anagrams."<< endl;
	}
	return 0;
}
