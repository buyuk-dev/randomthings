#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <cmath>
#include <queue>
#include <set>



using namespace std;




struct result
{
    result(int barn, int length, int num): barn(barn), length(length), numOfBarns(num) {}
    int barn, length, numOfBarns;
};


result solve(int n, int m, vector<vector<int>>& g)
{
    vector<int> dist(n + 1, -1);
    vector<bool> visited(n + 1, false); 
    visited[1] = true;
    dist[1] = 0;

    queue<int> q;
    q.push(1);

    int maxdist = -1;
    while(!q.empty())
    {
        int v = q.front();
        for(int i=0; i<g[v].size(); ++i)
        {
            int neighbour = g[v][i];
            if (!visited[neighbour])
            {
                visited[neighbour] = true;
                q.push(neighbour);
                dist[neighbour] = dist[v] + 1;
                if (dist[neighbour] > maxdist) {
                    maxdist = dist[neighbour];
                }
            }
        }
        q.pop();
    }

    vector<int> bs;
    for (int i=1; i<dist.size(); ++i)
    {
        if (dist[i] == maxdist)
            bs.push_back(i);   
    }

    sort(bs.begin(), bs.end());
    
    result r(bs[0], maxdist, bs.size());
    return r; 
}


int main()
{
    ios_base::sync_with_stdio(0);

    int n, m, a, b;
    cin >> n >> m;    
    vector<vector<int>> g(n+1);

    for (int i=0; i<m; ++i)
    {
        cin >> a >> b;
        g[a].push_back(b);
        g[b].push_back(a);
    }

    result res = solve(n, m, g);    
    cout << res.barn << " " << res.length << " " << res.numOfBarns << endl;

    return 0;
}
