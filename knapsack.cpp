#include <iostream>
#include <vector>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
#include <queue>
using namespace std;

typedef int index;

int maxprofit = 0;
int profit = 0;
int weight = 0;


// input
int n = 4;
int W = 16;
int w[4] = {2, 5, 10, 5};
int p[4] = {40, 30, 50, 10};

char include[5];
char bestset[5];

bool promising(index i)
{
    index j, k;
    int totweight;
    float bound;

    if(weight >= W) return false;
    else
    {
        j = i + 1;
        bound = profit;
        totweight = weight;
        while ((j <= n) && (totweight + w[j] <= W))
        {
            totweight = totweight + w[j];
            bound = bound + p[j];
            j++;
        }
        k = j;
        if(k <= n)
        {
            bound = bound + (W - totweight) * p[k]/w[k];
            return bound > maxprofit;
        }
    }
}

void knapsack(index i, int profit, int weight)
{
    if(weight <= W && profit > maxprofit)
    {
        maxprofit = profit;
        // numbest = i;
        strcpy(bestset, include);   // bestset = include
    }
    if(promising(i))
    {
        include[i+1] = 'Y';
        knapsack(i+1, profit + p[i+1], weight + w[i+1]);
        include[i+1] = 'N';
        knapsack(i+1, profit, weight);
    }
}


int main()
{
    knapsack()
    knapsack(3, 90, 12);
    for(int i = 0; i < n; i++)
        cout<<include[i]<<" ";
}