class Solution:
    def check(self,word: str):
        first=0
        last=len(word)-1
        status=1
        while(first<last):
            if(string[first]==string[last]):
                first=first+1
                last=last-1
            else:
                status=0
                break
        return status
        



if __name__ =='__main__':
    solution=Solution()
    string="momm"
    result=solution.check(string)
    if(result==1):
        print("lessgoo")
    else:
        print("boooo")