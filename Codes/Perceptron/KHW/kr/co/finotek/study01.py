import numpy as np

inputX = np.array([[29,56],[64,89],[33, 17],[45, 94],[24, 26],[55, 24],[35, 52],[57, 65],[45, 32],[52, 75],[62, 31]              ])
outputY = np.array([1,1,0,1,0,0,1,1,0,1,0])

def perceptron01(x,w,b):
    tmp = np.sum(w*x) + b
    if tmp <= 0: return 0
    elif tmp > 0: return 1

def execute(b):
    # 학습율 : 0.1
    # w의 범위 : -0.9 ~ 0.9
    w1s = np.arange(-0.9, 1.0, 0.1)
    w2s = np.arange(-0.9,1.0,0.1)

    result = np.array([False, False, False, False, False, False, False, False, False, False, False])

    for w1 in w1s:
        for w2 in w2s:
            w = np.array([w1, w2])
            idx = 0;
            for x in inputX:
                tmp = perceptron01(x, w,b)
                y = outputY[idx]
                if tmp != y:
                    result[idx] = False;
                    continue
                elif tmp == y:
                    result[idx] = True
                    idx += 1

                # 검증결과의 값이 모드 참인지 확인
                if ((result == True).all()):
                    print(w, b)
                    result = np.array([False, False, False, False, False, False, False, False, False, False, False])
    return 0;

def main():
    for b in np.arange(-0.9,1.0,0.1):
        print(b)
        execute(b)

main()