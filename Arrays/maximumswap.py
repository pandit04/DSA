def maximumSwap(num):
        digits = list(str(num))

        last = [0] * 10

        for i, digit in enumerate(digits):
            last[int(digit)] = i

        for i in range(len(digits)):
            current = int(digits[i])

            for d in range(9, current, -1):
                if last[d] > i:
                    j = last[d]

                    digits[i], digits[j] = digits[j], digits[i]

                    return int("".join(digits))

        return num