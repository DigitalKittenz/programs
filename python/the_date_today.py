
from datetime import date

#today is being defined here
today = date.today()#date today

#now is defined as today + strftime for formatting
now = today.strftime("%m/%d/%Y")
print("Today's date is:",now)

