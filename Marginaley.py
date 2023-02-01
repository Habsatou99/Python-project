import pandas as pd
def Marginaly(dataf):
    dataf=pd.DataFrame({'X\Y': ['X1','X2', 'X3'],

                   'Y1': [100, 0, 0],
                   'Y2': [10, 40, 0],
                   'Y3': [10, 0, 40],
                   })
    som1=dataf['Y1'].sum()
    som2=dataf['Y2'].sum()
    som3=dataf['Y3'].sum()
    df1=pd.DataFrame({
        'Marge de Y':[som1,som2, som3]
    })
  
    return df1
