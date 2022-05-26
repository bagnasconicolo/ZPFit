``` import numpy as np ```
``` parabdata=np.array(["dati_p_plot.csv","Tempo (s)","Spostamento (cm)", "Accelerazione Iniziale", float(0.05)]) ```
``` %store parabdata ```
``` %run parabolic.ipynb ```
``` %store -r latexfig ```
``` print("\n".join(latexfig)) ```
