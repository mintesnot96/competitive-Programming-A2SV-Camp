def superDigit(n, k):
    if len(n) == 1:
        return int(n)

    digit_sum = sum(map(int, n)) * k
    return superDigit(str(digit_sum), 1
                      

                     
# https://www.hackerrank.com/challenges/recursive-digit-sum/problem
