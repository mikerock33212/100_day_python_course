import requests
import os
import datetime as dt
import ssl
import smtplib as sp

now = dt.datetime.now()
today = now.date().strftime('%Y-%m-%d')

alpha_vantage_api_key = 'S8DZ7Q878IBOUGI4'
news_api_key = '4e9105b8257c484f9c679a5a458fef2f'
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").


def generate_news(company_name):
    news_params = {
        'q': company_name,
        'from': today,
        'sortBy': 'popularity',
        'language': 'en',
        'apiKey': news_api_key
    }
    response_1 = requests.get('https://newsapi.org/v2/everything', news_params)
    response_1.raise_for_status()
    news_data = response_1.json()['articles'][0:3]
    final_results = []
    for i in news_data:
        final_results.append(i['title'])
        final_results.append(i['description'])
        final_results.append(i['url'])
    return final_results


def check_stock_price(stock, difference):
    stock_param = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': stock,
        'apikey': alpha_vantage_api_key
    }
    response = requests.get('https://www.alphavantage.co/query', stock_param)
    response.raise_for_status()
    stock_data = response.json()
    daily_stock_price = stock_data['Time Series (Daily)']
    daily_price_list = list(daily_stock_price.items())
    day = float(daily_price_list[0][1]['4. close'])
    day_before = float(daily_price_list[1][1]['4. close'])
    if (day - day_before) / day_before >= difference * 1:
        return 1
    elif (day - day_before) / day_before <= difference * -1:
        return 2
    # for index in range(len(daily_price_list) - 1):
    #     day = float(daily_price_list[index][1]['4. close'])
    #     day_before = float(daily_price_list[index + 1][1]['4. close'])
    #     if (day - day_before) / day_before >= 0.05:
    #         print('Stock increased over 5%', day, day_before)
    #     elif (day - day_before) / day_before <= -0.05:
    #         print('Stock decreased over 5%', day, day_before)

def send_email(address):
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "mikerock332@gmail.com"
    password = 'Zrz1409197'
    news = generate_news(COMPANY_NAME)

    message = f"""Subject: Today's news for {COMPANY_NAME}!\n\n
    {news}"\n
    """
    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to server and send email
    try:
        server = sp.SMTP(smtp_server, port)
        server.ehlo()  # Can be omitted
        server.starttls(context=context)  # Secure the connection
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        # TODO: Send email here
        server.sendmail(sender_email, address, f'{message}')
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    else:
        server.quit()
        print('Email sent!')

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


# if check_stock_price(STOCK, 0.01) == 1:
#     print('To the Moon!')
# elif check_stock_price(STOCK, 0.01) == 2:
#     print('Down the earth!')
send_email('r.zhao@stompy.io')

# stock_param = {
#         'function': 'TIME_SERIES_DAILY',
#         'symbol': STOCK,
#         'apikey': alpha_vantage_api_key
#     }
# response = requests.get('https://www.alphavantage.co/query', stock_param)
# response.raise_for_status()
# stock_data = response.json()
# daily_stock_price = stock_data['Time Series (Daily)']
# print(daily_stock_price)




#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

