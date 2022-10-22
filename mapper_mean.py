#!/usr/bin/python3
import sys


def mapper():
    PRICE_COLUMN = 9
    
    chunk_count = 0
    total_sum = 0

    for line in sys.stdin:
        price = line.split(',')[PRICE_COLUMN]
        if not price.isdigit():
            continue
        price = int(price)
        chunk_count += 1
        total_sum += price

    chunk_mean = total_sum / chunk_count

    print(chunk_count, chunk_mean)

if __name__ == "__main__":
    mapper()
