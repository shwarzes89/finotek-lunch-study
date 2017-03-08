import scala.math._
import scala.util.Random

object GradientDecent extends App {
  def f(x:Double):Double = pow(x,2) + 1

  def df(x:Double):Double = 2 * x

  def gradient_decent(precision:Double): Double = {
    val lr = 0.01
    val start = Random.nextInt(5) + 1

    def op(prev:Double, start:Double): Double =
      if(abs(start - prev) < precision) {
        start
      } else {
        val nextStep = start - lr * df(start)
        printf("prev: %f, next: %f \n", start, nextStep)

        op(start, nextStep)
      }

    op(start + 3, start)
  }

  val min = gradient_decent(0.0001)
  printf("최소값이 되는 변수 x의 값 %f, 최소값 %f", min, f(min))
}
