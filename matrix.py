def my_plot_confusion_matrix(test_loader, model):
    '''
    Attributes
    -------------------------
    test_loader:

    model:

    Parameters
    --------------------------
    y_true: list
        true labels

    y_pred: list
        predicted labels

    tp: int
        True Positive values

    tn: int
        True Negative values

    fp: int
        False Positive values

    fn: int
        False Negative values

        ACTUAL
         1  0
   P  1 TP FP
   R  0 FN TN
   E
   D


    Returns
    tp, fp, fn, tn : int
    ------------------------------

    '''
    y_pred = []
    y_true = []

    # iterate over test data
    for inputs, labels in test_loader:
            inputs = inputs.to(device)
            labels = labels.to(device)
            output = model(inputs) # Feed Network

            output = (torch.max(torch.exp(output), 1)[1]).data.cpu().numpy()
            #print(output)
            y_pred.extend(output) # Save Prediction

            labels = labels.data.cpu().numpy()
            y_true.extend(labels) # Save Truth



    tp=0
    tn=0
    fp=0
    fn=0

    for el1, el2 in zip(y_true,y_pred):
        if el1 == el2 and el1 == 1:
            tp += 1
        elif  el1 == el2 and el1 == 0:
            tn += 1
        elif el1 == 1 and el1 != el2:
            fn += 1
        elif el1 == 0 and el1 != el2:
            fp += 1


    conf_matrix = np.array((tn, fn, fp, tp))
    conf_matrix = conf_matrix.reshape((2,2)) # bad shape ale dobry wychodzi w matplotlib xd (fuszera)
    #print(conf_matrix)

    len_dataset = np.sum(conf_matrix)
    fig, ax = plt.subplots(figsize=(7.5, 7.5))
    ax.matshow(conf_matrix, cmap=plt.cm.Blues, alpha=0.3)
    for i in range(conf_matrix.shape[0]):
        for j in range(conf_matrix.shape[1]):
            percentage = round((conf_matrix[i, j]/len_dataset)*100,2)
            text = f'''{conf_matrix[i, j]} val
{percentage} %'''
            ax.text(x=j, y=i,s=text, va='center', ha='center', size='xx-large')
    ax.invert_xaxis()
    ax.invert_yaxis()
    plt.xlabel('Confusion Matrix', fontsize=18)
    plt.ylabel('Predictions', fontsize=18)
    plt.title('Actual', fontsize=18)
    plt.show()
    
