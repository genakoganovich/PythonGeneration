# Python3 implementation to print
# first N Taxicab(2) numbers
import math


def print_taxicab(n):
    # Starting from 1, check every number if
    # it is Taxicab until count reaches N.
    i = 1
    count = 0
    while count < n:
        int_count = 0

        # Try all possible pairs (j, k)
        # whose cube sums can be i.
        for j in range(1, math.ceil(pow(i, 1.0 / 3)) + 1):

            for k in range(j + 1, math.ceil(pow(i, 1.0 / 3)) + 1):
                if j * j * j + k * k * k == i:
                    int_count += 1

        # Taxicab(2) found
        if int_count == 2:
            count += 1
            print(count, " ", i)

        i += 1


# Driver code
N = 5
print_taxicab(N)

# This code is contributed by Anant Agarwal.