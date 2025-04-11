#Task 1:Data exploration and preprocessing

#1. loading dataset 

## Importing necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

## Loading dataset
df = pd.read_csv('./Datasets/creditCard.csv')

#printing first five rows
print(df.head())

#2.Check for missing values and handle them appropriately.

##checking for missing values
print("total number of null value in the dataset:")
print(df.isnull().sum())

##handling missing values
print("removing missing values")
df = df.dropna()
print("after removing missing values:")
print(df.isnull().sum())


##Split the dataset into training and testing sets.
# Import required libraries
from sklearn.model_selection import train_test_split

#feature selection
print("performing feature selection:")
#feature1:
x=df.drop(["Amount"], axis=1)

#feature2:
y=df["Class"]

#splitting the dataset into training and testing sets
print("splitting the dataset into training and testing sets")
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)


#TASK-2 Feature Selection and Engineering

#1.Perform correlation analysis to identify important features.

##import required libraries
import seaborn as sns
##correlation matrix
print("performing correlation analysis")
correlation_matrix = x.corr()
print(correlation_matrix)

##plotting the correlation matrix
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix,cmap='coolwarm', center=0)
plt.title('Correlation Matrix of Features')
plt.show()

#2.	Use feature selection techniques such as Recursive Feature Elimination (RFE).

##import required libraries
from sklearn.feature_selection import  RFE
from sklearn.linear_model import LogisticRegression

##feature selection using Recursive elimination 
print("performing feature selection using recursive elimination:")

#logistic regression model
model=LogisticRegression()

##recursive elimination
rfe=RFE(model,n_features_to_select=5)

##fitting the model 
rfe.fit(x_train,y_train)
##feature ranking 
print("feature ranking: ")
print(rfe.ranking_)

#question 3.Implement sampling techniques if necessary to handle class imbalance.

#TASK 3: Model Implementation
##logistic Regression

###importing required libraries
from sklearn.linear_model import LogisticRegression

##logistic regression model
model=LogisticRegression()

##fitting the model
model.fit(x_train,y_train)

##prediction
y_pred=model.predict(x_test)

##evaluation
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix

##accuracy score
accuracy=accuracy_score(y_test,y_pred)
print("accuracy of the logistic regression model:")
print(accuracy)

##classsification report of the logistic regression model
print("classification report of the logistic regression model:")
print(classification_report(y_test,y_pred))

##confusion matrix of the logistic regression model
print("confusion matric of the logistic regression model:")
print(confusion_matrix(y_test,y_pred))

# Naive Bayes

#importing libraries
from sklearn.naive_bayes import GaussianNB

##naive bayes model
naive_model=GaussianNB()

##fitting the model
naive_model.fit(x_train,y_train)

##prediction
naive_y_predict=naive_model.predict(x_test)
print("prediction of the naive bayes model:")
print(naive_y_predict)

##evaluation of the naive bayes model
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix

##accuracy score
accuracy=accuracy_score(y_test,naive_y_predict)
print("accuracy of the naive bayes model:")
print(accuracy)
##classification report
print("classification report of the naive bayes model:")
print(classification_report(y_test,naive_y_predict))

##confusion matrix of the naive bayes model
print("confusion matrix of the naive bayes model:")
print(confusion_matrix(y_test,naive_y_predict))

#TASK 4: Model Interpretation and Insights
#1. model comparision 
#importing libraries
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix

##accuracy score
print("accuracy score of the logistic regression model:")
print(accuracy_score(y_test,y_pred))

print("accuracy score of the naive regression model: ")
print(accuracy_score(y_test,naive_y_predict))

#2. Interpret results and provide insights based on findings.
#importing libraries
from sklearn.metrics import classification_report

##classification report
print("classification report of the logistic regression model:")
print(classification_report(y_test,y_pred))
















