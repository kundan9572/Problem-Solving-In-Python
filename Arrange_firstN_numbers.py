# Python implementation of the approach

# Function to return the count
# of required arrangements
def countWays(n):
    # Create the dp array
    dp = [0 for i in range(n + 1)]

    # Initialize the base cases
    # as explained above
    dp[0] = 0
    dp[1] = 1

    # (12) as the only possibility
    dp[2] = 1

    # Generate answer for greater values
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 3] + 1

    # dp[n] contains the desired answer
    return dp[n]


# Driver code
n = int(input("Enter the number"))

print(countWays(n))

