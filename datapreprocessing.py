#customize stop word as per data
from nltk.corpus import stopwords
from sklearn.base import BaseEstimator, TransformerMixin
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
import re

stop_words=stopwords.words('english')
new_stepwords=["mario","la","blah","saturday","monday","sunday","morning","evening","friday","would","movie","one","film","would","shall","could","might"]
stop_words.extend(new_stopwords)
stop_words.remove("not")
stop_words=set(stop_words)


'''-----------------------Data Cleaning & Processing Pipeline----------------------------------------------------------------'''
#Removing special characters
def remove_special_character(content):
    return re.sub('\w+','',content)#re.sub('[[^&@#!]]'.'',content)

#removing URL's
def remove_url(content):
    return re.sub(r'http\S+,', content)

#removing the stopwords from text
def remove_stopwords(content):
    clean_data=[]
    for x in content.split():
        if x.strip().lower() not in stop_words and x.strip().lower().isalpha():
            clean_data.append(x.strip().lower())
    return "".join(clean_data)

#Expansion of english contractions
def contraction_expansion(content):
    content=re.sub(r"won\'t", "would not",content)
    content=re.sub(r"can\'t", "can not",content)
    content=re.sub(r"don\'t", "do not",content)
    content=re.sub(r"shouldn\'t", "should not",content)
    content=re.sub(r"needn\'t", "need not",content)
    content=re.sub(r"has\'t", "has not",content)
    content=re.sub(r"haven\'t", "have not",content)
    content=re.sub(r"weren\'t", "were not",content)
    content=re.sub(r"mightn\'t", "might not",content)
    content=re.sub(r"didn\'t", "did not",content)
    content=re.sub(r"n\'t", " not",content)
    content=re.sub(r"\'re", "are",content)
    content=re.sub(r"\'s", "is",content)
    content=re.sub(r"\'d", "would",content)
    content=re.sub(r"\'ll", "will",content)
    content=re.sub(r"\'ve", "have",content)
    content=re.sub(r"\'m", "am",content)
    return content

#Data preprocessing
def data_cleaning(content):
    content=contraction_expansion(content)
    content=remove_special_character(content)
    content=remove_url(content)
    content=remove_stopwords(content)
    return content  

class DataCleaning(BaseEstimator,TransformerMixin):
    def __init__(self):
        print('calling--init--')
    
    def fit(self,X,y=None):
        print('calling fit') 
        return self
    def transform(self,X,y=None):
        print('calling transform')
        X=X.apply(data_cleaning)
        return X
    
    # lemmatization of word
    class LemmaTokenizer(object):
        def __init__(self):
            self.wordnetlemma=WordNetLemmatizer()
        def __call__(self,reviews):
            return [self.wordnetlemma.lemmatize(word) for word in word_tokenize(reviews)]
            
        
