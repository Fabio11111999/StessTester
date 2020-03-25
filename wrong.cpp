#include<bits/stdc++.h>
using namespace std;
int main(){
	int a=1/0;
	int N;
	cin>>N;
	vector<int> v(N);
	for(int &x:v)
		cin>>x;
	sort(v.begin(),v.end());
	if(v[0]>1)
		swap(v[0],v[N-1]);
	for(int i=0;i<N;i++)
		cout<<v[i]<<" \n"[i==N-1];
}
