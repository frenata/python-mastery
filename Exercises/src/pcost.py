import sys


def main(filename):
    total = 0

    with open(filename) as f:
        for line in f:
            ticker, shares, price = line.split(" ")
            total += int(shares) * float(price)

    return total


if __name__ == "__main__":
    print(main(sys.argv[1]))
