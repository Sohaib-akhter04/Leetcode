#include<iostream>
using namespace std;

class Solution {
public:
    bool isPalindrome(long num) {
        long n=num,digit,reverse=0;
        if(num<0)
        {   
            cout<<"false";
            return false;
        }
        do{
            digit=num%10;
            reverse=(reverse*10)+digit;
            num=num/10;
        }   
        while(num!=0);
        if(n==reverse)
        {
            cout<<"true";
            return true;
        }
        else{
            cout<<"false";
            return false;
        }    
        }
        
};
int main()
{
    Solution abc;
    abc.isPalindrome((1000660001));
}