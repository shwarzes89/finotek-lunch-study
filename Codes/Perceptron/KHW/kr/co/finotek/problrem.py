# AND 게이트를 만족하는 `가중치와 편향을 구해보자
# 최대 3개만
# 0,0 => 0
# 1,0 => 0
# 0,1 => 0
# 1,1 => 0
# 학습 강도는 0.1

import kr.co.finotek.simple03 as perceptron


print(perceptron.AND(0,0))
print(perceptron.AND(1,0))
print(perceptron.AND(0,1))
print(perceptron.AND(1,1))


