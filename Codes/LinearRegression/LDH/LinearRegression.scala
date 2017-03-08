import scala.math._

object LinearRegression extends App {
  val x = List[Double](1400, 1600, 1700, 1875, 1100, 1550, 2350, 2450, 1425, 1700)
  val y = List[Double](245, 312, 279, 308, 199, 219, 405, 324, 319, 255)

  def make_f(w:Double) = (x:Double) => w * x + 0

  def cost(w:Double) =
    x.zip(y).foldLeft(0.0) { (sum, point) =>
      val x = point._1
      val y = point._2

      sum + pow(w * x - y, 2)
    } / x.size

  def deri_cost(w:Double):Double =
    x.zip(y).foldLeft(0.0) { (sum, point) =>
      val x = point._1
      val y = point._2

      sum + ((w * x - y) * x)
    } / x.size

  // gradient decent algorithm
  val precision = 0.0000001
  val lr = 0.0000001

  def operation(prev:Double, w:Double):Double =
    if(abs(w - prev) < precision) {
      w
    } else {
      val next = w - lr * deri_cost(w)
      printf("w: %f, next: %f\n", w, next)
      operation(w, next)
    }

  val w = operation(3, 5)
  val f = make_f(w)

  println("--------------")
  println("Predicted price of the house: " + f(800) + " with 800 feet")
  println("Predicted price of the house: " + f(1200) + " with 1200 feet")
  println("Predicted price of the house: " + f(1400) + " with 1400 feet")
  println("Predicted price of the house: " + f(1800) + " with 1800 feet")
}