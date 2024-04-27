def solution():
    leng = int(input())
    l = list(map(int, input().split()))

    def merge(left, right):
        p1 =0
        p2 =0
        n, m= len(left), len(right)
        res =[]
        while p1 <n and p2<m:
            # print(left[p1])
            if left[p1][0] > right[p2][0]:

                left[p1][0] += m-p2
                res.append(left[p1])
                p1+=1

            elif left[p1][0] < right[p2][0]:
                right[p2][0] += n-p1
                res.append(right[p2])
                p2+=1
            else:
                temp = p1+1
                while temp < n and left[p1][0] == left[temp][0]:
                    temp+=1
                right[p2][0] += n-temp
                res.append(right[p2])
                p2+= 1
        res.extend(left[p1:])
        res.extend(right[p2:])
        return res


    def divide(left, right):
        if left == right:
            return [[l[left],left]]
        mid = (left + right)//2

        left_arr = divide(left,mid)
        right_arr = divide(mid+1, right)


        return merge(left_arr, right_arr)
    result = divide(0, len(l)-1)

    for val, indx in result:
        l[indx] = val
    print(*l)
  
for _ in range(int(input())):
    solution()

# print(solution())
