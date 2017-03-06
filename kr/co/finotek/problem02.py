import numpy as np

# 입력값 AND 게이트
inputX= np.array([[0,0],[1,0],[0,1],[1,1]]);
outputY = np.array([0,0,0,1])
b = -0.8
# 편향 : 고정
# 입력값 : 고정
# AND게이트 조건을 만족하는 퍼셉트론을 구해 봅시다
def perceptron01(x,w):
    tmp = np.sum(w*x) + b
    if tmp <= 0: return 0
    elif tmp > 0: return 1

def main():
    # 학습율 : 0.1
    # w의 범위 : -0.9 ~ 0.9
    w1s = np.arange(-0.9,1.0,0.1)
    w2s = np.arange(-0.9,1.0,0.1)

    result = np.array([False,False,False,False])

    for w1 in w1s:
        for w2 in w2s:
            w = np.array([w1, w2])
            idx = 0;
            for x in inputX:
                tmp = perceptron01(x, w)
                y = outputY[idx]
                if tmp != y:
                    result[idx] = False;
                    continue
                elif tmp == y:
                    result[idx] = True
                    idx += 1

                #검증결과의 값이 모드 참인지 확인
                if((result == True).all()):
                    print(w, b)
                    result = np.array([False,False,False,False])
    return 0;

main()


