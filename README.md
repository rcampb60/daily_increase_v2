# daily_increase_v2

This script is the second verison of the dailyincrease script. This script finds the daily increase in COVID-19 cases in NHS Lothian and emails the results each day at 14:10. 

The script has been made into a lambda, but also now uses the NHS Scotland Opendata API which is updated daily, rather than the previous method of downloading spreadsheets which updated only on working days.

Additionally the timeouts and memory usage have been reduced to the minimum rather than having to bump them up each time the spreadsheet grows too big.

There was an issue when numbers were not reported one day and this had a knock on effect as the NaN in the spreadsheet couldn't been used to evaluate the increase. This new version doesn't rely on that. 

All secret keys and emails have been removed. To use please have two separate email addresses, I don't believe this will work with just one email address currently, and if using Gmail please use an app password.
