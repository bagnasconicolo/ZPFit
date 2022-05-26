#### Create np.array with parameters and save it in global functions

``` import numpy as np ```

``` parabdata=np.array(["filename.csv","X axis label","Y axis label", "Plot title", float(alpha)]) ```

``` %store parabdata ```

#### Run parabolic fit software

``` %run parabolic.ipynb ```

#### Read output datasets from global

NOTE: Always local-save this variables to prevent overwriting.

``` %store -r latexfig ```

``` print("\n".join(latexfig)) ```

``` %store -r dfcorr ```

``` %store -r dffit ```
