#include<iostream>
#include<map>
#include<vector>
using namespace std;
vector<int> singleNumber(vector<int>& nums)
{
    map<int,int>mp;
    vector<int> ans;
    for(auto i=nums.begin();i!=nums.end();i++)
    {
        mp[*i]+=1;
    }
    for(auto i=nums.begin();i!=nums.end();i++)
    {
        if(mp[*i]==1)
        {
          ans.push_back(*i);
          cout<<*i;
        }
        if(ans.size()==2)
        break;
    }
    return ans;
}
int main()
{
  vector<int> input;
  int n;
  for(int i=0;i<n;i++)
  {
    int a;
    cin>>a;
    input.push_back(a);
  }
  singleNumber(input);
}
