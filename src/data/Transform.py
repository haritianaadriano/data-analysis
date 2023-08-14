import pandas as pd
from translate import Translator

# q_text = '季姬寂，集鸡，鸡即棘鸡。棘鸡饥叽，季姬及箕稷济鸡。'
# print(ts.translate_text(q_text))

##########################################################Googleplaystore##############################################
# 1. importing the data and transform it to dataframe
dataframe = pd.read_csv("googleplaystore.csv")
pd.DataFrame(dataframe)

# 2. Transform all category to lowercase
def standardize_the_category(category):
    dataframe["App"].apply(standardize_the_category)
    return str.lower(category)

# 3. Find the count of category
def get_all_category():
    return dataframe["Category"].unique()
    

# 4. Switch to the most repeted the NaN rating
# it's usefull because if the application don't have rating we set it by the most low rating
def change_to_no_rating():
    dataframe["Rating"].fillna(0, inplace=True)

#TODO: some features will added like filter app by installs, price, and size

#####################################################Googleplaystoreuserreview#########################################
user_dataframe = pd.read_csv("googleplaystore_user_reviews.csv")
pd.DataFrame(user_dataframe)

# Ensure that the Translated_Review don't have a NaN
def transform_review_user_dataframe():
    user_dataframe["Translated_Review"].fillna(value="no review", inplace=True)

# 1. Translate all user language to english
def translate_to_english_user_dataframe(text):
    # Assuming ts.translate_text() is the function to translate text to English
    translator = Translator(to_lang="en")
    translated_text = translator.translate(text)
    return translated_text

# Apply the translate_to_english function to the "Translated_Review" column
def translate_to_english_user_dataframe():
    user_dataframe["Translated_Review"].astype(str)
    user_dataframe["Review_translated"] = user_dataframe["Translated_Review"].map(translate_to_english)

# 2. Change NaN to no review in translated review
def change_the_NaN_user_dataframe():
    user_dataframe["Sentiment"].fillna(user_dataframe["Sentiment"].mode()[0], inplace=True)
    user_dataframe["Sentiment_Polarity"].fillna(user_dataframe["Sentiment_Polarity"].median(), inplace=True)
    user_dataframe["Sentiment_Subjectivity"].fillna(user_dataframe["Sentiment_Subjectivity"].median(), inplace=True)

#####################################################Rates###############################################################
user_sentiment = user_dataframe.groupby("App")[["Sentiment_Polarity", "Sentiment_Subjectivity"]].median()
user_sentiment["Sentiment_Polarity"].fillna(0, inplace=True)
user_sentiment["Sentiment_Subjectivity"].fillna(0, inplace=True)

user_sentiment_polarity_mean = user_sentiment["Sentiment_Polarity"].mean()
user_sentiment_subjectivity_mean = user_sentiment["Sentiment_Subjectivity"].mean()

def add_user_sentiment_polarity(sentiment_purcentage):
    if(sentiment_purcentage > user_sentiment_polarity_mean):
        return "Good"
    else:
        return "Bad"
    
def add_user_sentiment_subjectivity(sentiment_purcentage):
    if(sentiment_purcentage > user_sentiment_subjectivity_mean):
        return "Good"
    else:
        return "Bad"
    
def add_user_sentiment(sentiment):
    return sentiment

def concatenate_playstore_userReview():
    dataframe["User_sentiment_polarity"] = user_dataframe["Sentiment_Polarity"].apply(add_user_sentiment_polarity)
    dataframe["User_sentiment_subjectivity"] = user_dataframe["Sentiment_Subjectivity"].apply(add_user_sentiment_subjectivity)
    dataframe["User_sentiment"] = user_dataframe["Sentiment"].apply(add_user_sentiment)
    dataframe["User_sentiment"].fillna(dataframe["User_sentiment"].mode()[0], inplace=True)

print(dataframe)