import urllib.request
import re
import time
from lib import I2C_LCD_driver

sleep = 3600

x=0
link = 'https://geoegl.msp.gouv.qc.ca/adnv2/tableau-region-simple.php?id=13&type_rapport=ADMIN'

mylcd = I2C_LCD_driver.lcd()

try :
    while (True):
        
        with urllib.request.urlopen(link) as url:
            s = url.read()


        search = str(s,"utf-8")

        search=search.strip("\r\t\n")
        search = re.findall("(Rivi.re des Prairies[\s<>/a-z='ÀéA-Zê()0-9.#\*,]*)",search)
        for i in search:
                niveau = re.findall("[0-9 ]*,[0-9]{2}",i)
                for y in niveau:
                        if x == 0:
                                SIM = y
                                print (("SIM deb: "+ SIM +" m³/s"))
                        elif x==1:
                                debit = y
                                print ("Deb: "+ debit +" m³/s")
                        else:
                                niveau = y
                                print ("Niv: "+ y +" m (normal - 20m)")
                        x+=1

        #print (SIM + "\n" + debit + "\n" + niveau + "\n")
        for z in range(180):
          mylcd.lcd_display_string(niveau + "m (20m)", 1)
          mylcd.lcd_display_string(debit + "m3/s     ", 2)
          time.sleep(5)
          mylcd.lcd_display_string(SIM + "m3/s SIM", 2)
          time.sleep(5)
          z+=1
        #time.sleep(sleep)

except KeyboardInterrupt:
    print("\nCtrl-C pressed")
    mylcd.lcd_clear()
