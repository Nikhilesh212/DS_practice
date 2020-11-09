#include<iostream>
using namespace std;
string next_greatest(string s,int a,int b){
  int flag=0,ind=0;
	    for(int i=s.length()-1-a;i!=b;i--){
	        for(int j=i-1;j!=b;j--){
	            if(stoi(to_string(s[i])) > stoi(to_string(s[j]))){
	                a=i;
                  b=j;
	                flag=1;
	                ind = j+1;
	                break;
	            }
	        }
          cout<<a<<" "<<b<<endl;
	        if(flag==1)
	            return next_greatest(s,a,b);
          else
          {
            cout<<"hi";
            swap(s[a],s[b]);
            return s;
          }
	    }
    }
int main()
{
  string s = "34722641";
  cout<<next_greatest(s,0,0);
}
