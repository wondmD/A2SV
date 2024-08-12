def count_valid_pairs(n, m):


  # Count multiples of 5 in each list
  n_fives = (n // 5) + (1 if n % 5 == 0 else 0)
  m_fives = (m // 5) + (1 if m % 5 == 0 else 0)

  # Calculate the total number of valid pairs
  return n_fives * m_fives

# Get input from the user
n, m = map(int, input().split())

# Call the function to count valid pairs
num_pairs = count_valid_pairs(n, m)

# Print the result
print(num_pairs)
