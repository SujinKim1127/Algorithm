#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int getParent(int set[], int x)
{
    if(set[x] == x) return x;
    return set[x] = getParent(set, set[x]);
}



void kruskal(int n, int m, char E, char F)
{
    // index i, j;
    int i, j;
    // set_pointer p, q;
    char p, q;
    // edge e;
    int e;

    // sort the m edges in E by weight in nondecreasing order;
    // F = 공집합;

    // initial(n);

    while (F < n-1)
    {
        // e = edges with least weight not yet considered;
        // i, j = indices of vertices connected by e;
        // p = find(i);
        // q = find(j);
        // if(!equal(p,q)){
        //     merge(p,q);
        //     add e to F;
        // }
    }
}