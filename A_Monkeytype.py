
def sol():
    alpha = input()
    word = input()
    dictionary = {alpha[i]:i+1 for i in range(len(alpha))}
    ans = 0
    for i in range(1,len(word)):
        ans += abs(dictionary[word[i]] - dictionary[word[i-1]])
    return ans

for _ in range(int(input())):
    print(sol())