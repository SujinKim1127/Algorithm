#include <iostream>
#include <memory.h>
#include <string.h>
using namespace std;

int V, E;
int W[11][11];
int D[11][11];
int P[11][11];

void floyd2(int n)
{
    int i, j, k;
    for (i = 1; i <= n; i++)
    {
        for(j = 1; j <= n; j++)
            P[i][j] = 0;
    }
    // memcpy(D, W, sizeof(W));    //D = W;
    for(k = 1; k <= n; k++)
    {
        for(i = 1; i <= n; i++)
        {
            for(j = 1; j <= n; j++)
            {
                if(D[i][k] + D[k][j] < D[i][j] && (D[i][k] != 0 || D[k][j] != 0))
                {
                    cout << i << "," << k << " + " << k << ","<< j << " < " << i <<","<< j  << endl;
                    P[i][j] = k;
                    D[i][j] = D[i][k] + D[k][j];
                    cout<<D[i][j]<<endl;
                }
            }
        }
    }

        cout << "최단경로 배열 D" << endl;
    for(i = 1; i <= n; i++)
    {
        for(j = 1; j <= n; j++)
        {
            cout << i << "->" << j << " 최단경로: " <<  D[i][j] << endl;
        }
    }

}

int main()
{
    int i, j;
    cout << "정점 개수: ";
    cin >> V;
    cout << "간선 개수: ";
    cin >> E;

    cout << "정점 연결 : 정점1 정점2 가중치" << endl;
    for(i = 1; i <= E; i++)
    {
        int v1, v2, w;
        cin >> v1 >> v2 >> w;
        
        D[v1][v2] = w;
    }
    cout<<endl;

    floyd2(V);

}