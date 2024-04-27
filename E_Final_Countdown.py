from sys import stdin

# Function to calculate the final total 'tot' without the loop
def calculate_total(n, tot):
    return tot + (10**(n-1) - 1) // 9

# Main function
def main():
    for _ in range(int(stdin.readline())):
        n = int(stdin.readline())
        tot = int(stdin.readline())
        result = calculate_total(n, tot)
        print(result)

if __name__ == "__main__":
    main()
