#!/usr/bin/python3
import sys


def mapper():
    PRICE_COLUMN = 9
    
    chunk_count = 0
    total_sum = 0
    total_sq_sum = 0

    for line in sys.stdin:
        price = line.split(',')[PRICE_COLUMN]
        if not price.isdigit():
            continue
        chunk_count += 1
        total_sum += price
        total_sq_sum += price**2

    chunk_mean = total_sum / chunk_count
    chunk_variance = total_sq_sum / chunk_count - chunk_mean
    print(chunk_count, chunk_mean, chunk_variance)

if __name__ == "__main__":
    mapper()
