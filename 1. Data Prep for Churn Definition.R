cat('\014')
rm(list = ls())

#install.packages("infotheo")
#install.packages("ROCR")
#install.packages("AUC")

library(randomForest)
library(infotheo)
library(ROCR)
library(AUC)
library(dplyr)
library(sqldf)

output_file = 'SmallerSampleData.csv'

all_data =read.delim(output_file, header = TRUE, sep = "\t")

head(all_data)

all_data_1 <- select(all_data, sn_anurag_variables_v5.account_id,
                     sn_anurag_variables_v5.order_id,
                     sn_anurag_variables_v5.order_item_unit_id,
                     sn_anurag_variables_v5.gmv,
                     sn_anurag_variables_v5.order_item_approve_max_date_key,
                     sn_anurag_variables_v5.first_purchase_date,
                     sn_anurag_variables_v5.newcust_flag)
colnames(all_data_1) <- c("CustomerID", "OrderID", "OrderItemID", "Amount", "OrderDate", "CustomerStartDate", "NewCustomerFlag")

all_data_2 <- sqldf("select
                      CustomerID,
                      OrderID,
                      COUNT(OrderItemID) as Quantity,
                      SUM(Amount) as Amount,
                      MAX(OrderDate) as OrderDate,
                      MAX(CustomerStartDate) as CustomerStartDate,
                      MAX(NewCustomerFlag) as NewCustomerFlag
                    from all_data_1
                    group by
                    OrderID")

write.csv(all_data_2, file = "SmallData.csv")
