
def generateStrinngs( i : int,  n : int, arr: list, ans : list):

    if i == n :
        # print(''.join(map(str, arr)))
        ans.append(arr.copy())
        return arr

    arr[i] = 0
    generateStrinngs(i+1, n, arr, ans) 

    arr[i] = 1
    generateStrinngs(i+1, n, arr, ans)


def main():
    n = 3
    i = 0
    arr = [0] * n
    ans = []
    generateStrinngs(i, n, arr, ans)
    print("this is ans",  ans)

main()
