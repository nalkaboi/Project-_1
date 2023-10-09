#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
import time
import numpy as np
from IPython.display import clear_output

df = pd.read_csv('Bitcoin.csv')

def main_menu():      
    clear_output()
    print('''--------MAIN MENU--------
    1.Bitcoin Values as dataframe
    2.Bitcoin Analysis Using Visuals
    3.Exit''')
    time.sleep(1)
    try:
        main = int(input('<mainM> '))
        if main == 1:
            submenu_1()
        elif main == 2:
            submenu_2()
        elif main == 3:
            exit()
        else:
            print('Input a Valid Choice From The Given.')
            time.sleep(1)
            main_menu()
    except:
        print("Please Enter A Valid Value")
        time.sleep(1)
        main_menu()
        

def exit():
    clear_output()
    print('~Thanks~')
    time.sleep(5)
    clear_output()

def submenu_1():
    print('''                 1.View records(Custom) from start   
                 2.View records(Custom) from end 
                 3.Check out available columns 
                 4. View data from selected column
                 5.Mathematical Analysis of data
                 6. Attributes of the csv taken
                 7.Return To Main Menu
                 8.Exit''')

    x = int(input('<subM1> '))                                             #DataFrame
    
    try:
        if x == 1:
            clear_output()
            numb_rec = int(input('Number Of Records You Want To View: '))
            print(df.head(numb_rec))
            submenu_1()

        elif x == 2:
            clear_output()
            numb_rec = int(input('Number Of Records You Want To View: '))
            print(df.tail(numb_rec))
            submenu_1()

        elif x == 3:
            clear_output()
            print(df.columns)
            submenu_1()

        elif x == 4:
            clear_output()
            columns_data()

        elif x == 5:
            clear_output()
            pass #abhi mereko pata ni isme krna kya
            submenu_1()

        elif x == 6:
            clear_output()
            attributes_csv()

        elif x == 7:
            clear_output()
            main_menu()

        elif x == 8:
            clear_output()
            exit()

        else:
            clear_output()
            print("Please Enter A Input From The Given.")
            time.sleep(1)
            submenu_1()
    except:
        print("Please Enter A Valid Value")
        time.sleep(1)
        submenu_1()
    

def columns_data():
    clear_output()
    print('''Columns Are:           
             ->Date
             ->Open
             ->High
             ->Low
             ->Close
             ->Volume
         ''')          # !!! It lacks that, if user wish to return to submenu he cannot !!!

   
    inp1 = str(input('Enter The Column Name: '))
    low = inp1.lower() #This makes every word small
    inp2 = low.capitalize() #This makes the first letter of the word capital

    if inp2 in df.columns:
        column_data = df[inp2]
        print(column_data)

    else:
        print(f"Column '{inp2}' not found in the DataFrame.") 
        time.sleep(1)
        columns_data()

    submenu_1()

def attributes_csv():             

    clear_output()
    print('''
        
        1.Diplay the [transpose]
        2.Display [indexes] of the DataFrame
        3.Display the [shape] of the DataFrame
        4.Display the [axes] of the DataFrame
        5.Display the [dimension] of the DataFrame
        6.Display the [data types] of all the columns
        7.Display the [size] of the DataFrame
        ''')
    
    try:
        inp = int(input("Enter Your Choice:"))
        if inp == 1:
            clear_output()
            print(df.T)
        elif inp == 2:
            clear_output()
            print(df.index)
        elif inp ==3:
            clear_output()
            print(df.shape)
        elif inp == 4:
            clear_output()
            print(df.axes)
        elif inp ==5:
            clear_output()
            print(df.ndim)           
        elif inp ==6:
            clear_output()
            print(df.dtypes)            
        elif inp ==7:
            clear_output()
            print(df.size)
        else:
            clear_output()
            print("Please Enter A Input From The Given.")
            time.sleep(1)
            attributes_csv()
    except:
        print("Please Enter A valid Input.")
        time.sleep(1)
        attributes_csv()
    submenu_1()

def submenu_2():
    print('''    1 View bar chart of some variable 
    2.View line chart of some variable
    3.Don't_know
    4.Main Menu
    5.Exit 
    ''')
    x = int(input('<subM2> '))          #DataVisualisation

    try:
        if x == 1:
            clear_output()
            time.sleep(0.4)
            bar_plot()
        elif x == 2:
            clear_output()
            time.sleep(0.4)
            line_plot()
        elif x == 3:
            clear_output()
            time.sleep(0.4)
            submenu_2()
        elif x == 4:
            clear_output()
            time.sleep(0.5)
            main_menu()
        elif x == 5:
            clear_output()
            time.sleep(0.5)
            exit()
        else:
            clear_output()
            print("Please Enter A Input From The Given.")
            time.sleep(0.5)
            submenu_2()
    except:
        print("Please Enter A Valid Value")
        time.sleep(0.5)
        submenu_2()

def bar_plot():
    print('''         1. Date versus Close/Open
    2. Date versus Volume 
    3. Date versus High/Low 
    4. Return to Submenu
    5. Exit''')

    try:
        inp = int(input("Enter Your Choice:"))
        df = pd.read_csv('Bitcoin.csv', parse_dates=['Date'], index_col='Date')
        f_d = df['2022-09':'2023-08']
        x = np.arange(12)

        m_d1 = None

        if inp == 1:
            clear_output()
            m_d1 = f_d['Open'].resample('M').mean()
            m_d2 = f_d['Close'].resample('M').mean()
            plt.bar(x - 0.2, m_d1, color='blue', width=0.4, label='Open')
            plt.bar(x + 0.2, m_d2, color='orange', width=0.4, label='Close')
            plt.xlabel('Date')
            plt.ylabel('Mean Value Over A Period Time')
            plt.title('Open Vs Close Time')

        elif inp == 2:
            clear_output()
            m_d = f_d['Volume'].resample('M').mean()
            plt.xlabel('Date')
            plt.ylabel('Mean Value Over A Period Time')
            plt.title('Volume Over Time')
            plt.bar(m_d.index.strftime('%Y-%m'), m_d, color='k', label='Volume')
            plt.xticks(rotation=45)

        elif inp == 3:
            clear_output()
            m_d1 = f_d['High'].resample('M').mean()
            m_d2 = f_d['Low'].resample('M').mean()
            plt.bar(x - 0.2, m_d1, color='green', width=0.4, label='High')
            plt.bar(x + 0.2, m_d2, color='red', width=0.4, label='Low')
            plt.xlabel('Date')
            plt.ylabel('Mean Value Over A Period Time')
            plt.title('High Vs Low Over Time')

        elif inp == 4:
            clear_output()
            submenu_2()

        elif inp == 5:
            clear_output()
            main_menu()
        
        else:
            clear_output()
            print("Please Enter A Valid Input.")
            time.sleep(1)
            bar_plot()
            
    except ValueError:
        print("Please Enter A Valid Input.")
        time.sleep(1)
        bar_plot()

    if m_d1 is not None:
        plt.legend()
        plt.xticks(x, m_d1.index.strftime('%Y-%m'), rotation=45)
    
    plt.show()
    time.sleep(0.7)
    submenu_2()

def line_plot():
    print('''1. Date versus Close/Open
    2. Date versus Volume 
    3. Date versus High/Low 
    4. Return to Submenu
    5. Exit''')
    
    try:
        inp = int(input("Enter Your Choice:"))
        df = pd.read_csv('Bitcoin.csv', parse_dates=['Date'], index_col='Date')
        f_d = df['2022-09':'2023-08']
        
        if inp == 1:
            clear_output()
            m_d1 = f_d['Open'].resample('M').mean()
            m_d2 = f_d['Close'].resample('M').mean()
            plt.xlabel('Date')
            plt.ylabel('Mean Value Over A Period Time')
            plt.title('Open Vs Close Vs Time')
            plt.plot(m_d1.index.strftime('%Y-%m'), m_d1, color='blue', linewidth=2, label='Open')
            plt.plot(m_d2.index.strftime('%Y-%m'), m_d2, color='orange', linewidth=2, label='Close')
          
            

        elif inp == 2:
            clear_output()
            m_d = f_d['Volume'].resample('M').mean()
            plt.xlabel('Date')
            plt.ylabel('Mean Value Over A Period Time')
            plt.title('Volume Over Time')
            plt.plot(m_d.index.strftime('%Y-%m'), m_d, linewidth = 2, color='k', label='Volume')
            

        elif inp == 3:
            clear_output()
            m_d1 = f_d['High'].resample('M').mean()
            m_d2 = f_d['Low'].resample('M').mean()
            plt.plot(m_d1.index.strftime('%Y-%m'), m_d1, color='green', linewidth=2, label='High')
            plt.plot(m_d2.index.strftime('%Y-%m'), m_d2, color='red', linewidth=2, label='Low')
            plt.xlabel('Date')
            plt.ylabel('Mean Value Over A Period Time')
            plt.title('High Vs Low Over Time')

        elif inp == 4:
            clear_output()
            submenu_2()

        elif inp == 5:
            clear_output()
            main_menu()

        else:
            clear_output()
            print("Please Enter A Valid Input.")
            time.sleep(1)
            line_plot()
            
    except ValueError:
        clear_output()
        print("Please Enter A Valid Input.")
        time.sleep(1)
        line_plot()
    plt.xticks(rotation = 45)
    plt.grid()
    plt.legend()
    plt.show()
    time.sleep(0.7)
    submenu_2()

main_menu()  #357 lines

