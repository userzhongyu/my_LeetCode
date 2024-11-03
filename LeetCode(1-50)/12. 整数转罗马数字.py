"""
    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000
"""
class Solution:
    def intToRoman(self, num: int) -> str:
        s = ''
        dic = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C',
               90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I' }
        for key in dic:
            temp = num // key
            if temp > 0:
                s += dic[key] * temp
                num -= temp * key
        return s

def main():
    while True:
        num = int(input())
        ob = Solution()
        print(ob.intToRoman(num))


if __name__ == '__main__':
    main()



