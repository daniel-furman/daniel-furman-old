#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 13:30:33 2020

@author: danielfurman
"""

# This file constructs classifiers for a species distribution (Xantusia
# vigilis). The classes are binary indicating presence or absence, and
# absences were randomly drawn from a 4x extent. The data were split
# into train/test sets in RStudio, where the extraction of BioClim
# features (1970-2000) was executed per presence/absence location. Here,
# we contrast the AUC, confusion  matrix, and the F statistic for 9 ML 
# classifiers. Random Forest proves best with an AUC of approximately .97
# and an F1 score of .94, with similar ensemble tree-based methods and a
# neural network falling just behind. 


# import libraries

import numpy as np
import random
from sklearn.metrics import confusion_matrix
from matplotlib import pyplot as plt
from sklearn.metrics import roc_curve, auc, f1_score
from sklearn.linear_model import LogisticRegression 
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.svm import SVC
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.neural_network import MLPClassifier
import pandas as pd

random.seed(1)

env_data = pd.read_csv('data-xant/envtrain_corr.csv')
class_type = env_data['pa']
env_data.head()

env_data1 = pd.read_csv('data-xant/testbackg_corr.csv')
env_data2 = pd.read_csv('data-xant/testpres_corr.csv')

env_data1.insert(0, 'pa', 0)
env_data2.insert(0, 'pa', 1)

env_data_test = pd.concat([env_data1, env_data2])

class_type_test = env_data_test['pa']
env_data = env_data.drop(['Unnamed: 0'], axis=1)
env_data = env_data.drop(['pa'], axis=1)

env_data_test = env_data_test.drop(['Unnamed: 0'], axis=1)
env_data_test = env_data_test.drop(['pa'], axis=1)

print('head validation features (length = 1282):\n\n', env_data_test.head())
 #validation set, 20 percent of the data
print('\nhead training features (length = 5125):\n\n', env_data.head())
 #train set, 80 percent of the data

import warnings
warnings.filterwarnings("ignore")

# create a dictionary of ML models, name -> (line format, classifier)
CLASS_MAP = {
'Random Forest':('-', RandomForestClassifier(oob_score=True)),
'Bagging':('--', BaggingClassifier(oob_score=True)),
'Ada Boosting':('--', AdaBoostClassifier()),
'Neural-net':('--', MLPClassifier(solver='adam')),
'QDA':('--', QuadraticDiscriminantAnalysis()),
'Naive Bayes': ('--', GaussianNB()),
'Logistic Regression':('--', LogisticRegression()),
'LDA':('--', LinearDiscriminantAnalysis()),
'SVM':('--', SVC(kernel = 'rbf',probability=True))
    }

training_data = env_data
training_class = class_type

validation_data = env_data_test
validation_class = class_type_test

frac_correct = np.zeros(len(CLASS_MAP))
i = 0 #iterator

# modeling loop over dictionary :

for name, (line_fmt, model) in CLASS_MAP.items():
    model.fit(training_data, training_class)
    # array w one col per label
    preds = model.predict_proba(validation_data)
    pred = pd.Series(preds[:,1])
    fpr, tpr, thresholds = roc_curve(validation_class, pred)
    auc_score = auc(fpr, tpr)
    label='%s: auc=%f' % (name, auc_score)
    plt.plot(fpr, tpr, line_fmt,
        linewidth=2, label=label)
    result = model.fit(training_data, training_class)
    # if desired, assess oob scores for select models
    if hasattr(result, 'oob_score_') == True :
        result.oob_score_
    #if desired, assess feature importance for select models
    if hasattr(result, 'feature_importances_') == True :
        #print('feature_importances',result.feature_importances_)
        feat = np.zeros([1,10])
        feat[0,:] = (result.feature_importances_)
        feat_pd = pd.DataFrame(feat)
        feat_pd.columns = ["bclim12", "bclim14", "bclim15" ,"bclim18",
                           "bclim19" ,"bclim3" , "bclim6" , "bclim7" ,
                           "bclim8" , "bclim9" ]
        #print(feat_pd)
    #compute confusion matrix and F1 stat    
    predicted_class_type = model.predict(validation_data)
    print('\n\nFraction correct ' + name +' :' ,
          np.sum(predicted_class_type == validation_class)
              / len(validation_class))
    cnf_matrix_test = confusion_matrix(validation_class, predicted_class_type)
    print(cnf_matrix_test)
    frac_correct[i] = np.sum(predicted_class_type ==
                             validation_class)/len(validation_class)
    i =+ (i + 1)
    print('The F1 score is : ',
          f1_score(validation_class, predicted_class_type))

# annotate AUC Plot     
plt.legend(loc="lower right") 
plt.title('Comparing Classifiers')
#plt.plot([0, 1], [0, 1], 'k--') #x=y line. Visual aid plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate') 
#plt.savefig('images-xant/auc.png', dpi = 300)
plt.show()

