import math

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return(False)
        elif x<10:
            return(False)
        else:
            return str(x)==str(x)[::-1]
    
    def helloWorld(self, y: float) -> bool:
        pi = math.pi
        if y>=pi:
            return y==7
        else:
            return(False)
class Calculation:
    def squareRoot(self, n: float):
        if n<0:
            return('Cannot square root negative numbers.')
        else:
            return(round(math.sqrt(n), 4))
    def logarithm(self, num: float):
        if num<0:
            return(False)
        else:
            return(
                math.log(num)
            )
            
            
x = int(input("Integer input: "))
y = float(input('Float input: '))
n = float(input('Number to be square rooted: '))
num = float(input('Input numnber to have the natural log taken of: '))
print(f'Is palindrome: {Solution().isPalindrome(x)}')
print(f'Hello world: {Solution().helloWorld(y)}')
print(f'Square root: {Calculation().squareRoot(n)}')
print(f'Natural log of number: {Calculation().logarithm(num)}')