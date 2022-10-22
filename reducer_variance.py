import sys


def reducer():
    
    data_count = 0
    data_sum = 0
    data_sq_sum = 0

    for line in sys.stdin:
        trio = line.split()
        data_count += float(trio[0])
        data_sum += float(trio[0]) * float(trio[1])
        data_sq_sum += (float(trio[2]) + (float(trio[1]))**2) * float(trio[0])
    
    data_mean = data_sum / data_count
    data_variance = data_sq_sum / data_count - data_mean**2

    print(data_variance)

if __name__ == "__main__":
    reducer()
