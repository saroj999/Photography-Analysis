import numpy as np
import pandas as pd
'''
Total customer 
Unique customer
Total modeling
Total wedding
Total Xerox/Print
Total Karizma album
Total Id Photo
Total Earning
'''
def fetch_stats(selected_user,df):
    
    Total_customer = df.shape[0]
    Unique_customer = len(df['Name'].unique())
    Total_modeling = df[df['Type'] == "M"].shape[0]
    Total_wedding = df[df['Type'] == "W"].shape[0]
    
    return Total_customer,Unique_customer,Total_modeling,Total_wedding

def fetch_stats_1(selected_user,df):
    
    Total_Xerox = df[df['Type'] == "X"].shape[0]
    Total_Karizma_album = df[df['Type'] == "WKA"].shape[0]
    Total_Id_Photo = df[df['Type'] == "ID"].shape[0]
    Total_Earning = df['Amount'].sum()
    
    return Total_Xerox,Total_Karizma_album,Total_Id_Photo,Total_Earning

def fetch_stats_graphs(df):
    x = df['Type'].value_counts()
    return x

def fetch_stats_graphs1(df):
    m=df[df['Type'] == "M"].shape[0]
    w=df[df['Type'] == "W"].shape[0]
    x=df[df['Type'] == "X"].shape[0]
    iD=df[df['Type'] == "ID"].shape[0]
    wka=df[df['Type'] == "WKA"].shape[0]
    
    labels = ['Modeling', 'Wedding', 'Xerox/Print', 'Id Photo','Karizma album']
    sizes = [m, w, x, iD,wka]
    # only "explode" the 2nd slice ()
    explode = (0, 0, 0, 0.1, 0)
    return labels, sizes, explode

def fetch_stats_graphs2(df):
    df1 = df.groupby(['Age']).count()['Amount'].reset_index()
    return df1


def fetch_stats_graphs3(df):
    x = df.groupby('month')['Amount'].sum()
    return x


def fetch_stats_graphs4(df):
    a=df[df['Gender'] == 'M'].value_counts()
    m = len(a)
    b=df[df['Gender'] == 'F'].value_counts()
    g = len(b)
    labels = ['Male','Female']
    sizes = [m, g]
# only "explode" the 2nd slice ()
    explode = (0.1,0)
    return labels, sizes, explode



