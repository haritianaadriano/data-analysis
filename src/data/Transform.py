import pandas as pd
import numpy as np
import translators as ts



# q_text = '季姬寂，集鸡，鸡即棘鸡。棘鸡饥叽，季姬及箕稷济鸡。'
# print(ts.translate_text(q_text))

##########################################################Googleplaystore##############################################
# 1. importing the data and transform it to dataframe
dataframe = pd.read_csv("googleplaystore.csv")
pd.DataFrame(dataframe)
print(dataframe)

# 2. Transform all category to lowercase
def standardize_the_category(category):
    return str.lower(category)

dataframe["App"].apply(standardize_the_category)
print(dataframe)

# 3. Find the count of category
all_categories = dataframe["Category"].unique()
print(all_categories)

# 4. Switch to the most repeted the NaN rating
# it's usefull because if the application don't have rating we set it by the most low rating
dataframe["Rating"].fillna(0, inplace=True)

#TODO: some features will added like filter app by installs, price, and size

#####################################################Googleplaystoreuserreview#########################################
user_dataframe = pd.read_csv("googleplaystore_user_reviews.csv")
pd.DataFrame(user_dataframe)
print(user_dataframe)

# 1. Translate all user language to english
def translate_to_english(translated_review):
    return ts.translate_text(translate_to_english)

# user_dataframe["Translated_Review"].apply(translate_to_english)

# 2. Change NaN to no review in translated review
user_dataframe["Translated_Review"].fillna(value="no review", inplace=True)
user_dataframe["Sentiment"].fillna(user_dataframe["Sentiment"].mode()[0], inplace=True)
user_dataframe["Sentiment_Polarity"].fillna(user_dataframe["Sentiment_Polarity"].median(), inplace=True)
user_dataframe["Sentiment_Subjectivity"].fillna(user_dataframe["Sentiment_Subjectivity"].median(), inplace=True)
print(user_dataframe)