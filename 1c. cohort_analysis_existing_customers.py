import numpy as np
import pandas as pd
import datetime
import time

### Define Functions

def customer_return_count(days,customer_list, date):
    check_till = pd.to_datetime(date) + pd.DateOffset(days+1)
    #tmp_df = customer_data[(customer_data['CustomerID'].isin(customer_list)) & (customer_data['NewCustomerFlag'] == 0)]
    tmp_df = customer_data[(customer_data['CustomerID'].isin(customer_list)) & (customer_data['OrderDate'] > pd.to_datetime(date))]
    tmp_df = tmp_df[tmp_df['OrderDate'].dt.to_pydatetime() <= check_till.to_pydatetime()]
    return len(tmp_df['CustomerID'].unique())


#['ACC14266665009185396','ACC14125678795121376']

### Load data
customer_data = pd.read_csv("X:\ISB\Capstone\Data\phase2 data\SmallData\SmallData.csv")
customer_data.drop(customer_data.columns[[0]], axis=1, inplace=True)

### Convert into datetime format
customer_data['OrderDate'] = pd.to_datetime(customer_data['OrderDate'], format='%Y%m%d')
customer_data['CustomerStartDate'] = pd.to_datetime(customer_data['CustomerStartDate'])


### Filter out new customer data
new_customer_data = customer_data[customer_data['NewCustomerFlag'] == 1]

#############################################
### Number of customers accuired - daywise
#############################################

#grp_obj = new_customer_data['CustomerID'].groupby([new_customer_data['CustomerStartDate'].dt.date])
#df = grp_obj.agg({'nunique'})
#df.reset_index(level= 0, inplace = True)
#df.rename(columns = {'nunique':'NumberOfNewCustomer'}, inplace = True)

#######################################################
################### Return count ######################
#######################################################

### Get customer start dates
dt_lst = list(set(new_customer_data['CustomerStartDate'].astype(str)))
dt_lst.sort()

df2 = pd.DataFrame(columns= ['CustomerStartDate','NumberofOldCustomerPurshased', 'return30','return60','return90', 'return120', 'return150','return180', 'return210','return240','return270', 'return300','return330', 'return360', 'results390', 'results420', 'results450', 'results480', 'results510', 'results540'])
#d = '2015-04-01'
for d in dt_lst:
    start = time.time()
    #cust_lst = list(set(new_customer_data.groupby(new_customer_data['CustomerStartDate'].dt.date).get_group(d)['CustomerID']))
    cust_lst = customer_data[(customer_data['OrderDate'] == pd.to_datetime(d)) & (customer_data['CustomerStartDate'] != pd.to_datetime(d))]['CustomerID']
    NumberofOldCustomerPurshased = len(cust_lst.unique())
    results30  = customer_return_count(30,  cust_lst, d)
    results60  = customer_return_count(60,  cust_lst, d)
    results90  = customer_return_count(90,  cust_lst, d)
    results120 = customer_return_count(120, cust_lst, d)
    results150 = customer_return_count(150, cust_lst, d)
    results180 = customer_return_count(180, cust_lst, d)
    results210 = customer_return_count(210, cust_lst, d)
    results240 = customer_return_count(240, cust_lst, d)
    results270 = customer_return_count(270, cust_lst, d)
    results300 = customer_return_count(300, cust_lst, d)
    results330 = customer_return_count(330, cust_lst, d)
    results360 = customer_return_count(360, cust_lst, d)
    results390 = customer_return_count(390, cust_lst, d)
    results420 = customer_return_count(420, cust_lst, d)
    results450 = customer_return_count(450, cust_lst, d)
    results480 = customer_return_count(480, cust_lst, d)
    results510 = customer_return_count(510, cust_lst, d)
    results540 = customer_return_count(540, cust_lst, d)

    df1 = pd.DataFrame([[d, NumberofOldCustomerPurshased,results30, results60, results90, results120, results150, results180, results210, results240, results270, results300, results330, results360, results390, results420, results450, results480, results510, results540]], columns=['CustomerStartDate', 'NumberofOldCustomerPurshased','return30', 'return60', 'return90', 'return120', 'return150', 'return180', 'return210', 'return240', 'return270', 'return300', 'return330', 'return360', 'results390', 'results420', 'results450', 'results480', 'results510', 'results540'])
    df2 = df2.append(df1)
    df2.to_csv("X:\ISB\Capstone\Data\phase2 data\SmallData\cohort_oldcustomer_churn_analysis.csv")
    print(d,"done ", "Time Taken: ", time.time() - start)

