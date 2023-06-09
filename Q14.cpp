/*Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".*/
#include<iostream>
using namespace std;
#include <string>
#include <vector>
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string result;
        string str;
        int min=9999;
        int len;
        for(int i=0; i<strs.size();i++){
            len=strs[i].length();
            // cout<<len<<endl;
            if(min>len){
                min=len;
                str=strs[i];
            }
        }
        cout<<min;
  
        for(int i=0; i<min;i++){
            for(int j=0; j<strs.size();j++){
                int count=0;
                if(strs[j][i]!=str[i])
                {
                    return str.substr(0,i);
                }

            }

            
    
        }
        return str.substr(0,min);
        
    }
};
int main(){

}
