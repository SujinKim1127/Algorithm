#include <iostream>
#include <vector>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
#include <queue>
using namespace std;

typedef int index;

int INF = 100000;
void dijkstra(int n, const int W[6][6],  queue<int> F)
{
    index i, vnear;
    index touch[n];
    index length[n];

    // initial
    for(i = 2; i <= n; i++)
    {
        touch[i] = 1;
        length[i] = W[1][i];
    }
    int cnt=n;
    while(cnt - 1 > 0)
    {
        int min = INF;
        for(i = 2; i <= n; i++)
        {
            // find the vertex number 
            if(0 <= length[i] < min && length[i] != -1)
            {
                min = length[i];
                vnear = i;
            }
        }

        // e = edge from vertex indexed by touch[vnear] to vertex indexed by vnear
        F.push(W[touch[vnear]][vnear]);
        cout << "F: " << F.front() << endl;
        F.pop(); 
        for(i = 2; i <= n; i++)
        {
            if(length[vnear] + W[vnear][i] < length[i])
            {
                length[i] = length[vnear] + W[vnear][i];
                touch[i] = vnear;
            }
            
        }
        length[vnear] = -1;
        
        cnt--;
    }
}

int main()
{
    int W[6][6]={
        {0, 0, 0, 0, 0, 0},
        {0, 0, 4, 1, 5, 3},
        {0, INF, 0, INF, INF, INF},
        {0, INF, 3, 0, INF, INF},
        {0, INF, 2, 6, 0, INF},
        {0, INF, INF, 2, 1, 0}
    };

    queue<int> F;
    dijkstra(5, W, F);
}