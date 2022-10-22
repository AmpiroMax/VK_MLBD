import sys


def reducer():
    
    data_count = 0
    data_mean = 0
    data_variance = 0

    for line in sys.stdin:
        trio = line.split()
        data_mean_new = data_mean * data_count + trio[0] * trio[1]
        data_mean_new /= data_count + trio[0]

        data_variance_new = data_variance * data_count + trio[0] * trio[2]
        data_variance_new /= data_count + trio[0]
        data_variance_new += data_count * trio[0] * ((data_mean - trio[1]) / data_count + trio[0])**2

        data_count += trio[0]
        data_mean = data_mean_new
        data_variance = data_variance_new

    print(data_count, data_mean, data_variance)

if __name__ == "__main__":
    reducer()
