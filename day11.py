a=[[1,2,3,4],[3,4,5,6],[6,7,8,9]]
print(a[0],a[1])
print(a[0][0:3])
print(sum(a[0][0:3]))
b=[[1,2,3,4]]
c=b*4
print(c)
def mv(arr,index1,index2,ran):

    value=0
    for i in range(index1,index1+ran):
        value+=sum(arr[i][index2:index2+ran])##square area
    return value
print(mv(c,0,0,3))
print(max([1,3,4]))





import sys


arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)
sumvalue=[]
def mv(arr,index1,index2):
    return sum(arr[index1][index2:index2+3])+sum(arr[index1+2][index2:index2+3])+arr[index1+1][index2+1]# hourglass
for i in range(0,4):
    for j in range(0,4):
        sumvalue.append(mv(arr,i,j))

print(max(sumvalue))
