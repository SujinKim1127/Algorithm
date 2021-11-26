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


void merge(set_pointer p, set_pointer q)
{
    if(U[p].depth == U[q].depth)
    {
        U[p].depth++;
        U[q].parent = p;
    }
    else if(U[p].depth < U[q].depth)
        U[p].parent = q;
    else 
        U[q].parent = p;
    // cout<<endl;
    // cout<<"\t merge"<<endl;
    // cout<<"U"<<p<<": "<<U[p].depth<<endl;
    // cout<<"U"<<q<<": "<<U[q].depth<<endl;
}

void kruskal(int n, int m, queue<int> F)
{
    index i, j;
    set_pointer p, q;

    // edge e
    vector<Edge> e;
    e.push_back(Edge(1,2,1));
    e.push_back(Edge(1,3,3));
    e.push_back(Edge(2,3,3));
    e.push_back(Edge(2,4,6));
    e.push_back(Edge(3,4,4));
    e.push_back(Edge(3,5,2));
    e.push_back(Edge(4,5,5));    

    sort(e.begin(), e.end());
    // cout<<"e print"<<endl;
    // for(int a = 0; a < m; a++)
    //     cout<<e[a].weight<<" "<<endl;
    // F 이미 공백
    initial(n);

    int cnt=0;
    while (cnt < m)
    {
        i = e[cnt].node[0];
        j = e[cnt].node[1];
        // cout<<"i,  j: "<<i<<",  "<<j<<endl;
        p = find(i);
        q = find(j);

        // cout<<"p, q    O"<<endl;
        // cout << p << ",  " << q <<endl;

        if(!equal(p, q))
        {
            merge(p, q);
            F.push(e[cnt].weight);

            cout<<"F: "<<F.front()<<endl;
            F.pop();

        }
        // else
        // {
        //     cout<<"XXX merge XXX"<<endl;   
        //     cout<<"----------------------"<<endl;
        // }
        cnt++;

    }
}

int main()
{
    queue<int> F;
    kruskal(5, 7, F);
}