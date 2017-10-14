#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <cmath>
#include <queue>
#include <set>



using namespace std;



long long int solve(int n, vector<vector<int>>& values)
{
    long long int r = 0;

    return r; 
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
        vector<vector<int>> values(n);
        for(int i=0; i<n; ++i)
            values[i].resize(n);

        for(int i=0; i<n; ++i)
        {
            for(int j=0; j<n; ++j)
            {
                cin >> values[i][j];
            }
        }
       
        cout << "Case " << t << ": " << solve(n, values) << endl;
    }
    return 0;
}
