#include <iostream>
using namespace std;
int next_min(int arr[],int i,int n)
{
    for(int j=i+1;j<n;j++)
    {
        if(arr[j]>arr[j-1])
        return j-1;
    }
    return -1;
}
int next_max(int arr[],int i,int n)
{
    for(int j=i+1;j<n;j++)
    {
        if(arr[j]<arr[j-1])
        return j-1;
    }
    return n-1;
}
int main() {
	int t;
	cin>>t;
	while(t>0)
	{
	    int n,f=0;
	    cin>>n;
	    int arr[n];
	    for(int i=0;i<n;i++)
	    {
	        cin>>arr[i];
	    }
	    for(int i=0;i<n;i++)
	    {
	        int temp=next_min(arr,i,n);
	        if(temp==-1)
	        {
	            if(f==0)
	            cout<<"No Profit";
	            break;
	        }
	        else
	        {
	            f=1;
	            i=temp;
	            int temp2=next_max(arr,i,n);
	            cout<<"("<<temp<<" "<<temp2<<") ";
	            i=temp2;
	        }
	    }
	    cout<<endl;
	    t--;
	}
	return 0;
}
