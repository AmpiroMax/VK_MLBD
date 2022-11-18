from sklearn.datasets import make_regression
import pandas as pd


def generate_data():
    DATA_SIZE = 100
    TRAIN_SIZE = 0.8
    data = make_regression(
        n_samples=DATA_SIZE,
        n_features=10,
        n_informative=2,
        noise=0.1,
        random_state=42
    )
    X = data[0]
    y = data[1]

    x_frame = pd.DataFrame(X)
    y_frame = pd.DataFrame(y)
    data_frame = pd.concat([x_frame, y_frame], axis=1)

    train = data_frame[:int(TRAIN_SIZE * DATA_SIZE)]
    test = data_frame[int(TRAIN_SIZE * DATA_SIZE):]

    train.to_csv("data/train.csv", index=False)
    test.to_csv("data/test.csv", index=False)


if __name__ == "__main__":
    generate_data()
