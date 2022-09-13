## 1. Data Overview:
    Data Source: https://www.kaggle.com/datasets/crisbam/imdb-dataset-of-65k-movie-reviews-and-translation
    
    Basic statics of data:
 - IMDB review dataset has four columns; Ratings, Reviews, Movies, Resenhas
 - Number of Reviews: 149780
 - Number of Movies:14205
 
   Attribute Information:
1. Review: User review in English language
2. Ratings: Rating btw 1 to 10
3. Movies:Movie names
4. Resenhas:User review translation in Portuguese Language

## 2. Objective
Usually such dataset provides a solid foundation for sentiment analysis. 
  
  Goal: Aim is to use the rating, review attribute to divelop a           sentimizer analyzer to categoze review either positive or         negative.
  
  This will be achieved through:
  1. Map ratings(1-10) to binary classes
  2. Solving the challenges related ti sentiment analyzer:sarcasm, multi polarity and negation.
  3. Develop NLP & Ml model to categorize english text reviews either positive or negative.
  4. Deploy Sentiment Analyzer model on AWS cloud by using rest API

## 3. Problem statement
The task of this project is to find the subjective sentiment of the raters using NLP based model.The outcome of the modelling would either be a positive or a negative binary class. However, we know that rating is btw 1 to 10, therefore there is need to convert this problem into binary class text classification problem.

We need to map 'ratings ranges' to binary classes as follows;
    1-4: Negative
    5-6: Neutral(**We can ignore this to match our binary class classification**
    7-10: Positive

## 4. final outcome
Our outcome would either be the rater either likes(positive) or doesn't like (negative).


## 5. Possible Challenges
1. Interpretation of sarcasm:
Sometimes users can provide a negative response to mean positive.A simple model would easily be fooled by such sarcasm. Therefore there is the need to design one that would be able to detect one.

2. Issue of polarity:
Sometimes the raters may provide a multipolarity review. This would bev  hard for a traditional sentiment analyzer. Hence, we need t design a sentiment analyzer that could bypass multipolarity reviews. 
   e.g
   the movie is not good but i like its background music.

3. Issue of negation:
The use of words like non,less,not,cannot ect may reverse the polarity of a word. It would be a golden buzzer if our machine could manouver around this.
      e.g
      I can't say it is a nice movie.
   
