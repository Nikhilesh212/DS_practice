#include <iostream>
#include<map>
using namespace std;
int odd_occurance(int arr[],int n)
{
  map<int,int>mp;
  for(int i=0;i<n;i++)
  {
    mp[arr[i]]+=1;
  }
  for(auto i=mp.begin();i!=mp.end();i++)
  {
    if(i->second%2!=0)
    return i->first;
    //cout<<i->first<<" "<<i->second<<endl;
  }
}
