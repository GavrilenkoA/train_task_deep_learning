def binary_classification_metrics(prediction, ground_truth):
    '''
    Computes metrics for binary classification

    Arguments:
    prediction, np array of bool (num_samples) - model predictions
    ground_truth, np array of bool (num_samples) - true labels

    Returns:
    precision, recall, f1, accuracy - classification metrics
    '''
    precision = 0
    recall = 0
    accuracy = 0
    f1 = 0
    TP = 0
    FN = 0
    FP = 0
    TN = 0
    for i, j in zip(prediction, ground_truth):
        if (i == j) and (i == 1):
            TP += 1
        if (i == j) and (i != 1):
            TN += 1
        if i != j:
            if i == 0:
                FN += 1
            else:
                FP += 1
    try:
        precision = TP/(TP + FP)
    except ZeroDivisionError:
        precision = 0
     
   
    
    recall = TP/(TP + FN)
    try:
        f1 = 2 * precision * recall / (precision + recall)
    except ZeroDivisionError:
        f1 = 0
        
    accuracy = (TP + TN)/(FP + FN + TP + TN)
    
    

    # TODO: implement metrics!
    # Some helpful links:
    # https://en.wikipedia.org/wiki/Precision_and_recall
    # https://en.wikipedia.org/wiki/F1_score
    
    return  precision, recall, f1, accuracy


def multiclass_accuracy(prediction, ground_truth):
    '''
    Computes metrics for multiclass classification

    Arguments:
    prediction, np array of int (num_samples) - model predictions
    ground_truth, np array of int (num_samples) - true labels

    Returns:
    accuracy - ratio of accurate predictions to total samples
    '''
    # TODO: Implement computing accuracy
    TP = 0
    FP = 0
    FN = 0
    total_TP = 0
    total_FN = 0
    total_FP = 0
    for i in ground_truth:
        for j, k in zip(ground_truth, prediction):
            if j == i and k == i:
                TP += 1
            elif j == i and k != i:
                FN += 1
            elif j != i and k == i:
                FP += 1 
        total_TP += TP
        total_FP += FP
        total_FN += FN
    recall = total_TP/(total_TP + total_FN)
    accuracy = recall
    return accuracy
