#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main()
{   
    int cnt = 0;
    while(true) {
        string s1, s2, w1, w2;
        cin >> s1 >> s2;
        if (s1 == "END" && s2 == "END") break;
        w1 = s1; w2 = s2;
        cnt++;
        sort(w1.begin(), w1.end());
        sort(w2.begin(), w2.end());
        if (w1 == w2) cout << "Case " << cnt << ": same"<< endl;
        else cout << "Case " << cnt << ": different"<<endl;
    }
}
/*
#include <iostream>
#include <string>
#include <set>
using namespace std;

int main() {
	int cnt = 0;
	while(true) {
		string s1, s2;
		multiset<char> m1, m2;
		cin >> s1 >> s2;
		cnt++;
		if (s1 == "END" && s2 == "END") break;
		else {
			if (s1.length() == s2.length()) {
				for (int i = 0; i<s1.length(); i++){
					m1.insert(s1[i]);
					m2.insert(s2[i]);
				}
				if (m1 == m2) cout <<"Case " << cnt <<": same"<<endl;
				else cout <<"Case " << cnt <<": different"<<endl;
			}
			else cout <<"Case " << cnt <<": different"<<endl;
		}
	}
	return 0;
}
*/
