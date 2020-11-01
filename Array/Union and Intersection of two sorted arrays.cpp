#include <iostream>
#include<map>
#include<vector>
using namespace std;
int main() {
	int t;
  cin>>t;
  while(t>0)
  {
    map<int,int>mp;
    int n1,n2;
    vector<int>u;
    cin>>n1>>n2;
    int a1,a2;
    for(int i=0;i<n1;i++)
    {
      cin>>a1;
      mp.insert({a1,1});
      u.push_back(a1);
    }
    for(int i=0;i<n2;i++)
    {
      cin>>a2;
      if(mp.find(a2)!=mp.end())
      continue;
      else
      u.push_back(a2);
    }
    t--;
  }
	return 0;
}
