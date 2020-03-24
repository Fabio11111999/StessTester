#include<bits/stdc++.h>
using namespace std;
//Only 1 parameter , the seed
int main(int argc, char **argv){
	int seed=atoi(argv[1]);
	srand(seed);
	int N=1+rand()%10000;
	cout<<N<<endl;
	for(int i=0;i<N;i++)
		cout<<1+rand()%100<<" ";
}
