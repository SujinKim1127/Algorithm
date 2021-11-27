#include <iostream>
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


void dijkstra(int n, const int W[10][10])
{
    index i, vnear;
    index touch[n];
    index length[n];

    for(i = 2; i <= n; i++)
    {
        touch[i] = 1;
        length[i] = W[1][i];
    }

    while((n-1)--)
    {
        
    }

}