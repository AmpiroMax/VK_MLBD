import sys
import csv

def mapper():
    PRICE_COLUMN = 9
    chunk_count = 0
    total_sum = 0

    for line in csv.reader(sys.stdin, delimiter=",")
        price = line[PRICE_COLUMN]
        
        try:
            price = int(price)
        except ValueError:
            continue

        chunk_count += 1
        total_sum += price

    if chunk_count == 0:
        chunk_mean = 0
    else:
        chunk_mean = total_sum / chunk_count
    print(chunk_count, chunk_mean)

if __name__ == "__main__":
    mapper()
