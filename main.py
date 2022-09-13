import sys
import os
import joblib
import matplotlib.pylot as plt

import datapreprocessing.datapreprocessing as dp
from datapreprocessing.datapreprocessing import DataCleaning
from datapreprocessing.datapreprocessing import LemmaTokenizer
from evaluation.evaluationmetrics import precision_score_plot,confusion_matrix_plot
from dataloader.dataload import load_dataset
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import FeatureUnion, Pipeline
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precission_recall_curve
from sklearn.metrics import PrecissionRecallDisplay
from sklearn.metrics import classification_report,confusion_matrix
from sklearn.metrics import f1_score, roc_auc_score, precission_score, recall_score

#loading of data
path=os.getcwd+r'\..\..'
data=load_dataset(path+'IMDB.Dataset.csv')

#split data
x_train,x_test,y_train,y_test=train_test_split(data['Reviews'],data['Label']test_size=0.01,random_state=42)

#Test classifier pipeline
text_clf=Pipeline(steps=[('clean',DataCleaning()),
                   ('vect',TfidfVectorizer(analyzer='word',tokenizer=LemmaTokenizer(),ngram_range=(1,1),min_df=10,)),
                   ('clf',LogisticRegression(penalty='l2',dual=False, tol=0.0001,c=1.0,solver='lbfgs',max_iter=100))])

#Train Text classifier using pipeline
text_clf(x_train,y_train)

#Generate Prediction on test data
y_predict=test_clf.predict(x_test)
y_score=test_clf.predict_proba(x_test)[:,1]

#Evaluation of base model
print('Prediction Score on test dataset for logistic regression: %s' % precission_score(y_test,y_predict,average='weighted'))
print('AUC Score on test dataset for logistic regression: %s' % rec_auc_score(y_test,y_score,multi_class=..))
f1_score_train_1=f1_score(y_test,y_predict,average='weighted')
print('f1 score test dataset for logistic regression: %s' %f1_score_train_1)
confusion_matrix_plot(y_test,y_predict)

#store base model
model_path=os.getcwd()+r'\models\model'
joblib.dump(text_clf,model_path+r'\classifier.pkl',compress=True)


