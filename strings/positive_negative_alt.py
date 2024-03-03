def function(array):
    positive=[ num for num in  array if num>0]
    negative=[ num for num in  array if num<0]
    p_index=0
    n_index=0
    for i in range(len(array)):
        if i%2==0:
            array[i]=positive[p_index]
            p_index+=1
        else:
            array[i]=negative[n_index]
            n_index+=1
    print(array)

if __name__=="__main__":
    array=[-1,1,2,-2,3,-4]
    print(array)
    function(array)