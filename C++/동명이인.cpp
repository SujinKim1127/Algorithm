/* 
자신과 비슷한 이름을 가진 사람 찾기
*/

#include <iostream>
#include <string>
using namespace std;

int main() {
	int num;
	string name = "";
	string input = "";
	cin >> num;
	cin >> name;
	int cnt = 0;
	for(int i = 0; i < num; i++){
		cin >> input;
		if (input.find(name) != string::npos) cnt++;
	}
	cout << cnt;
}