#1374331 josh fitzgerald

num_calls=0

def partition(user_ids,i,k):
    p=(i+k)//2
    index=i
    while(index<=k):
        while(user_ids[index]<user_ids[p]):
            index=index+1
        while(user_ids[k]>user_ids[p]):
            k=k-1
        if(index<=k):
            t=user_ids[index]
            user_ids[index]=user_ids[k]
            user_ids[k]=t
            index=index+1
            k=k-1
    return index

def quicksort(user_ids,i,k):
    global num_calls
    num_calls=num_calls+1
    if(i>=k):
        return
    index=partition(user_ids,i,k)
    quicksort(user_ids,i,index-1)
    quicksort(user_ids,index,k)

if __name__=="__main__":
    user_ids=[]
    user_id=input()
    while user_id!="-1":
        user_ids.append(user_id)
        user_id=input()
    quicksort(user_ids,0,len(user_ids) - 1)
    print(num_calls)
    for user_id in user_ids:
        print(user_id)
