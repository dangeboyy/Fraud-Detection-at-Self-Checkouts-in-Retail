from sklearn.svm import SVC

def svc_method(x_train,x_test, y_train):
    model = SVC(gamma='auto').fit(x_train, y_train)
    pred = model.predict(x_test)
    return pred
