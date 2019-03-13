#include <bits/stdc++.h>
using namespace std;

vector<string> get_tests() {}

string solve(const string &test) {}

bool check(const string& out) {}

int main() {
    for (string& test : get_tests()) {
        if (!check(solve(test))) {
            cout << test;
            return 0;
        }
    }

    return 0;
}
