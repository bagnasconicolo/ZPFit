
from sympy import *

import numpy as np
import scipy.stats
import csv
import matplotlib.pyplot as plt
import pandas as pd
from random import randint
xx, yy, aa, bb, cc = symbols('xx yy aa bb cc')

    
#Livello di criticità es. (.05)
alpha=.05
unma='cm'
unmb='N'
plt.rcParams['figure.figsize'] = [15, 10]

#Importo dati.csv con tre colonne (x, y, yerr) in tre liste

data = csv.reader(open('dati.csv', 'r'), delimiter=",", quotechar='|')
lxcol, lycol, lyerrcol = [], [], []

for row in data:
    lxcol.append(row[0])
    lycol.append(row[1])
    lyerrcol.append(row[2])
    
#Converto in array
ydatap = np.asarray(lycol, dtype=np.float64)

yerrp = np.asarray(lyerrcol, dtype=np.float64)
print('')

xdataor = np.asarray(lxcol, dtype=np.float64)
npoint = len(xdataor)
npoint
ax,bx = float(xdataor[0]),float(xdataor[npoint-1])
apx,bpx = 2./(bx-ax),(bx + ax)/(bx - ax)
print(ax)
print(bx)
print(apx)
print(bpx)
xdata = xdataor*apx - bpx
xdata
#xdata=xdataor
ydata = ydatap
yerr = yerrp
if (len(xdata)!=len(ydata)): print ("dimensioni vettori disuguali")
if (len(yerr)!=len(ydata)) : print ("dimensioni vettori disuguali")
    # Calcolo delle derivate di X^2
s = expand((yy - cc*xx**2 - bb*xx - aa)**2)
s
s_aa = diff(s,aa)
s_aa
s_bb = diff(s,bb)
s_bb
s_cc = diff(s,cc)
s_cc
yerrSq = yerr*yerr
sum_one_over_yerrSq = (1./yerrSq).sum()
sum_x_over_yerrSq = (xdata/yerrSq).sum()
sum_x2_over_yerrSq = (xdata*xdata/yerrSq).sum()
sum_x3_over_yerrSq = (xdata*xdata*xdata/yerrSq).sum()
sum_x4_over_yerrSq = (xdata*xdata*xdata*xdata/yerrSq).sum()
sum_y_over_yerrSq = (ydata/yerrSq).sum()
sum_xy_over_yerrSq = (xdata*ydata/yerrSq).sum()
sum_x2y_over_yerrSq = (xdata*xdata*ydata/yerrSq).sum()
#Calcolo matrice D e matrice inversa


matD = np.array([[sum_one_over_yerrSq,sum_x_over_yerrSq,sum_x2_over_yerrSq],
                [sum_x_over_yerrSq,sum_x2_over_yerrSq,sum_x3_over_yerrSq],
                [sum_x2_over_yerrSq,sum_x3_over_yerrSq,sum_x4_over_yerrSq]])
matD_inv = np.linalg.inv(matD)
matD
matD_inv

print("check =I")
np.dot(matD,matD_inv)

matB = np.array([sum_y_over_yerrSq,sum_xy_over_yerrSq,sum_x2y_over_yerrSq])
matB
np.dot(matD_inv,matB)


a, b, c = np.dot(matD_inv,matB)[0],np.dot(matD_inv,matB)[1],np.dot(matD_inv,matB)[2]
print(" a = ", a)
print(" b = ", b)
print(" c = ", c)



vara, varb, varc= matD_inv[0,0], matD_inv[1,1], matD_inv[2,2]
erra=np.sqrt(vara)
errb=np.sqrt(varb)
errc=np.sqrt(varc)
print(" errore su a = ",erra)
print(" errore su b = ",errb)
print(" errore su c = ",errc)

fig, ax = plt.subplots()
thickxdata = np.arange(-1.,1.,0.1)
ax.set_xlabel('variable x (u.m.)')
ax.set_ylabel('variable y (u.m.)')
# ax.set_xlim(0, 5); ay.set_xlim(0, 5) PEr cambiare range plot
plt.plot(thickxdata,c*thickxdata*thickxdata+b*thickxdata+a)
plt.errorbar(xdata,ydata,yerr=yerr,fmt='o')
scarto1 = (ydata-a-b*xdata-c*xdata*xdata)/yerr
scarto2 = (ydata-a-b*xdata-c*xdata*xdata)
chi2 = (scarto1*scarto1).sum()
errstSq = (scarto2*scarto2/(npoint-3)).sum()
errst = np.sqrt(errstSq)
print(" Chi^2 = ",chi2)
print (" errore standard della stima = ",errst)

sum_y = (ydata).sum()
ymean=sum_y/npoint
ameany = ydata-ymean
vary = (ameany*ameany).sum()
yatteso =a+b*xdata+c*xdata*xdata
scarto3=yatteso-ymean
var_numeratore=(scarto3*scarto3).sum()
detercoeff2=var_numeratore/vary
detercoeff=np.sqrt(detercoeff2)
print("coefficiente determinazione = ",detercoeff)




#CSV Fit
#First column merging with um
aatext='Parametro a ['+ unma+ ']'
print(aatext)
abtext='Parametro b ['+ unmb+ '])'
print(abtext)
actext='Parametro c ['+ unma+ '])'
print(actext)
erratext='Errore su a ['+ unmb+ '])'
print(erratext)
errbtext='Errore su b ['+ unmb+ '])'
print(errbtext)
errctext='Errore su c ['+ unmb+ '])'
print(errctext)
determtext='Coeff. di determinaz.'
print(errctext)
#Creating Arrays
corrhead = np.array(['Variabile','Valore'])

aa = np.array([aatext,c])
ab = np.array([abtext,b])
ac = np.array([actext,a])
aerra = np.array([erratext,errc])
aerrb = np.array([errbtext,errb])
aerrc = np.array([errctext,erra])

adeterm = np.array([determtext,detercoeff])
#writing csv
with open('corr.csv', mode='w') as corr:
    corr_writer = csv.writer(corr, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    corr_writer.writerow(corrhead)
    corr_writer.writerow(aa)
    corr_writer.writerow(ab)
    corr_writer.writerow(ac)
    corr_writer.writerow(aerra) 
    corr_writer.writerow(aerrb) 
    corr_writer.writerow(aerrc) 
    corr_writer.writerow(adeterm)

#Plot
#-----------------------------------------------------------------------------------------------------

#Chi2 logic test
def check(c2,cr,su):
    if c2>cr:
        return 'Rigettato'
    elif c2<cr and c2>su:
        return 'Accettato'
    elif c2<su:
        return 'Sospetto'
    else:
        print('Check error')
        return 0
    
#Numero GDL
n=len(xdata)-3
print('len',len(xdata))
crit=scipy.stats.chi2.ppf(1-alpha , df=n)
sus=scipy.stats.chi2.ppf(alpha , df=n)

print('Chi quadro critico, ',crit)
print('Chi quadro sospetto, ',sus)
es=check(chi2,crit,sus)
print("Esito del test, ",es)

#Arrays for csv
asig = np.array(['Livello di significatività',alpha])
agdl = np.array(['Gradi di libertà',n])
acrit = np.array(['Chi quadro critico',crit])
chi = np.array(['Chi quadro ',chi2])
asus = np.array(['Chi quadro sospetto',sus])
esito = np.array(['Esito',es])
head = np.array(['Variabile','Valore'])
#CSV writing
with open('fit.csv', mode='w') as fit:
    fit_writer = csv.writer(fit, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    fit_writer.writerow(head)
    fit_writer.writerow(asig)
    fit_writer.writerow(agdl)
    fit_writer.writerow(chi)    
    fit_writer.writerow(acrit)
    fit_writer.writerow(asus)
    fit_writer.writerow(esito)   
    
print('')
print('')

dfcorr = pd.read_csv ('corr.csv')
dffit = pd.read_csv ('fit.csv')
    
print('')
print('')
print(dfcorr)
    
print('')
print('')
print(dffit)
    
print('')
print('')
indexcorr='corr'+str(randint(0, 1000))
indexfit='fit'+str(randint(0, 1000))
    
print('')
print('')
print(dfcorr.to_latex(index=False, caption='Dati relativi al fit lineare', bold_rows=True, label=indexcorr, position='ht'))
    
print('')
print('')
print(dffit.to_latex(index=False,  caption='Dati relativi al test del $\chi^2$', bold_rows=True, label=indexfit, position='ht'))

    
print('')
print('')
