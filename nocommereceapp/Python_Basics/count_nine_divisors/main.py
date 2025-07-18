def count_numbers_with_nine_divisors(n):
    def count_divisors(num):
        count = 0
        for i in range(1, int(num**0.5) + 1):
            if num % i == 0:
                count += 1
                if i != num // i:
                    count += 1
        return count

    count = 0
    for i in range(1, n + 1):
        if count_divisors(i) == 9:
            count += 1

    return count

if __name__ == "__main__":
    n = int(input("Enter a positive integer n: "))
    result = count_numbers_with_nine_divisors(n)
    print(f"Count of numbers with exactly 9 divisors less than or equal to {n}: {result}")