import sys


def reducer():
    
    data_count = 0
    data_sum = 0
    data_sq_sum = 0

    for line in sys.stdin:
        trio = line.split()
        data_count += trio[0]
        data_sum += trio[0] * trio[1]
        data_sq_sum += (trio[2] + (trio[0] * trio[1])**2) * trio[0]
    
    data_mean = data_sum / data_count
    data_variance = data_sq_sum / data_count - data_mean**2

    print(data_variance)

if __name__ == "__main__":
    reducer()
