#include <iostream>
#include <vector>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
#include <queue>
using namespace std;

typedef int index;
typedef index set_pointer;

struct nodetype {
	int depth;
    index parent;
};

typedef nodetype universe[10];

universe U;


class Edge
{
public:
    int node[2];
    int weight;
    Edge(int a, int b, int weight)
    {
        this->node[0] = a;
        this->node[1] = b;
        this->weight = weight;
    }
    bool operator<(Edge &edge)
    {
        return this->weight < edge.weight;
    }

};


set_pointer find (index i)
{
    index j;
    j = i;
    while(U[j].parent != j)
        j = U[j].parent;
    return j;
}

bool equal(set_pointer p, set_pointer q)
{
    if(p == q)
        return true;
    else
        return false;
}

void makeset(index i)
{
    U[i].parent = i;
    U[i].depth = 0;
}

void initial(int n)
{
    index i;
    for(i = 1; i <= n; i++)
        makeset(i);
}


void dijkstra(int n, const int W[10][10], Edge f)
{
    index i, vnear;

    vector<Edge> e;
    e.push_back(Edge(1,2,7));
    e.push_back(Edge(1,3,4));
    e.push_back(Edge(1,4,6));
    e.push_back(Edge(1,5,1));
    e.push_back(Edge(3,2,2));
    e.push_back(Edge(3,4,5));
    e.push_back(Edge(4,2,3));
    e.push_back(Edge(5,4,1));

    index touch[n];
    index length[n];

    for(i = 2; i <= n; i++)
    {
        touch[i] = 1;
        length[i] = W[1][i];
    }

    while(n - 1 > 0)
    {
        string min = "infinite";
        n--;
        for(i = 2; i <= n; i++)
        {
            if(0 <= length[i] <= sizeof(min))
            {
                min = length[i];
                vnear = i;
            }

        }

        F.push(e[cnt].weight);

    }

}

int main()
{
    queue<int> F;

}