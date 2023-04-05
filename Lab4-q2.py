temperature = input('Enter Temperature:')
if(float(temperature)>= 50):
    print('Hot')
if(float(temperature)>= 30 and float(temperature) < 50):
    print('Warm')
if(float(temperature)>= 0 and float(temperature) < 30):
    print('Cold')
if(float(temperature)<=0):
        print('Extreme cold')

