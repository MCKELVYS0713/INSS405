temperature=input('Enter Temperature:')
if(float(temperature)>=50):
   print('Hot')
elif (float(temperature)>=30 and float(temperature)<=50):
   print('Warm')
elif (float(temperature)>=0 and float(temperature)<=30):
   print('Cold')
else:
   print('Extreme Cold')
if(float(temperature)<=-20):
    print('Extreme chill cold,shelter in place')



