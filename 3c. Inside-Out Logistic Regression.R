
######### Logistic Regression Model1 - All Variables #########

logistic.model<-glm(Churn ~., data = model_data,family = "binomial")

######### Logistic Regression Model2 - Actionable Variables #########

logistic.model<-glm(Churn ~Discount.+ReturnReason+OverallProdRating+PromisedSLA+DeliveryTAT+OverallSellerRating+SellerTier+DeliveryFee+CSTAT+CSContacted+PromiseUpdateFlag+NewCustomer+return_item_status+return_action+RTOReasonAttribution+return_reason_bucket+Breach+ReturnedFlag+RTOed+TRRFlag+RRFlag, data = model_data,family = "binomial")

######### Logistic Regression Model3 - Cleaned Variables #########

logistic.model<-glm(Churn ~Discount.+ReturnReason+OverallProdRating+PromisedSLA+OverallSellerRating+SellerTier+DeliveryFee+CSTAT+CSContacted+PromiseUpdateFlag+NewCustomer+RTOReasonAttribution+Breach+TRRFlag, data = model_data,family = "binomial")
summary(logistic.model)

#install.packages("ResourceSelection")

library(ResourceSelection)
hoslem.test(model_data$Churn, fitted(logistic.model))

## Confusion Matrix

predict <- predict(logistic.model, model_data, type = 'response')
#View(predict)
table(model_data$Churn, predict > 0.5)

#install.packages("pROC")
library(pROC)
roccurve <- roc(model_data$Churn ~ predict)
plot(roccurve)
auc(roccurve)
