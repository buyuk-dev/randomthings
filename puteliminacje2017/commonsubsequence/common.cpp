#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <cmath>
#include <queue>
#include <set>
#include <string>


using namespace std;


function LCSubstr(S[1..r], T[1..n])
    L := array(1..r, 1..n)
    z := 0
    ret := {}
    for i := 1..r
        for j := 1..n
            if S[i] == T[j]
                if i == 1 or j == 1
                    L[i,j] := 1
                else
                    L[i,j] := L[i-1,j-1] + 1
                if L[i,j] > z
                    z := L[i,j]
                    ret := {S[i-z+1..i]}
                else
                if L[i,j] == z
                    ret := ret ∪ {S[i-z+1..i]}
            else
                L[i,j] := 0
    return ret


int solve(string s1, string s2)
{
    L = vector<vector<int>>(s1.size());
    for (int i=0; i<
}


int main()
{
    ios_base::sync_with_stdio(0);
    
    int T;
    cin >> T;
    for(int t=1; t<=T; ++t)
    {
        string s1, s2;
        cin >> s1 >> s2;    
        cout << solve(n, mm) << endl;
        break;
    }
    return 0;
}
