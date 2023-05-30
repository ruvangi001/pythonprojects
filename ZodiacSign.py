
def zodaicsign(day,month):
    if month=='December':
      sign='Sagittarius' if (day<22) else 'Capricon'
    elif month == 'November':
      sign='Scorpio' if (day<22) else 'Sagittarius'    
    elif month == 'October':
      sign='Libra' if (day<23) else 'Scorpio'
    elif month == 'September':
      sign='Virgo' if (day<23) else 'Libra'
    elif month == 'August':
      sign='Leo' if (day<23) else 'Virgo'
    elif month == 'July':
      sign='Cancer' if (day<23) else 'Leo'
    elif month == 'June':
      sign='Gemini' if (day<21) else 'Cancer'
    elif month == 'May':
      sign='Taurus' if (day<21) else 'Gemini'
    elif month == 'April':
      sign='Aries' if (day<20) else 'Taurus'
    elif month == 'March':
      sign='Pisces' if (day<21) else 'Aries'
    elif month == 'February':
      sign='Aquarius' if (day<19) else 'Pisces'
    elif month == 'January':
      sign='Capricon' if (day<20) else 'Aquarius'
    else:
      print('Enter valid month and date.')
    print('zodiac sign:- ',sign)
       
name = input('Enter the name:- ')
day = int(input('Enter the day:- '))
month = input('Enter the month:- ')
sign=zodaicsign(day,month)

