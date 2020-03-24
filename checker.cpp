#include<bits/stdc++.h>
using namespace std;
int main(){
	ifstream correct_in("files/correct_output.txt"), wrong_in("files/wrong_output.txt");
	vector<string> c, w;
	string tmp;
	while(!correct_in.eof()){
		correct_in>>tmp;
		c.push_back(tmp);
	}
	while(!wrong_in.eof()){
		wrong_in>>tmp;
		w.push_back(tmp);
	}
	if(c.size()!=w.size())
		return 1;
	for(int i=0;i<(int)c.size();i++)
		if(c[i]!=w[i])
			return 1;
	return 0;
}
