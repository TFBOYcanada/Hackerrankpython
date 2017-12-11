# Write your code here
class Calculator(object):  ##python3中有无object 都默认带obejct 继承所有属性  python2 不同
    def power(self, n, p):
        if (n < 0) or (p < 0):
            raise Exception("n and p should be non-negative")
        else:
            return n ** p


myCalculator = Calculator()
T = int(input())
for i in range(T):
    n, p = map(int, input().split())
    try:
        ans = myCalculator.power(n, p)
        print(ans)
    except Exception as e:
        print(e)
