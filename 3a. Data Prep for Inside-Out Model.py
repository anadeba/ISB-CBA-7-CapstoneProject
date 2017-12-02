import pandas as pd
import numpy as np

def find_recent_order_date(cid):
    x = customer_data_all_april17[customer_data_all_april17['sn_anurag_variables_v13_1_percent_v3.account_id'] == cid]
    print(cid)
    return (x[x['sn_anurag_variables_v13_1_percent_v3.order_item_date'] == x['sn_anurag_variables_v13_1_percent_v3.order_item_date'].max()]['sn_anurag_variables_v13_1_percent_v3.order_id'].iloc[0].astype(np.int64))


### Load data
fields_to_read = ['sn_anurag_variables_v13_1_percent_v3.account_id','sn_anurag_variables_v13_1_percent_v3.order_id','sn_anurag_variables_v13_1_percent_v3.order_item_id','sn_anurag_variables_v13_1_percent_v3.order_item_date','sn_anurag_variables_v13_1_percent_v3.order_sales_channel_generic','sn_anurag_variables_v13_1_percent_v3.order_item_service_profile','sn_anurag_variables_v13_1_percent_v3.order_item_discount_percent','sn_anurag_variables_v13_1_percent_v3.shipping_charge','sn_anurag_variables_v13_1_percent_v3.city_tier','sn_anurag_variables_v13_1_percent_v3.analytic_business_unit','sn_anurag_variables_v13_1_percent_v3.analytic_super_category','sn_anurag_variables_v13_1_percent_v3.analytic_category','sn_anurag_variables_v13_1_percent_v3.analytic_sub_category','sn_anurag_variables_v13_1_percent_v3.analytic_vertical','sn_anurag_variables_v13_1_percent_v3.segment_2','sn_anurag_variables_v13_1_percent_v3.first_purchase_date','sn_anurag_variables_v13_1_percent_v3.newcust_flag','sn_anurag_variables_v13_1_percent_v3.paymentmethod','sn_anurag_variables_v13_1_percent_v3.sellertier','sn_anurag_variables_v13_1_percent_v3.new_pro_rating_count','sn_anurag_variables_v13_1_percent_v3.new_pro_rating', 'sn_anurag_variables_v13_1_percent_v3.new_pro_overall_rating_count', 'sn_anurag_variables_v13_1_percent_v3.new_pro_overall_rating', 'sn_anurag_variables_v13_1_percent_v3.new_sel_rating_count', 'sn_anurag_variables_v13_1_percent_v3.new_sel_rating','sn_anurag_variables_v13_1_percent_v3.new_sel_overall_rating_count','sn_anurag_variables_v13_1_percent_v3.new_sel_overall_rating']
customer_data = pd.read_csv(r"X:\ISB\Capstone\Data\phase2 data\revised_data\Others_1_29112017\Others_1_29112017.csv", delimiter = '\t', usecols = fields_to_read)
#customer_data_fields = pd.read_csv('C:\Users\debanjan\Downloads\other_1\other_fields.csv')

### Remane fields

#customer_data.rename(index=str, columns={"sn_anurag_variables_v13_1_percent_v3.account_id": "CustomerID", "sn_anurag_variables_v13_1_percent_v3.order_id": "OrderID", "sn_anurag_variables_v13_1_percent_v3.order_item_date": "OrderDate", "sn_anurag_variables_v13_1_percent_v3.order_sales_channel_generic": "SalesChannel","sn_anurag_variables_v13_1_percent_v3.first_purchase_date": "CustomerStartDate", "sn_anurag_variables_v13_1_percent_v3.newcust_flag": "NewCustomerFlag"})


### Convert into datetime format
customer_data['sn_anurag_variables_v13_1_percent_v3.order_item_date'] = pd.to_datetime(customer_data['sn_anurag_variables_v13_1_percent_v3.order_item_date'])
#customer_data['sn_anurag_variables_v13_1_percent_v3.order_item_date'] = customer_data['sn_anurag_variables_v13_1_percent_v3.order_item_date'].dt.date
#customer_data['CustomerStartDate'] = pd.to_datetime(customer_data['CustomerStartDate'])

### April all customers
customer_data_all_april17 = customer_data[(customer_data['sn_anurag_variables_v13_1_percent_v3.order_item_date'] >= pd.to_datetime('2017-04-01')) & (customer_data['sn_anurag_variables_v13_1_percent_v3.order_item_date'] <= pd.to_datetime('2017-04-30'))]
customer_id_all_april17 = customer_data_all_april17['sn_anurag_variables_v13_1_percent_v3.account_id'].unique()
customer_id_all_april17_nochurn = customer_data[(customer_data['sn_anurag_variables_v13_1_percent_v3.account_id'].isin(customer_id_all_april17)) & (customer_data['sn_anurag_variables_v13_1_percent_v3.order_item_date'] > pd.to_datetime('2017-04-30'))]['sn_anurag_variables_v13_1_percent_v3.account_id'].unique()
df = pd.DataFrame(columns= ['sn_anurag_variables_v13_1_percent_v3.account_id'])
df = pd.DataFrame(customer_id_all_april17, columns = ['sn_anurag_variables_v13_1_percent_v3.account_id'])
df['Churn'] = df['sn_anurag_variables_v13_1_percent_v3.account_id'].isin(customer_id_all_april17_nochurn)

#df['Recent_OrderID_April17'] = df.apply(lambda r: find_recent_order_date(r['CustomerID']), axis = 1)
#order_list = []
#for c in df['CustomerID']:
#    order_list = order_list.append(find_recent_order_date(c))

df['Recent_OrderID_April17'] = list(map(find_recent_order_date, df['sn_anurag_variables_v13_1_percent_v3.account_id']))

df.to_csv(r"X:\ISB\Capstone\Data\phase2 data\revised_data\april_customers.csv")
df.rename(columns = {"Recent_OrderID_April17" : "sn_anurag_variables_v13_1_percent_v3.order_id"}, inplace = True)

df1 = df.merge(customer_data_all_april17, how = 'left', on = 'sn_anurag_variables_v13_1_percent_v3.order_id')
df1['sn_anurag_variables_v13_1_percent_v3.order_item_id'] = df1['sn_anurag_variables_v13_1_percent_v3.order_item_id'].apply(lambda x: str(x)+"C")
df1.to_csv(r"X:\ISB\Capstone\Data\phase2 data\revised_data\april_customers_data_v2.csv")

################# CX Formatting ##################

df1 = pd.read_csv(r"X:\ISB\Capstone\Data\phase2 data\revised_data\april_customers_data_v2.csv")
cx_data = pd.read_csv(r"X:\ISB\Capstone\Data\phase2 data\revised_data\CX_1_29112017\CX_1_29112017.csv", delimiter = '\t')
cx_data['ps_mac_features_anurag_account_incident_level_1_percent_v2.i_date'] = pd.to_datetime(cx_data['ps_mac_features_anurag_account_incident_level_1_percent_v2.i_date'])
cx_data_all_april17 = cx_data[(cx_data['ps_mac_features_anurag_account_incident_level_1_percent_v2.i_date'] >= pd.to_datetime('2017-04-01')) & (cx_data['ps_mac_features_anurag_account_incident_level_1_percent_v2.i_date'] <= pd.to_datetime('2017-04-30'))]

#cx_data.rename(columns = {"ps_mac_features_anurag_account_incident_level_1_percent_v2.order_id" : "order_id"}, inplace = True)
cx_data_all_april17.rename(columns = {"ps_mac_features_anurag_account_incident_level_1_percent_v2.account_id" : "sn_anurag_variables_v13_1_percent_v3.account_id_x"}, inplace = True)
df2 = df1.merge(cx_data_all_april17, how ='left', on = 'sn_anurag_variables_v13_1_percent_v3.account_id_x')
df2.to_csv(r"X:\ISB\Capstone\Data\phase2 data\revised_data\april_customers_data_v3.csv")


### RVP Formatting

df2 = pd.read_csv(r"X:\ISB\Capstone\Data\phase2 data\revised_data\april_customers_data_v3.csv")
rvp_data = pd.read_csv(r"X:\ISB\Capstone\Data\phase2 data\revised_data\RVP_1_29112017\RVP_1_29112017.csv")
rvp_reasons_bucket = pd.read_csv(r"X:\ISB\Capstone\Data\phase2 data\revised_data\RVP_1_29112017\rvp_reasons_mapping.csv")
rvp_reasons_bucket.rename(columns = {"return_item_reason" : "rav_churn_model_rvp_base_v2_1_percent_v2.return_item_reason"}, inplace = True)
rvp_data = rvp_data.merge(rvp_reasons_bucket, how = 'left', on = 'rav_churn_model_rvp_base_v2_1_percent_v2.return_item_reason')
rvp_data.rename(columns = {"rav_churn_model_rvp_base_v2_1_percent_v2.order_item_id" : "sn_anurag_variables_v13_1_percent_v3.order_item_id"}, inplace = True)
df3 = df2.merge(rvp_data, how = 'left', on = 'sn_anurag_variables_v13_1_percent_v3.order_item_id')
df3.loc[df3['rav_churn_model_rvp_base_v2_1_percent_v2.return_action'].str.contains('replace',na = False), 'rav_churn_model_rvp_base_v2_1_percent_v2.return_actions'] = 'replace'
df3.loc[df3['rav_churn_model_rvp_base_v2_1_percent_v2.return_action'].str.contains('refund',na = False), 'rav_churn_model_rvp_base_v2_1_percent_v2.return_actions'] = 'refund'
df3.loc[df3['rav_churn_model_rvp_base_v2_1_percent_v2.return_action'].str.contains('exchange',na = False), 'rav_churn_model_rvp_base_v2_1_percent_v2.return_actions'] = 'exchange'
df3.drop('rav_churn_model_rvp_base_v2_1_percent_v2.return_action', axis = 1, inplace = True)

df3.loc[df3['rav_churn_model_rvp_base_v2_1_percent_v2.return_item_status'].str.contains('cancelled',na = False), 'rav_churn_model_rvp_base_v2_1_percent_v2.return_item_status2'] = 'cancelled'
df3.loc[df3['rav_churn_model_rvp_base_v2_1_percent_v2.return_item_status'].str.contains('rejected',na = False), 'rav_churn_model_rvp_base_v2_1_percent_v2.return_item_status2'] = 'rejected'
df3.loc[df3['rav_churn_model_rvp_base_v2_1_percent_v2.return_item_status'].str.contains('completed|requested|init',na = False), 'rav_churn_model_rvp_base_v2_1_percent_v2.return_item_status2'] = 'accepted'
df3.drop('rav_churn_model_rvp_base_v2_1_percent_v2.return_item_status', axis = 1, inplace = True)
df3.rename(columns = {"rav_churn_model_rvp_base_v2_1_percent_v2.return_item_status" : "rav_churn_model_rvp_base_v2_1_percent_v2.return_item_status"}, inplace = True)
df3.to_csv(r"X:\ISB\Capstone\Data\phase2 data\revised_data\april_customers_data_v4.csv")


### RTO formatting
df3 = pd.read_csv(r"X:\ISB\Capstone\Data\phase2 data\revised_data\april_customers_data_v4.csv")
fields_to_read = ['rav_churn_model_rtos_base_v1_1_percent_v2.order_item_id','rav_churn_model_rtos_base_v1_1_percent_v2.account_id','rav_churn_model_rtos_base_v1_1_percent_v2.promised_fse_sla','rav_churn_model_rtos_base_v1_1_percent_v2.rto_qty','rav_churn_model_rtos_base_v1_1_percent_v2.promise_update_flag','rav_churn_model_rtos_base_v1_1_percent_v2.courier_return_item_derived_reason','rav_churn_model_rtos_base_v1_1_percent_v2.reason_attribution','rav_churn_model_rtos_base_v1_1_percent_v2.deliver_date_key']
rto_data = pd.read_csv(r"X:\ISB\Capstone\Data\phase2 data\revised_data\RTO_1_29112017\RTO_1_29112017.csv", delimiter = '\t', usecols = fields_to_read)
rto_data.rename(columns = {"rav_churn_model_rtos_base_v1_1_percent_v2.order_item_id" : "sn_anurag_variables_v13_1_percent_v3.order_item_id"}, inplace = True)
rto_data['sn_anurag_variables_v13_1_percent_v3.order_item_id'] = rto_data['sn_anurag_variables_v13_1_percent_v3.order_item_id'].apply(lambda x: str(x)+"C")
df4 = df3.merge(rto_data, how = 'left', on = 'sn_anurag_variables_v13_1_percent_v3.order_item_id')
df4.to_csv(r"X:\ISB\Capstone\Data\phase2 data\revised_data\april_customers_data_v5.csv")