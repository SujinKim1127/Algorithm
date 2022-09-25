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
int profit;
int numbest = 0;


// input
int n = 4;
int W = 12;
int p[5] = {0, 60,30,40,20};
int w[5] = {0, 3,3,8,5};
string include[6], bestset[6];

bool promising(index i, int wweight)
{
    index j, k;
    int totweight;
    float bound;

    if(wweight >= W) return false;
    else
    {
        j = i + 1;
        bound = (float)profit;
        totweight = wweight;
        while ((j <= n) && (totweight + w[j] <= W))
        {
            totweight = totweight + w[j];
            bound = bound + p[j];
            j++;
        }
        k = j;
        if(k <= n)
        {
            bound = bound + (W - totweight) * p[k] / w[k];
        }
		cout << "profit: " << profit << ",\tweight: " << wweight << ",\tbound: " << bound << endl;
		cout << "maxprofit: " << maxprofit << ",\ttotweight: " << totweight << endl<<endl;

        if (bound > maxprofit) 
            return true;

		else    // bound <= maxprofit 
            return false;

    }
}

void knapsack(index i, int pprofit, int wweight)
{
    if(wweight <= W && pprofit > maxprofit)
    {
        maxprofit = pprofit;
        numbest = i;
        for(int j = 1; j <= n; j++)
            bestset[j] = include[j];
    }
    if(promising(i, wweight))
    {
        include[i+1] = "YES";
        profit = pprofit + p[i + 1];
        knapsack(i+1, pprofit + p[i+1], wweight + w[i+1]);

        include[i+1] = "NO";
        profit = pprofit;
        knapsack(i+1, pprofit, wweight);
    }
}


int main()
{
    int weight = 0;
    profit = 0;

	cout <<"i \tp \tw \t" << endl;
    for(int i = 1; i <= n; i++)
		cout << i << ": \t" << p[i] << "\t" << w[i] << "\t" << endl;

    knapsack(0, 0, 0);
    cout << "bestset: ";
    for(int i = 1; i <= n; i++)
        cout<<bestset[i]<<" ";
}