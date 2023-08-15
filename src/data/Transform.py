import pandas as pd
from translate import Translator

# q_text = '季姬寂，集鸡，鸡即棘鸡。棘鸡饥叽，季姬及箕稷济鸡。'
# print(ts.translate_text(q_text))

##########################################################Googleplaystore##############################################
# 1. Find the count of category
def get_all_category(frame):
    return frame["Category"].unique()

# 3. Switch to the most repeted the NaN rating
# it's usefull because if the application don't have rating we set it by the most low rating
def change_to_no_rating(frame):
    frame["Rating"].fillna(0, inplace=True)

#TODO: some features will added like filter app by installs, price, and size

#####################################################Googleplaystoreuserreview#########################################
# Ensure that the Translated_Review don't have a NaN
def transform_review_user_dataframe(frame):
    frame["Translated_Review"].fillna(value="no review", inplace=True)

# 1. Translate all user language to english


# Apply the translate_to_english function to the "Translated_Review" column
def translate_to_english_user_dataframe(frame):
    frame["Translated_Review"].astype(str)
    frame["Review_translated"] = frame["Translated_Review"].map(translate_to_english)

# 2. Change NaN to no review in translated review
def change_the_NaN_user_dataframe(frame):
    frame["Sentiment"].fillna(frame["Sentiment"].mode()[0], inplace=True)
    frame["Sentiment_Polarity"].fillna(frame["Sentiment_Polarity"].median(), inplace=True)
    frame["Sentiment_Subjectivity"].fillna(frame["Sentiment_Subjectivity"].median(), inplace=True)

#####################################################Rates###############################################################

def add_user_sentiment(sentiment):
    return sentiment

def concatenate_playstore_userReview(frame,framereview):
    frame["User_sentiment_polarity"] = framereview.apply(lambda x: add_user_sentiment_polarity(x["Sentiment_Polarity"],framereview),axis=1)
    frame["User_sentiment_subjectivity"] = framereview.apply(lambda x: add_user_sentiment_subjectivity(x["Sentiment_Subjectivity"],framereview),axis=1)
    frame["User_sentiment"] = framereview["Sentiment"].apply(add_user_sentiment)
    frame["User_sentiment"].fillna(frame["User_sentiment"].mode()[0], inplace=True)

