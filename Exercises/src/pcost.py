import sys
import logging

logger = logging.getLogger(__name__)


def main(filename):
    total = 0

    with open(filename) as f:
        for line in f:
            ticker, shares, price = line.split()
            try:
                total += int(shares) * float(price)
            except Exception as e:
                logger.exception(f"Failed to parse {line}")

    return total


if __name__ == "__main__":
    print(main(sys.argv[1]))
