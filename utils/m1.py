import pandas as pd
import streamlit as st

class Search:
    def __init__ (self,lst,var):
        self.lst = lst
        self.var = var

    @staticmethod
    def algo0 (lst,var):
        for i in range(0, len(lst)):
            if var == lst[i]:
                return i
    
    def algo1 (df,lst):
        #Selection of choices for scatterplot
        xs, ys      = st.sidebar.multiselect(label='Select data type to compare',
                                            options=['spoilage_risk', 'daily_demand'],
                                            default=['spoilage_risk', 'daily_demand'],
                                            max_selections=2)
        numd        = st.sidebar.number_input(f"Insert number of data",
                                        min_value=50, max_value=1000, step=50, placeholder=100)
        #Concatenation of dataframe
        x0 = Search.algo0(lst,xs)
        y0 = Search.algo0(lst,ys)
        df1 = df[[lst[x0]]].iloc[0:numd]
        df2 = df[[lst[y0]]].iloc[0:numd]
        jdf = pd.concat([df1, df2], axis = 1)
        
        return jdf, xs, ys , df1, df2