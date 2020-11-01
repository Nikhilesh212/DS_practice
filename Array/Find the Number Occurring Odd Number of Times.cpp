#include <iostream>
#include<map>
using namespace std;
int odd_occurance(int arr[],int n)
{
  map<int,int>mp;
  for(int i=0;i<n;i++)
  {

    if(mp.find(arr[i])==mp.end())
    mp.insert({arr[i],1});
    else
    mp.insert({arr[i],mp.find(arr[i])->second+1});
  }
  for(auto i=mp.begin();i!=mp.end();++i)
  {
    //if(i->second%2!=0)
    //return i->first;
    cout<<i->first<<" "<<i->second<<endl;
  }
}
int main()
{
  int arr[7] = {1, 2, 3, 2, 3, 1, 3};
  cout<<odd_occurance(arr,7);
}
