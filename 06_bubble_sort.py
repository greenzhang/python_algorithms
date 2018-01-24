#coding:utf-8
def bubble(alist):
    n = len(alist)
    for i in range(0,n-1):
        count = n
        for j in range(0,n-i-1):
            if alist[j] > alist[j+1]:
                alist[j],alist[j+1] = alist[j+1],alist[j]
        if 0 == count:
            return
if __name__ == "__main__":
    a = [123,3,2,5,1,4]
    bubble(a)
    print(a)