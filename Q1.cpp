#include<iostream>
using namespace std;
#include<unordered_map>
#include<vector>
class solution{
    public:
        vector<int>nums;
        solution(vector<int> a)
        {
            for(int i=0;i<a.size();i++)
            {
                nums.push_back(a[i]);
            }       
        }
        vector<int> Twosum(int target)
        {
            vector<int> ans;
            unordered_map<int,int> umap;
            int temp;
            for(int i=0;i<nums.size();i++)
            {
                temp=target-nums[i];
                if(umap.find(temp)!=umap.end() && umap.find(temp)->second!=i) //umap.find(temp) basically iterates where the element is present if it is not equal to the end then it means its present in some position in the array
                {
                    ans.push_back(i);
                    ans.push_back(umap.find(temp)->second);
                    break;
                }
                umap[nums[i]]=i;
            }
            return ans;
        }
    
};
int main()
{
    vector<int> num;
    int size,temp;
    cout<<"Enter number of elements in the vector:";
    cin>>size;
    for(int i=0;i<size;i++)
    {   
        cin>>temp;
        num.push_back(temp);
        // cout<<num[i];
    }
    solution abc(num);
    num= abc.Twosum(6);
    for(int i=0;i<num.size();i++)
    {
        cout<<num[i]<<endl;
    }

}
