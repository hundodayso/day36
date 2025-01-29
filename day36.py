import key
import requests
import pprint
import json
from twilio.rest import Client
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_API_KEY = key.stock_api
account_sid = key.account_sid
auth_token = key.auth_token

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# stock_params = {
#     'function': 'TIME_SERIES_DAILY',
#     'symbol': STOCK,
#     'apikey': STOCK_API_KEY,
# }
#
# stock_url = 'https://www.alphavantage.co/query?'
# response = requests.get(stock_url,stock_params)
# if response.status_code == 200:
#     data = response.json()
#     print(data)
#
# else:
#     print("No response from server")

data = {'Meta Data': {'1. Information': 'Daily Prices (open, high, low, close) and Volumes', '2. Symbol': 'TSLA', '3. Last Refreshed': '2025-01-24', '4. Output Size': 'Compact', '5. Time Zone': 'US/Eastern'}, 'Time Series (Daily)': {'2025-01-24': {'1. open': '414.4500', '2. high': '418.8800', '3. low': '405.7800', '4. close': '406.5800', '5. volume': '56427149'}, '2025-01-23': {'1. open': '416.0600', '2. high': '420.7300', '3. low': '408.9500', '4. close': '412.3800', '5. volume': '50690592'}, '2025-01-22': {'1. open': '416.8100', '2. high': '428.0000', '3. low': '414.5900', '4. close': '415.1100', '5. volume': '60963342'}, '2025-01-21': {'1. open': '432.6400', '2. high': '433.2000', '3. low': '406.3100', '4. close': '424.0700', '5. volume': '87320894'}, '2025-01-17': {'1. open': '421.5000', '2. high': '439.7400', '3. low': '419.7500', '4. close': '426.5000', '5. volume': '94991429'}, '2025-01-16': {'1. open': '423.4900', '2. high': '424.0000', '3. low': '409.1300', '4. close': '413.8200', '5. volume': '68335151'}, '2025-01-15': {'1. open': '409.9000', '2. high': '429.8000', '3. low': '405.6610', '4. close': '428.2200', '5. volume': '81375460'}, '2025-01-14': {'1. open': '414.3400', '2. high': '422.6400', '3. low': '394.5400', '4. close': '396.3600', '5. volume': '84565022'}, '2025-01-13': {'1. open': '383.2100', '2. high': '403.7900', '3. low': '380.0700', '4. close': '403.3100', '5. volume': '67580494'}, '2025-01-10': {'1. open': '391.4000', '2. high': '399.2800', '3. low': '377.2900', '4. close': '394.7400', '5. volume': '62287333'}, '2025-01-08': {'1. open': '392.9500', '2. high': '402.4999', '3. low': '387.4000', '4. close': '394.9400', '5. volume': '73038805'}, '2025-01-07': {'1. open': '405.8300', '2. high': '414.3300', '3. low': '390.0000', '4. close': '394.3600', '5. volume': '75699525'}, '2025-01-06': {'1. open': '423.2000', '2. high': '426.4300', '3. low': '401.7000', '4. close': '411.0500', '5. volume': '85516534'}, '2025-01-03': {'1. open': '381.4800', '2. high': '411.8799', '3. low': '379.4500', '4. close': '410.4400', '5. volume': '95423329'}, '2025-01-02': {'1. open': '390.1000', '2. high': '392.7299', '3. low': '373.0400', '4. close': '379.2800', '5. volume': '109710749'}, '2024-12-31': {'1. open': '423.7900', '2. high': '427.9300', '3. low': '402.5400', '4. close': '403.8400', '5. volume': '76825121'}, '2024-12-30': {'1. open': '419.4000', '2. high': '427.0000', '3. low': '415.7500', '4. close': '417.4100', '5. volume': '64941012'}, '2024-12-27': {'1. open': '449.5200', '2. high': '450.0000', '3. low': '426.5000', '4. close': '431.6600', '5. volume': '82666821'}, '2024-12-26': {'1. open': '465.1600', '2. high': '465.3299', '3. low': '451.0200', '4. close': '454.1300', '5. volume': '76651210'}, '2024-12-24': {'1. open': '435.9000', '2. high': '462.7800', '3. low': '435.1400', '4. close': '462.2800', '5. volume': '59551750'}, '2024-12-23': {'1. open': '431.0000', '2. high': '434.5100', '3. low': '415.4112', '4. close': '430.6000', '5. volume': '72698055'}, '2024-12-20': {'1. open': '425.5050', '2. high': '447.0800', '3. low': '417.6400', '4. close': '421.0600', '5. volume': '132216176'}, '2024-12-19': {'1. open': '451.8800', '2. high': '456.3600', '3. low': '420.0200', '4. close': '436.1700', '5. volume': '118566146'}, '2024-12-18': {'1. open': '466.4950', '2. high': '488.5399', '3. low': '427.0100', '4. close': '440.1300', '5. volume': '149340788'}, '2024-12-17': {'1. open': '475.9000', '2. high': '483.9900', '3. low': '457.5101', '4. close': '479.8600', '5. volume': '131222978'}, '2024-12-16': {'1. open': '441.0900', '2. high': '463.1900', '3. low': '436.1500', '4. close': '463.0200', '5. volume': '114083811'}, '2024-12-13': {'1. open': '420.0000', '2. high': '436.3000', '3. low': '415.7100', '4. close': '436.2300', '5. volume': '89000158'}, '2024-12-12': {'1. open': '424.8400', '2. high': '429.3000', '3. low': '415.0000', '4. close': '418.1000', '5. volume': '87752225'}, '2024-12-11': {'1. open': '409.7000', '2. high': '424.8800', '3. low': '402.3800', '4. close': '424.7700', '5. volume': '104287559'}, '2024-12-10': {'1. open': '392.6800', '2. high': '409.7300', '3. low': '390.8500', '4. close': '400.9900', '5. volume': '97563578'}, '2024-12-09': {'1. open': '397.6100', '2. high': '404.8000', '3. low': '378.0100', '4. close': '389.7900', '5. volume': '96359173'}, '2024-12-06': {'1. open': '377.4200', '2. high': '389.4900', '3. low': '370.8000', '4. close': '389.2200', '5. volume': '81455834'}, '2024-12-05': {'1. open': '359.8700', '2. high': '375.4300', '3. low': '359.5000', '4. close': '369.4900', '5. volume': '81403569'}, '2024-12-04': {'1. open': '353.0000', '2. high': '358.1000', '3. low': '348.6000', '4. close': '357.9300', '5. volume': '50810874'}, '2024-12-03': {'1. open': '351.8000', '2. high': '355.6900', '3. low': '348.2000', '4. close': '351.4200', '5. volume': '58267196'}, '2024-12-02': {'1. open': '352.3800', '2. high': '360.0000', '3. low': '351.1501', '4. close': '357.0900', '5. volume': '77986478'}, '2024-11-29': {'1. open': '336.0800', '2. high': '345.4500', '3. low': '334.6500', '4. close': '345.1600', '5. volume': '37167621'}, '2024-11-27': {'1. open': '341.8000', '2. high': '342.5500', '3. low': '326.5900', '4. close': '332.8900', '5. volume': '57896439'}, '2024-11-26': {'1. open': '341.0000', '2. high': '346.9600', '3. low': '335.6600', '4. close': '338.2300', '5. volume': '62295857'}, '2024-11-25': {'1. open': '360.1400', '2. high': '361.9300', '3. low': '338.2000', '4. close': '338.5900', '5. volume': '95890899'}, '2024-11-22': {'1. open': '341.0850', '2. high': '361.5300', '3. low': '337.7000', '4. close': '352.5600', '5. volume': '89140722'}, '2024-11-21': {'1. open': '343.8100', '2. high': '347.9899', '3. low': '335.2800', '4. close': '339.6400', '5. volume': '58011719'}, '2024-11-20': {'1. open': '345.0000', '2. high': '346.5999', '3. low': '334.3000', '4. close': '342.0300', '5. volume': '66340650'}, '2024-11-19': {'1. open': '335.7600', '2. high': '347.3799', '3. low': '332.7500', '4. close': '346.0000', '5. volume': '88852452'}, '2024-11-18': {'1. open': '340.7300', '2. high': '348.5499', '3. low': '330.0100', '4. close': '338.7400', '5. volume': '126547455'}, '2024-11-15': {'1. open': '310.5700', '2. high': '324.6799', '3. low': '309.2200', '4. close': '320.7200', '5. volume': '114440286'}, '2024-11-14': {'1. open': '327.6900', '2. high': '329.9800', '3. low': '310.3700', '4. close': '311.1800', '5. volume': '120726109'}, '2024-11-13': {'1. open': '335.8500', '2. high': '344.5999', '3. low': '322.5000', '4. close': '330.2400', '5. volume': '125405599'}, '2024-11-12': {'1. open': '342.7400', '2. high': '345.8400', '3. low': '323.3100', '4. close': '328.4900', '5. volume': '155726016'}, '2024-11-11': {'1. open': '346.3000', '2. high': '358.6400', '3. low': '336.0000', '4. close': '350.0000', '5. volume': '210521625'}, '2024-11-08': {'1. open': '299.1400', '2. high': '328.7100', '3. low': '297.6600', '4. close': '321.2200', '5. volume': '204782763'}, '2024-11-07': {'1. open': '288.8900', '2. high': '299.7500', '3. low': '285.5200', '4. close': '296.9100', '5. volume': '117309232'}, '2024-11-06': {'1. open': '284.6700', '2. high': '289.5900', '3. low': '275.6200', '4. close': '288.5300', '5. volume': '165228710'}, '2024-11-05': {'1. open': '247.3400', '2. high': '255.2799', '3. low': '246.2101', '4. close': '251.4400', '5. volume': '69282505'}, '2024-11-04': {'1. open': '244.5600', '2. high': '248.9000', '3. low': '238.8800', '4. close': '242.8400', '5. volume': '68802354'}, '2024-11-01': {'1. open': '252.0430', '2. high': '254.0000', '3. low': '246.6300', '4. close': '248.9800', '5. volume': '57544757'}, '2024-10-31': {'1. open': '257.9900', '2. high': '259.7500', '3. low': '249.2500', '4. close': '249.8500', '5. volume': '66575292'}, '2024-10-30': {'1. open': '258.0350', '2. high': '263.3500', '3. low': '255.8201', '4. close': '257.5500', '5. volume': '53993576'}, '2024-10-29': {'1. open': '264.5100', '2. high': '264.9800', '3. low': '255.5100', '4. close': '259.5200', '5. volume': '80521751'}, '2024-10-28': {'1. open': '270.0000', '2. high': '273.5360', '3. low': '262.2400', '4. close': '262.5100', '5. volume': '107653603'}, '2024-10-25': {'1. open': '256.0100', '2. high': '269.4900', '3. low': '255.3200', '4. close': '269.1900', '5. volume': '161611931'}, '2024-10-24': {'1. open': '244.6800', '2. high': '262.1199', '3. low': '242.6500', '4. close': '260.4800', '5. volume': '204491903'}, '2024-10-23': {'1. open': '217.1250', '2. high': '218.7200', '3. low': '212.1100', '4. close': '213.6500', '5. volume': '80938892'}, '2024-10-22': {'1. open': '217.3100', '2. high': '218.2200', '3. low': '215.2600', '4. close': '217.9700', '5. volume': '43268741'}, '2024-10-21': {'1. open': '218.9000', '2. high': '220.4800', '3. low': '215.7260', '4. close': '218.8500', '5. volume': '47328988'}, '2024-10-18': {'1. open': '220.7100', '2. high': '222.2800', '3. low': '219.2300', '4. close': '220.7000', '5. volume': '49611867'}, '2024-10-17': {'1. open': '221.5900', '2. high': '222.0800', '3. low': '217.9000', '4. close': '220.8900', '5. volume': '50791784'}, '2024-10-16': {'1. open': '221.4000', '2. high': '222.8199', '3. low': '218.9300', '4. close': '221.3300', '5. volume': '49632824'}, '2024-10-15': {'1. open': '220.0100', '2. high': '224.2600', '3. low': '217.1200', '4. close': '219.5700', '5. volume': '62988787'}, '2024-10-14': {'1. open': '220.1300', '2. high': '221.9100', '3. low': '213.7400', '4. close': '219.1600', '5. volume': '86291923'}, '2024-10-11': {'1. open': '220.1300', '2. high': '223.3400', '3. low': '214.3800', '4. close': '217.8000', '5. volume': '142628874'}, '2024-10-10': {'1. open': '241.8100', '2. high': '242.7899', '3. low': '232.3400', '4. close': '238.7700', '5. volume': '83087063'}, '2024-10-09': {'1. open': '243.8200', '2. high': '247.4300', '3. low': '239.5100', '4. close': '241.0500', '5. volume': '66289529'}, '2024-10-08': {'1. open': '243.5600', '2. high': '246.2100', '3. low': '240.5600', '4. close': '244.5000', '5. volume': '56303160'}, '2024-10-07': {'1. open': '249.0000', '2. high': '249.8300', '3. low': '240.7000', '4. close': '240.8300', '5. volume': '68113270'}, '2024-10-04': {'1. open': '246.6900', '2. high': '250.9600', '3. low': '244.5800', '4. close': '250.0800', '5. volume': '86726285'}, '2024-10-03': {'1. open': '244.4800', '2. high': '249.7900', '3. low': '237.8100', '4. close': '240.6600', '5. volume': '80729240'}, '2024-10-02': {'1. open': '247.5500', '2. high': '251.1585', '3. low': '241.5000', '4. close': '249.0200', '5. volume': '93983930'}, '2024-10-01': {'1. open': '262.6700', '2. high': '263.9800', '3. low': '248.5300', '4. close': '258.0200', '5. volume': '87397613'}, '2024-09-30': {'1. open': '259.0400', '2. high': '264.8600', '3. low': '255.7700', '4. close': '261.6300', '5. volume': '80873381'}, '2024-09-27': {'1. open': '257.3750', '2. high': '260.6999', '3. low': '254.1200', '4. close': '260.4600', '5. volume': '70988067'}, '2024-09-26': {'1. open': '260.6000', '2. high': '261.7500', '3. low': '251.5300', '4. close': '254.2200', '5. volume': '67142193'}, '2024-09-25': {'1. open': '252.5400', '2. high': '257.0500', '3. low': '252.2800', '4. close': '257.0200', '5. volume': '65034318'}, '2024-09-24': {'1. open': '254.0800', '2. high': '257.1900', '3. low': '249.0501', '4. close': '254.2700', '5. volume': '88490999'}, '2024-09-23': {'1. open': '242.6100', '2. high': '250.0000', '3. low': '241.9200', '4. close': '250.0000', '5. volume': '86927194'}, '2024-09-20': {'1. open': '241.5200', '2. high': '243.9900', '3. low': '235.9200', '4. close': '238.2500', '5. volume': '99879070'}, '2024-09-19': {'1. open': '234.0000', '2. high': '244.2400', '3. low': '232.1300', '4. close': '243.9200', '5. volume': '102694576'}, '2024-09-18': {'1. open': '230.0900', '2. high': '235.6800', '3. low': '226.8800', '4. close': '227.2000', '5. volume': '78010204'}, '2024-09-17': {'1. open': '229.4500', '2. high': '234.5700', '3. low': '226.5533', '4. close': '227.8700', '5. volume': '66761636'}, '2024-09-16': {'1. open': '229.3000', '2. high': '229.9600', '3. low': '223.5300', '4. close': '226.7800', '5. volume': '54322995'}, '2024-09-13': {'1. open': '228.0000', '2. high': '232.6700', '3. low': '226.3200', '4. close': '230.2900', '5. volume': '59515114'}, '2024-09-12': {'1. open': '224.6600', '2. high': '231.4500', '3. low': '223.8300', '4. close': '229.8100', '5. volume': '72020042'}, '2024-09-11': {'1. open': '224.5500', '2. high': '228.4700', '3. low': '216.8003', '4. close': '228.1300', '5. volume': '83548633'}, '2024-09-10': {'1. open': '220.0700', '2. high': '226.4000', '3. low': '218.6377', '4. close': '226.1700', '5. volume': '78891136'}, '2024-09-09': {'1. open': '216.2000', '2. high': '219.8700', '3. low': '213.6700', '4. close': '216.2700', '5. volume': '67443518'}, '2024-09-06': {'1. open': '232.6000', '2. high': '233.6000', '3. low': '210.5100', '4. close': '210.7300', '5. volume': '112177004'}, '2024-09-05': {'1. open': '223.4900', '2. high': '235.0000', '3. low': '222.2500', '4. close': '230.1700', '5. volume': '119355013'}, '2024-09-04': {'1. open': '210.5900', '2. high': '222.2200', '3. low': '210.5700', '4. close': '219.4100', '5. volume': '80217329'}, '2024-09-03': {'1. open': '215.2600', '2. high': '219.9043', '3. low': '209.6400', '4. close': '210.6000', '5. volume': '76714222'}, '2024-08-30': {'1. open': '208.6300', '2. high': '214.5701', '3. low': '207.0300', '4. close': '214.1100', '5. volume': '63370608'}}}

#print(data)

time_series = list(data['Time Series (Daily)'].values())
print()
day1_close = float(time_series[0]['4. close'])
print(f'{day1_close= }')
day2_close = float(time_series[1]['4. close'])
print(f'{day2_close= }')

change_pct = 100 - ((day2_close / day1_close) * 100)
abs_change_pct = abs(change_pct)
print(f'{change_pct= }')
print(f'{abs_change_pct= }')


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
if abs_change_pct >= 1:
    # news_params = {
    #     'q': COMPANY_NAME,
    #     'searchIn': 'title'
    #     'pageSize': '3',
    #     'sortBy':'publishedAt',
    #     'apikey': key.news_api
    # }
    #
    # news_url = "https://newsapi.org/v2/everything?"
    #
    # news_response = requests.get(news_url, news_params)
    # print(news_response.json())
    #
    # news_articles = list(news_response.json()['articles'])

    print("Get News")
    news_response = {'status': 'ok', 'totalResults': 910, 'articles': [{'source': {'id': None, 'name': 'Motley Fool Australia'}, 'author': 'Bronwyn Allen', 'title': "Here's how the ASX 200 market sectors stacked up last week", 'description': "ASX technology shares led the market with a 3.23% increase while the ASX 200 lifted 0.98% last week. \nThe post Here's how the ASX 200 market sectors stacked up last week appeared first on The Motley Fool Australia.", 'url': 'https://www.fool.com.au/2025/01/26/heres-how-the-asx-200-market-sectors-stacked-up-last-week-4-2025/', 'urlToImage': 'https://www.fool.com.au/wp-content/uploads/2022/02/cyber-1200x675.jpg', 'publishedAt': '2025-01-25T21:00:00Z', 'content': 'Tech shares\xa0led the ASX 200 market sectors\xa0with a 3.23% uplift over the five trading days.\r\nMeanwhile, the S&amp;P/ASX 200 Index\xa0(ASX: XJO) rose 0.98% to finish at 8,408.9 points on Friday.\r\nThe worl… [+3317 chars]'}, {'source': {'id': None, 'name': 'Securityaffairs.com'}, 'author': 'Pierluigi Paganini', 'title': 'Subaru Starlink flaw allowed experts to remotely hack cars', 'description': 'Subaru Starlink flaw exposed vehicles and customer accounts in the US, Canada, and Japan to remote attacks. Popular security researcher Sam Curry and he colleague Shubham Shah discovered a vulnerability in Subaru’s Starlink connected vehicle service that expo…', 'url': 'https://securityaffairs.com/173434/security/subaru-starlink-vulnerability-remote-attacks.html', 'urlToImage': 'https://securityaffairs.com/wp-content/uploads/2025/01/image-40.png', 'publishedAt': '2025-01-25T19:26:30Z', 'content': 'Subaru Starlink flaw allowed experts to remotely hack cars\r\n\xa0|\xa0U.S. CISA adds SonicWall SMA1000 flaw to its Known Exploited Vulnerabilities catalog\r\n\xa0|\xa0J-magic malware campaign targets Juniper router… [+133845 chars]'}, {'source': {'id': 'financial-post', 'name': 'Financial Post'}, 'author': 'Bloomberg News', 'title': 'Stocks Are Jumping on Earnings Wins by the Most Since 2018', 'description': 'With uncertainty swirling around the outlook for inflation and interest rates, there’s been one dependable catalyst keeping Wall Street’s spirits lifted: Corporate America’s bottom line.', 'url': 'https://financialpost.com/pmn/business-pmn/stocks-are-jumping-on-earnings-wins-by-the-most-since-2018', 'urlToImage': 'https://smartcdn.gprod.postmedia.digital/financialpost/wp-content/uploads/2025/01/profit-revisions-for-sp-500-companies-slump-analysts-lowere.jpg', 'publishedAt': '2025-01-25T17:28:01Z', 'content': 'With uncertainty swirling around the outlook for inflation and interest rates, theres been one dependable catalyst keeping Wall Streets spirits lifted: Corporate Americas bottom line.\r\nAuthor of the … [+9570 chars]'}]}
    news_articles = list(news_response['articles'])
    if change_pct > 0:
        text = f"*TSLA: 🔺{round(abs_change_pct,2)}%* \n\n"
    elif change_pct < 0:
        text = f"*TSLA: 🔻{round(abs_change_pct,2)}%* \n\n"

    for article in news_articles:
        headline = article['title']
        brief = article['description']
        # print(f'{headline= }')
        # print(f'{brief= }')
        text += f'*Headline*: {headline} \n*Brief*: {brief}\n\n'
    print(text)

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
    client = Client(account_sid, auth_token)
    #print("leng")

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=text,
        to='whatsapp:+447860779613'
    )
print(message.sid)
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

