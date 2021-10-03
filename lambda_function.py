import requests
import smtplib
import datetime

frommail = 'SENDING EMAIL ADDRESS'
passwd = 'PASSWORD'
tomail = 'RECIPIENT EMAIL ADDRESS'

def lambda_handler(event,context):

    url = 'https://www.opendata.nhs.scot/api/3/action/datastore_search?resource_id=7fad90e5-6f19-455b-bc07-694a22f8d5dc'
    r = requests.get(url)
    data = r.json()
    total = str(data['result']['records'][0]['NewPositive'])

    now = datetime.datetime.now() #retreives the date using datetime
    day = now.strftime("%d") #changes the date into a string
    month = now.strftime("%B")

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(frommail, passwd)
    subject = 'NHS Lothian COVID-19 - ' + day + ' ' + month
    body = 'The daily increase in NHS Lothian today: ' + total
    msg = 'Subject: {}\n\n{}'.format(subject, body)
    server.sendmail(frommail, tomail, msg)
    server.quit()
