import sys

def reducer():
    
    data_sum = 0
    data_count = 0
    for line in sys.stdin:
        pair = line.split()
        data_sum += float(pair[0]) * float(pair[1])
        data_count += float(pair[0])

    print(data_count, data_sum / data_count)

if __name__ == "__main__":
    reducer()
