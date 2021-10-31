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

        cout << "�ִܰ�� �迭 D" << endl;
    for(i = 1; i <= n; i++)
    {
        for(j = 1; j <= n; j++)
        {
            cout << i << "->" << j << " �ִܰ��: " <<  D[i][j] << endl;
        }
    }

}

int main()
{
    int i, j;
    cout << "���� ����: ";
    cin >> V;
    cout << "���� ����: ";
    cin >> E;

    cout << "���� ���� : ����1 ����2 ����ġ" << endl;
    for(i = 1; i <= E; i++)
    {
        int v1, v2, w;
        cin >> v1 >> v2 >> w;
        
        D[v1][v2] = w;
    }
    cout<<endl;

    floyd2(V);

}