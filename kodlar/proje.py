import RPi.GPIO as GPIO
import dht11
import time
import datetime
veriler=open("veriler.txt","w")
veriler.close()
GPIO.setmode(GPIO.BCM)
GPIO.setmode(GPIO.BOARD)
instance1 = dht11.DHT11(pin=11)
instance2 = dht11.DHT11(pin=13)
GPIO.setup(29, GPIO.INPUT)
GPIO.setup(31, GPIO.INPUT)
GPIO.setup(33, GPIO.INPUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

while(true):
    zaman =datetime.datetime.now()
    dakika=zaman.minute
    saniye=zaman.second
    kayit=dakika+saniye
    step_motor_calisiyor = 0
    result1 = instance1.read()
    if result1.is_valid():
        icsicaklik = result.temperature
        icnem = result.humidity
    result2 = instance2.read()
    if result2.is_valid():
        dissicaklik = result.temperature
        disnem = result.humidity


    sicaklık_farkı= icsicaklik - dissicaklik

    if icsicaklik<=20 :
       GPIO.output(16,1)
       GPIO.PWM(12, 1)
    elif icsicaklik<=30 :
       GPIO.output(16,1)
       GPIO.PWM(12, 0.9)
    elif icsicaklik<=35 :
       GPIO.output(16,1)
       a=(50+sicaklık_farkı*1.5)/100
       GPIO.PWM(12, a)
    elif icsicaklik<=36.5 :
       GPIO.output(16,1)
       b=(sicaklık_farkı*3)/100
       GPIO.PWM(12, b)
    elif icsicaklik<=38 :
       GPIO.output(16,1)
       a=0
       GPIO.PWM(12, a)
    else :
        GPIO.output(18, 1)
        GPIO.output(16, 1)

    if step_motor_calisiyor==0 :

        hareket1=GPIO.input(29)
        hareket2=GPIO.input(31)
        hareket3=GPIO.input(33)
        hareket=hareket1+hareket2+hareket3
        if hareket!=3:
            GPIO.output(22, 1)


    if kayit==0 :
        sistem_zamani=datetime.datetime.now()
        saat=sistem_zamani.hour
        gun=sistem_zamani.day
        ay=sistem_zamani.month
        yil=sistem_zamani.year

        veriler=open("veriler.txt","a")
        veriler.write("%d-%d-%d %d:00      iç sıcaklık=%f,   dış sıcaklık=%f,   nem=%f,",gun,ay,yil,saat,icsicaklik,dissicaklik,icnem)
        veriler.close()
        time.sleep(1)

