#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <cmath>
#include <queue>
#include <set>
#include <string>


using namespace std;


string solve(int n, vector<int>& mm)
{
    int sum = 0;
    if (mm.size() == 1 && mm[0] == 1) return "Brother";
    for (int i=0; i<mm.size(); ++i)
    {
        // cout << "mm[" << i << "] = " << mm[i] << endl;
        if (mm[i] == 1) sum += 1;
        else if (mm[i] == 2) sum += 2;
        else sum += 3;  
    }
    // cout << "sum is " << sum << endl;
    if ( sum & 1 ) return "John";
    else return "Brother";
}


int main()
{
    ios_base::sync_with_stdio(0);

    int T;
    cin >> T;
    for(int t=1; t<=T; ++t)
    {
        int n;
        cin >> n;
        vector<int> mm(n);
        for(int i=0; i<n; ++i) {
            cin >> mm[i];
        }
        cout << solve(n, mm) << endl;
    }
    return 0;
}
