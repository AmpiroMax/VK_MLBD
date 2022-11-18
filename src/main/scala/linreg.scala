import breeze.linalg.{
    DenseMatrix,
    csvread, csvwrite,
    inv, sum
}
import java.io.File


class DataWorker(val data_path: String){
    def read_data() = {
        val train = csvread(new File(data_path+"train.csv"),',')
        val test = csvread(new File(data_path+"test.csv"),',')
        
        val cols = train.cols-1
        val train_rows = train.rows
        val train_size = 0.8

        val x_train = train(1 until (train_rows * train_size).toInt, 0 until cols)
        val y_train = DenseMatrix(train(1 until (train_rows * train_size).toInt, cols)).t

        val x_valid = train((train_rows * train_size).toInt until train_rows, 0 until cols)
        val y_valid = DenseMatrix(train((train_rows * train_size).toInt until train_rows, cols)).t

        val test_rows = test.rows
        val x_test = test(1 until test_rows, 0 until cols)

        (x_train, y_train, x_valid, y_valid, x_test)
    }

    def write_data(predictions: DenseMatrix[Double]) = {
        csvwrite(new File(data_path+"predictions.csv"), predictions, ',')
    }
}

class LinReg(val n_in: Int, val n_out: Int){
    var weights = DenseMatrix.rand(n_in, n_out)

    def mse_loss(y_true: DenseMatrix[Double], y_pred: DenseMatrix[Double]) = {
        sum((y_true - y_pred)*:*(y_true - y_pred))
    }

    def fit(x_train: DenseMatrix[Double], y_train: DenseMatrix[Double]) = {
        weights = inv(x_train.t * x_train) * x_train.t * y_train
    }

    def predict(x_test: DenseMatrix[Double]) = {
        x_test * weights
    }
}

object Hello {
    def main(args: Array[String]) = {
        val worker = new DataWorker("data/")
        val data = worker.read_data()
        
        val x_train = data._1
        val y_train = data._2
        val x_valid = data._3
        val y_valid = data._4
        val x_test = data._5

        val cols = x_train.cols
        val model = new LinReg(cols, 1)

        val pred1 = model.predict(x_valid)
        println("MSE loss before fit " + model.mse_loss(y_valid, pred1))

        model.fit(x_train, y_train)
        val pred2 = model.predict(x_valid)
        println("MSE loss after fit " + model.mse_loss(y_valid, pred2))

        worker.write_data(model.predict(x_test))

    }
}

 