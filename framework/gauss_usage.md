##create array with dataset
gaussdata=np.array([x,mu,err_x,alpha])
##save dataset
%store gaussdata
##run ipynb
%run gauss.ipynb
##now the output is savedi in 'gdf' dataframe, copy this in another variable to prevent overwriting.
