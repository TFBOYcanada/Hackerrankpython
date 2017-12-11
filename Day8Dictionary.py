# cmd optional +l   PEM8
if __name__ == "__main__":
    print("one.py is being run directly")
else:
    print("one.py is being imported into another module")

print('number of ')

n = int(input().strip())
dict1 = {}
# arr = [str(arr_temp) for arr_temp in input().strip().split(' ')]
for i in range(0, n):
    arr = [str(arr_temp) for arr_temp in input().strip().split(' ')]
    # name,number=input().split()
    print('name and number')
    seq = str(arr[0])
    key = arr[1]
    dict1[seq] = key  ## dictionary adding new keys and values

for i in range(0, n):
    name = input().strip()
    resl = dict1.get(name, 'Not found')
    if resl == 'Not found':

        print("Not found")
    else:
        # print(name,,resl)
        print("{}={}".format(name, dict1[name]))
if __name__ == "__main__":
    print("one.py is being run directly")
else:
    print("one.py is being imported into another module")
