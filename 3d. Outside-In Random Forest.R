######### Required Inputs #########

load(file = "model_data_final.Rda")

######### Libraries #########

#install.packages("h2o")
#install.packages("sys")
#install.packages("ROSE")
#install.packages("xgboost")

library(data.table)
library(h2o)
library(sys)
library(ROSE)
library(randomForest)
library(xgboost)

######### Modelling - Random Forest #########

class(model_data$Churn)
levels(model_data$Churn)
model_data$Churn <- factor(model_data$Churn)
levels(model_data$Churn)

rf = randomForest(Churn ~., data = model_data, importance = TRUE)

imp = importance(rf)
imp = imp[, 'MeanDecreaseAccuracy']
imp = imp[order(-imp)]
imp
yact = model_data$Churn
yhat = predict(rf)
mean_error = mean(yhat != yact)
mean_error
accuracy = 1 - mean_error
accuracy
table(yhat, yact)
