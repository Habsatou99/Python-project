from pandas import pd

from MarginalX import Marginalx


def IndependanceTheorique(df):
    dataf=pd.DataFrame({'X\Y': ['X1','X2', 'X3'],

                   'Y1': [100, 0, 0],
                   'Y2': [10, 40, 0],
                   'Y3': [10, 0, 40],
                   })
    
    df3=pd.DataFrame({
  'X\Y': ['X1', 'X2', 'X3'],

  'Y1': [(Marginalx(dataf)[0]/200)*100,(Marginalx(dataf)[1]/200)*100],
  'Y2': [10, 40, 0],
  'Y3': [10, 0, 40],  
})