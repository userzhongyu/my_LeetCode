class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        temp = []
        ans = ''
        for i in range(0, len(path)):
            if path[i] == '' or path[i] == '.':
                continue
            elif path[i] == '..':
                if len(temp) > 0:
                    temp.pop()
            else:
                temp.append(path[i])
        for item in temp:
            ans += '/' + item
        if ans == '':
            ans = '/'
        return ans


def main():
    path = eval(input())
    print(Solution().simplifyPath(path))


if __name__ == '__main__':
    main()