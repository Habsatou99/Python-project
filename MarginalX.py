import pandas as pd
def Marginalx(dataf):
    dataf= pd.DataFrame({'X\Y': [0, 0, 0],

                   'Y1': [100, 0, 0],
                   'Y2': [10, 40, 0],
                   'Y3': [10, 0, 40],
                   })
    dataf1 =pd.DataFrame({
        'Marge de X':dataf.sum(axis = 1)
    })
  
    return dataf1
