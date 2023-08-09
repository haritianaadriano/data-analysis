from Extract import extract_rates
from Extract import extract_datas
from S3Pusher import uploadToS3


def main():
    apps = extract_datas('googleplaystore.csv')
    reviews = extract_datas('googleplaystore_user_reviews.csv')
    rates = extract_rates(
        'https://v6.exchangerate-api.com/v6/85a67b762af150352ffb7e6a/latest/USD')

# name as 'data.csv' which is the name of this file in S3
# uploadToS3(name,'cleared_data.csv')


main()
