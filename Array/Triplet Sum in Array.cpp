#include <bits/stdc++.h>
using namespace std;
int hasArrayTwoCandidates(vector<int> arr, int n, int x) {
    map<int,int> no;
    for(int i=0;i<n;i++)
    {
        no[arr[i]]+=1;
    }
    for(int i=0;i<n;i++)
    {
        if(x-arr[i]==arr[i])
        {
            if(no[arr[i]]>=2)
            return 1;
        }
        else if(no[x-arr[i]]>=1)
        {
            //cout<<x<<" "<<arr[i]<<" "<<x-arr[i]<<" ";
            return 1;
        }
    }
    return 0;
}
int main() {
	int t;
	cin>>t;
	while(t>0)
	{
	    int n,x;
	    cin>>n>>x;
	    vector<int> a;
	    for(int i=0;i<n;i++)
	    {
	        int s;
	        cin>>s;
	        a.push_back(s);
	    }

	    int f=0;
	    for(int i=0;i<n;i++)
	    {
	        vector<int> temp;
	        temp=a;
	        temp.erase(temp.begin()+i);
	        int ans=hasArrayTwoCandidates(temp,n-1,x-a[i]);
	        if(ans==1)
	        {
	            cout<<1<<endl;
	            f=1;
	            break;
	        }

	    }
	    if(f==0)
	    cout<<0<<endl;
	    t--;
	}
	return 0;
}
