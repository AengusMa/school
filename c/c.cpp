#include<iostream>
using namespace std;
int max(int i, int j)
{
		if(i>j)
		{
				return (i);
		}
		else
		{
				return (j);
		}
}
int main()
{
		int i,j,k;
		i=3;
		j=5;

		cout<<"hello linux."<<endl;
		k = max(i,j);
		cout<<k<<endl;
		return (0);
}
