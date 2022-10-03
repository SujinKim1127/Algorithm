/*
n번째 수열에서 n이 소수인 수열의 합 구하기
*/

#include <iostream>
using namespace std;
int main() {
	int length;
	int num[100001];
	cin >> length;
	int sum = 0;
	for(int i = 1; i <= length; i++){
		cin>>num[i];
		for(int j = 2; j * j <= i; j++){
			if(i % j == 0) num[i] = 0;
		}
		num[1] = 0;
		sum += num[i];
	}
	cout << sum;	
}