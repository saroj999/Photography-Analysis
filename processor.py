import pandas as pd
def process(data):
    
    df = pd.read_csv(data)
    
    df.drop(columns=['No'],inplace = True)
    
    #Extracting year from the data
    df['year'] = pd.DatetimeIndex(df['Date']).year
    
    #Extracting month from the data
    df['month'] = pd.DatetimeIndex(df['Date']).month
    
    
    return df
    

