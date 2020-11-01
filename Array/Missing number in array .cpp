#include <iostream>
#include<map>
using namespace std;
int missing(int arr[],int n)
{
	int sum=((n+1)*(n+2))/2;
	for(int i=0;i<n;i++)
	{
		sum-=arr[i];
	}
	return sum;
}
int main()
{
  int t;
	cin>>t;
	while(t>0)
	{
		int n;
		cin>>n;
		int arr[n-1];
		for(int i=0;i<n-1;i++)
		{
			cin>>arr[i];
		}
		cout<<missing(arr,n-1)<<endl;
		t--;
	}
}
