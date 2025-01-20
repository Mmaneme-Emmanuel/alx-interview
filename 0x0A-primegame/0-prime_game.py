#!/usr/bin/python3
"""Module defining isWinner function."""


def isWinner(x, nums):
    """Determines the winner of the prime game."""
    if not nums or x <= 0:
        return None

    # Find the maximum number in nums
    max_n = max(nums)

    # Precompute primes using the Sieve of Eratosthenes
    primes = sieve_of_eratosthenes(max_n)

    # Calculate cumulative prime counts
    prime_counts = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_counts[i] = prime_counts[i - 1] + (1 if primes[i] else 0)

    # Count wins for Maria and Ben
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # Determine the number of primes up to n
        if prime_counts[n] % 2 == 1:  # Maria wins if the count is odd
            maria_wins += 1
        else:  # Ben wins if the count is even
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None


def sieve_of_eratosthenes(n):
    """Returns a list of booleans where True indicates a prime number."""
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not primes
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return primes
