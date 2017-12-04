######### Required Inputs #########

model_data = 'Final Modelling Data -v5.csv'

model_data =read.delim(model_data, header = TRUE, sep = ",")
model_data =setDT(model_data)

VARIABLES_REMOVED = c('ID')
NUMERIC_THRESHOLD_MIN = 10
FACTOR_THRESHOLD_MAX = 20
TARGET_VAR = 'Churn'

######### Libraries #########

#install.packages("h2o")
#install.packages("sys")
#install.packages("ROSE")

library(data.table)
library(h2o)
library(sys)
library(ROSE)
library(randomForest)

######### Variables Formatting #########

for (var in names(model_data)) {
  len_unique = length(unique(subset(model_data[[var]], !is.na(model_data[[var]]))))
  print(paste(var, len_unique))
  
  if (len_unique > 1) {
    if (class(model_data[[var]]) == 'character' | class(model_data[[var]]) == 'factor' | class(model_data[[var]]) == 'Date') {
      model_data[[var]] <- as.factor(model_data[[var]])
      if (len_unique > FACTOR_THRESHOLD_MAX) {
        VARIABLES_REMOVED = c(VARIABLES_REMOVED, var)
      }
    } 
    else {
     if (len_unique < NUMERIC_THRESHOLD_MIN) {
       model_data[[var]] = as.factor(model_data[[var]])
       if (len_unique > FACTOR_THRESHOLD_MAX) {
         VARIABLES_REMOVED = c(VARIABLES_REMOVED, var)
       }
     } else {
     model_data[[var]] = as.numeric(model_data[[var]])
     }
    }
  } else {
    VARIABLES_REMOVED = c(VARIABLES_REMOVED, var)
  }
}

model_data = model_data[, (VARIABLES_REMOVED) := NULL]

######### Missing Value Treatment #########

for (var in names(model_data)) {
  if (class(model_data[[var]]) == 'factor' | class(model_data[[var]]) == 'character' | class(model_data[[var]]) == 'Date') {
    levels(model_data[[var]]) = c(levels(model_data[[var]]), 'missing')
    model_data[[var]][is.na(model_data[[var]])] = 'missing'
  } else {
    model_data[[var]][is.na(model_data[[var]])] = -999
  }
}

summ = summary(model_data)
write.csv(summ, 'Summary_Final.csv')

save(model_data, file = 'model_data_final.Rda')
