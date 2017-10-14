#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <cmath>
#include <queue>
#include <set>
#include <string>


using namespace std;


int solve(string s1, string s2)
{
    vector<vector<int>> L(s1.size());
    for (int i=0; i<s1.size(); ++i)
        L[i].resize(s2.size());

    int z = 0;
    string ret;
    for(int i=0; i<s1.size(); ++i)
    {
        for (int j=0; j<s2.size(); ++j)
        {
            if (s1[i] == s2[j]) {
                if (i == 0 || j == 0) {
                    L[i][j] = 1;
                }
                else {
                    int max = -1;
                    for(int k=0; k<j; ++k)
                    {
                        int tmp = L[i][j] = L[i-1][k];
                        max = max > tmp ? max : tmp;
                    }
                    L[i][j] = max + 1;
                }
                if (L[i][j] > z) {
                    z = L[i][j];
                }
            }
            else {
                L[i][j] = 0;
            }
        }
    }
    return z;
}


int main()
{
    ios_base::sync_with_stdio(0);

    string s1, s2;
    while(cin >> s1 >> s2)
    {
        cout << solve(s1, s2) << endl;
    }
    return 0;
}
