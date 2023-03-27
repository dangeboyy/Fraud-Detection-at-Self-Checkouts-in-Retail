#import csv
import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt

from sklearn.neighbors import KNeighborsClassifier,KNeighborsRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier


df = pd.read_csv('train.csv', delimiter='|')
x = np.array(df.iloc[:, 0:8])
y = np.array(df['fraud'])



total_accuracy_score = 0
total_confusion_matrix = [[0, 0], [0, 0]]
total_lost = 0

for i in range(100):
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
    model = GaussianNB().fit(x_train, y_train)
    pred = model.predict(x_test)
    current_accuracy_score = accuracy_score(pred, y_test)
    current_confusion_matrix = confusion_matrix(pred, y_test)

    lost = current_confusion_matrix[0][1] * -5 + current_confusion_matrix[1][0] * -25 + current_confusion_matrix[1][
        1] * 5
    total_lost += lost

    total_accuracy_score += current_accuracy_score

    for j in range(2):
        for k in range(2):
            total_confusion_matrix[j][k] += current_confusion_matrix[j][k]

for i in range(2):
    for j in range(2):
        total_confusion_matrix[i][j] /= 100

average_accuracy_score = total_accuracy_score / 100
average_lost = total_lost / 100
average_confusion_matrix = total_confusion_matrix
print('average_accuracy_score: ' + str(average_accuracy_score))
print('average_lost: ' + str(average_lost))
print('average_confusion_matrix: ', average_confusion_matrix)


def writeToFile(file_name, avg_accuracy, avg_lost, avg_confusion_matrix):
    with open(file_name + '.txt', 'w') as file:
        file.write(file_name + ' 100 times 0.3 train' + '\n')
        file.write('average_accuracy_score: ' + str(avg_accuracy) + '\n')
        file.write('average_lost: ' + str(avg_lost) + '\n')
        file.write('average_confusion_matrix:')
        for i in range(2):
            file.write('\n')
            for j in range(2):
                file.write(str(avg_confusion_matrix[i][j]) + ' ')


writeToFile('NaiveBayes', average_accuracy_score, average_lost, average_confusion_matrix)