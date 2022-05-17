# Repository di file per fare fit statistici con output in LaTeX
Diritto di autore - N. Bagnasco [Email me!](mailto:nicolo.bagnasco@edu.unito.it)


Per funzionare si devono creare nella stessa directory del file `.ipynb` o `.py` tre file  `.csv`:

1. `fit.csv` vuoto,
2. `corr.csv` vuoto,
3. `dati.csv` con tre colonne, rispettivamente:
  * xdata,
  * ydata,
  * yerr.

Nella cartella  `/jupyter/` sono già disponibili i tre  `.csv` vuoti.

Nota: 
Parte del codice è stata presa dai notebook utilizzati dai professori R. Bonino e M. Bertaina per il corso di Esperimentazioni 1 all'Università di Torino.

## Versione 2 aggiunta!

changelog:
- Aggiunto blocco per conversione da excel a csv
- Aggiunti ```display()``` per l'output
- Migliorato il debug e la formattazione dei dati in output
- Ora il notebook crea da se' i csv necessari, e se sono già esistenti li svuota prima di iniziare i calcoli.
