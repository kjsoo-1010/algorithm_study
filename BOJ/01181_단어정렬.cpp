#include <iostream>
#include <algorithm>
#include <string>
#include <set>
#include <vector>

using namespace std;

int main() {
    set<pair<int, string>> s;
    int n;
    string word;
    cin >> n;
    for (int i = 0; i<n; i++) {
        cin >> word;
        s.insert(pair<int, string>(word.length(), word));
    }
    vector<pair<int, string>> v(s.begin(), s.end());
    for(int i = 0; i<s.size(); i++) {
        cout << v[i].second << endl;
    }
}
