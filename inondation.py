import urllib.request
import re
import time
from lib import I2C_LCD_driver

link = 'https://geoegl.msp.gouv.qc.ca/libcommunes/MSPwidgets/hydrogramme/index.php?station=043301&type1=niveau&type2=debit'

mylcd = I2C_LCD_driver.lcd()

with urllib.request.urlopen(link) as url:
  s = url.read()
search = str(s,"utf-8")

#ETAT
etat = re.findall("(État[\s<>/-ÀA-Z\&;:,]*)",search)
etat = (etat[1])
etat = str(etat[16:])
etat = etat.split('<')
etat = str(etat[0])
etat = str(etat[:7])
print ("Etat: "+etat)

#debit
debit = re.findall("(Débit[\s<>/-ÀA-Z\&,]*)",search)
debit = (debit[0])
debit = str(debit[18:])
debit = debit.split('m')
debit = str(debit[0])
print ("Debit: "+debit+"m3/s")

#SIM
SIM = re.findall("(SIM[\s<*>/-ÀA-Z\&,]*)",search)
SIM = (SIM[0])
SIM = str(SIM[29:])
SIM = SIM.split('\t')
SIM = str(SIM[0])
SIM = SIM.split('m')
SIM = str(SIM[0])
SIM = SIM[:-1]
print ("SIM: "+SIM+"m3/s")

#NIVEAU
niveau = re.findall("(Niveau[\s<*>/-ÀA-Z\&,]*)",search)
niveau = str(niveau[0])
niveau = niveau[19:]
niveau = niveau.split('<')
niveau = str(niveau[0])
niveau = niveau[:4]
print ("Niveau: "+niveau+"m")

print ("\n")

mylcd.lcd_display_string(etat+" "+niveau+"m", 1)
mylcd.lcd_display_string(debit+"m3/s      ", 2)
