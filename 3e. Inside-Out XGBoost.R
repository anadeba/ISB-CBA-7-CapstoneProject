cat('\014')
rm(list = ls())

###################Import libraries and Final Data####################
setwd("F:/CBA/Capstone")
library('dplyr')
library(randomForest)
library(e1071)
library(xgboost)

output_file = 'Final Modelling Data -v5.csv'
final_data = read.csv(output_file, header = TRUE)
head(final_data)

class(final_data$Churn)
final_data$Churn = as.factor(as.character(final_data$Churn))

for(col in colnames(final_data)){
  print(col)
  print(sum(length(which(is.na(final_data[,col])))))
}

# ?randomForest()
# colnames(final_data[,c(1,2)])



initial_feature_list = c("Churn","SalesChannel","ServiceProfile","Discount.","DeliveryFee","CityTier","BusinessUnit",
                         "SuperCategory","Persona","NewCustomer","Tenure","PaymentMethod","SellerTier","OverallSellerRatingCount",
                         "OverallSellerRating","CSContacted","IssueType","ReturnedFlag","ReturnReason","return_request_channel",
                         "return_reason_bucket","return_action","return_item_status","RTOed","RTODerivedReason","RTOReasonAttribution")

initial_rf_data = final_data[,initial_feature_list]
for(col in colnames(initial_rf_data)){
  print(col)
  print(sum(length(which(is.na(initial_rf_data[,col])))))
}

rf = randomForest(Churn ~., data = initial_rf_data, importance = TRUE, na.action=na.omit)

imp = importance(rf)
imp = imp[, 'MeanDecreaseAccuracy']
imp = imp[order(-imp)]
names(imp)

initial_rf_data = initial_rf_data[complete.cases(initial_rf_data),]

yact = initial_rf_data[, 1]
yhat = predict(rf,initial_rf_data[,-1])
test_df = as.data.frame(yact,yhat)
mean_error = mean(yhat != yact)
mean_error
accuracy = 1 - mean_error
accuracy
table(yhat, yact)

################# Data transformation ########################
library(psych)

levels(unique(initial_rf_data$ServiceProfile))
serviceprofile_dummies = dummy.code(initial_rf_data$ServiceProfile)
serviceprofile_dummies = as.data.frame(serviceprofile_dummies)
initial_rf_data = cbind(initial_rf_data,serviceprofile_dummies)

levels(unique(initial_rf_data$CityTier))
citytier_dummies = as.data.frame(dummy.code(initial_rf_data$CityTier))
initial_rf_data = cbind(initial_rf_data,citytier_dummies)

levels(unique(initial_rf_data$BusinessUnit))
businessunit_dummies = as.data.frame(dummy.code(initial_rf_data$BusinessUnit))
colnames(businessunit_dummies)
initial_rf_data = cbind(initial_rf_data,businessunit_dummies)
sum(length(which(initial_rf_data$V1 == 1)))
names(initial_rf_data)[names(initial_rf_data) == 'V1'] = 'Missing_BusinessUnit'

# levels(unique(initial_rf_data$SuperCategory))
# sum(length(levels(unique(initial_rf_data$SuperCategory))))
# SuperCategory_dummies = as.data.frame(dummy.code(initial_rf_data$BusinessUnit))
# colnames(SuperCategory_dummies)
# initial_rf_data = cbind(initial_rf_data,SuperCategory_dummies)
# sum(length(which(initial_rf_data$V1 == 1)))

levels(unique(initial_rf_data$Persona))
persona_dummies = as.data.frame(dummy.code(initial_rf_data$Persona))
colnames(persona_dummies)
initial_rf_data = cbind(initial_rf_data,persona_dummies)

levels(unique(initial_rf_data$PaymentMethod))
payment_dummies = as.data.frame(dummy.code(initial_rf_data$PaymentMethod))
initial_rf_data = cbind(initial_rf_data,payment_dummies)

levels(unique(initial_rf_data$SellerTier))
sellertier_dummies = as.data.frame(dummy.code(initial_rf_data$SellerTier))
initial_rf_data = cbind(initial_rf_data,sellertier_dummies)

levels(unique(initial_rf_data$return_request_channel)) #4 factors
return_request_channel_dummies = as.data.frame(dummy.code(initial_rf_data$return_request_channel))
names(return_request_channel_dummies)
initial_rf_data = cbind(initial_rf_data,return_request_channel_dummies)
names(initial_rf_data)[names(initial_rf_data) == 'V1'] = 'Missing_return_req_channel'

levels(unique(initial_rf_data$ReturnReason)) #20 factors
returnReason_channel_dummies = as.data.frame(dummy.code(initial_rf_data$ReturnReason))
names(returnReason_channel_dummies)
initial_rf_data = cbind(initial_rf_data,returnReason_channel_dummies)
names(initial_rf_data)[names(initial_rf_data) == 'V1'] = 'Missing_ReturnReason'

levels(unique(initial_rf_data$return_reason_bucket)) #5 factors
returnReason_bucket_dummies = as.data.frame(dummy.code(initial_rf_data$return_reason_bucket))
names(returnReason_bucket_dummies)
initial_rf_data = cbind(initial_rf_data,returnReason_bucket_dummies)
names(initial_rf_data)[names(initial_rf_data) == 'V1'] = 'Missing_ReturnReason_Bucket'

levels(unique(initial_rf_data$return_action))# 4 facors
return_action_dummies = as.data.frame(dummy.code(initial_rf_data$return_action))
names(returnReason_bucket_dummies)
initial_rf_data = cbind(initial_rf_data,returnReason_bucket_dummies)
names(initial_rf_data)[names(initial_rf_data) == 'V1'] = 'Return_action_missing'



# levels(unique(initial_rf_data$IssueType)) #32 factors





####################################Feature_Selection#############################
exclude_feature_list = c("ServiceProfile","CityTier","BusinessUnit","Persona","PaymentMethod","SellerTier","IssueType",
                         "ReturnReason","return_request_channel","return_reason_bucket","return_action",
                         "return_item_status","RTODerivedReason","RTOReasonAttribution","SuperCategory")

final_subset_xgboost = initial_rf_data[,!names(initial_rf_data) %in% exclude_feature_list]

#### Data Partition ####
set.seed(1234)
ind = sample(2, nrow(final_subset_xgboost), replace = T, prob = c(0.8,0.2))
train_data = final_subset_xgboost[ind == 1,]
test_data = final_subset_xgboost[ind == 2,]
train_label = train_data[,"Churn"]

# #Parameter
# nc = length(unique(train_label))
# xgb_params = list()
# 
# watch_list = list(train = as.matrix(train_data), test = as.matrix(test_data))
# # class(target_var)
# # target_var = as.factor(as.character(final_subset_xgboost$Churn))
xgb_model = xgboost(data = data.matrix(train_data[,-1]), label = train_label,
                    eta = 0.1,
                    max_depth = 15,
                    nround = 25,
                    subsample = 0.5,
                    colsample_bytree = 0.5,
                    seed = 1,
                    eval_metric = "merror",
                    objective = "multi:softmax",
                    num_class = 3,
                    nthread = 3)
#########################Train data Accuracy ###################################

yact_xgboost_train = train_data[,1]
yhat_xgboost_train = predict(xgb_model,data.matrix(train_data[,-1]))
yhat_xgboost_train = yhat_xgboost_train - 1
mean_error_train = mean(yhat_xgboost_train != yact_xgboost_train)
mean_error_train
accuracy_train = 1 - mean_error_train
accuracy_train #82%
table(yact_xgboost_train, yhat_xgboost_train)


#########################Test data Accuracy ####################################
yact_xgboost = test_data[,1]
yhat_xgboost = predict(xgb_model, data.matrix(test_data[,-1]))
yhat_xgboost = yhat_xgboost - 1
mean_error = mean(yhat_xgboost != yact_xgboost)
mean_error
accuracy = 1 - mean_error
accuracy #75%
table(yact_xgboost, yhat_xgboost)

###################error plots #################################################
e = data.frame(xgb_model$evaluation_log)
plot(e$iter,e$train_merror, col = 'blue')

#######################Features importance #####################################
imp_features = xgb.importance(colnames(train_data),model = xgb_model)
xgb.plot.importance(imp_features)
