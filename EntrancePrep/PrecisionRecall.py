def PrecisionRecall(y_true, y_pred):
    TP = sum(1 for true, pred in zip(y_true, y_pred) if true==1 and pred==1)
    FP = sum(1 for true, pred in zip(y_true, y_pred) if true==0 and pred==1)
    FN = sum(1 for true, pred in zip(y_true, y_pred) if true==1 and pred==0)
    precision = TP / (TP+FP) if (TP+FP) >0 else 0
    recall = TP / (FN+TP) if (TP+FN) >0 else 0
    return (precision*100, recall*100)

y_true = [0, 1, 0, 1, 1]
y_pred = [0, 1, 1, 1, 0]

print(PrecisionRecall(y_true, y_pred))