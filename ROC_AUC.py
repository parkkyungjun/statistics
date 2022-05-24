import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import auc

def draw_ROC_Curve(ac, pro):
    uac = ['NG', 'OK']
    upro = sorted(set(pro))
    x, y = [], []
    M = 0
    for i in upro:
        tp, fn, fp, tn = 0, 0, 0, 0
        for j in range(len(pro)):
            if pro[j] >= i and ac[j] == uac[0]:
                tp += 1
            elif pro[j] < i and ac[j] == uac[0]:
                fn += 1
            elif pro[j] >= i and ac[j] == uac[1]:
                fp += 1
            elif pro[j] < i and ac[j] == uac[1]:
                tn += 1

        x.append(fp / (fp + tn))
        y.append(tp / (tp + fn))
        #print(fp / (fp + tn), tp / (tp + fn))
        if tp / (tp + fn) - fp / (fp + tn) >= M:
            M = tp / (tp + fn) - fp / (fp + tn)
            MM = i
    plt.plot(x, y)
    plt.xlabel('FPR')
    plt.ylabel('TPR')
    print(f'threshold: {MM}\nauc: {auc(x,y)}')
    plt.show()

# a = pd.read_csv("C:/momentum/ROC_AUC.csv")
# ac = a['ac']
# pro = a['pro']
#
# draw_ROC_Curve(ac, pro)
