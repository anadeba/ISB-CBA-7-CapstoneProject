cat('\014')
rm(list = ls())


library(randomForest)
library(infotheo)
library(ROCR)
library(AUC)


MCMC_LIMIT = 200
REMOVE_OTHER_PP = TRUE
#class_wts = c(1.5, 2.3, 1)
#class_wts = c(1, 1, 1)

output_file = 'data_processed_csv.csv'
objectives = c("last_flipkart_rating", "flipkart_rating", "last_amazon_rating", "flipkart_recommend", "amazon_recommend", "none_recommend", "preferred_portal", "binary_pp", 
               "binary_flipkart_rating", "binary_last_flipkart_rating", "binary_flipkart_recommend",
               "binary_2_flipkart_rating", "binary_2_last_flipkart_rating", "binary_2_flipkart_recommend", 
               "binary_3_flipkart_rating", "binary_3_last_flipkart_rating", "binary_3_flipkart_recommend", 
               "trinary_flipkart_rating", "trinary_last_flipkart_rating", "trinary_flipkart_recommend",
               "linear_flipkart_rating", "linear_last_flipkart_rating", "linear_flipkart_recommend")

all_data = read.csv(output_file, header = TRUE)
all_data = all_data[, !names(all_data) %in% c('start_dt', 'end_dt')]
all_data[, 'binary_pp'] = ifelse(all_data$preferred_portal == 'Flipkart', 1, ifelse(all_data$preferred_portal == 'Amazon', 0, -999))
all_data[, 'differential_pricing'] = as.factor(as.integer(all_data[, 'flipkart_pricing']) - as.integer(all_data[, 'amazon_pricing']))
all_data[, 'differential_selection'] = as.factor(as.integer(all_data[, 'flipkart_selection']) - as.integer(all_data[, 'amazon_selection']))
all_data[, 'differential_product_quality'] = as.factor(as.integer(all_data[, 'flipkart_product_quality']) - as.integer(all_data[, 'amazon_product_quality']))
all_data[, 'differential_navigation'] = as.factor(as.integer(all_data[, 'flipkart_navigation']) - as.integer(all_data[, 'amazon_navigation']))
all_data[, 'differential_delivery_quality'] = as.factor(as.integer(all_data[, 'flipkart_delivery_quality']) - as.integer(all_data[, 'amazon_delivery_quality']))
all_data[, 'differential_delivery_speed'] = as.factor(as.integer(all_data[, 'flipkart_delivery_speed']) - as.integer(all_data[, 'amazon_delivery_speed']))
all_data[, 'differential_payment'] = as.factor(as.integer(all_data[, 'flipkart_payment']) - as.integer(all_data[, 'amazon_payment']))
all_data[, 'differential_discoverability'] = as.factor(as.integer(all_data[, 'flipkart_discoverability']) - as.integer(all_data[, 'amazon_discoverability']))
all_data[, 'differential_returns'] = as.factor(as.integer(all_data[, 'flipkart_returns']) - as.integer(all_data[, 'amazon_returns']))
all_data_backup = all_data

sink('All_Objective_Functions_Output.txt')

for (obj in c("binary_flipkart_rating", "binary_last_flipkart_rating", "binary_flipkart_recommend", "binary_2_flipkart_rating", "binary_2_last_flipkart_rating", "binary_2_flipkart_recommend", "binary_3_flipkart_rating", "binary_3_last_flipkart_rating", "binary_3_flipkart_recommend", "trinary_flipkart_rating", "trinary_last_flipkart_rating", "trinary_flipkart_recommend", "linear_flipkart_rating", "linear_last_flipkart_rating", "linear_flipkart_recommend")) {
  print("----------")
  print("----------")
  print(obj)
  all_data = all_data_backup
  if (obj == 'binary_flipkart_rating') {
    binary_flipkart_rating = all_data$flipkart_rating - 3
    all_data[, 'binary_flipkart_rating'] = ifelse(binary_flipkart_rating < 0, 0, ifelse(binary_flipkart_rating > 0, 1, -999))
    all_data = all_data[(!is.na(all_data$binary_flipkart_rating)) & (all_data$binary_flipkart_rating == 0 | all_data$binary_flipkart_rating == 1), ]
    all_data$binary_flipkart_rating = as.factor(all_data$binary_flipkart_rating)
  }
  
  if (obj == 'binary_flipkart_recommend') {
    binary_flipkart_recommend = all_data$flipkart_recommend - 3
    all_data[, 'binary_flipkart_recommend'] = ifelse(binary_flipkart_recommend < 0, 0, ifelse(binary_flipkart_recommend > 0, 1, -999))
    all_data = all_data[(!is.na(all_data$binary_flipkart_recommend)) & (all_data$binary_flipkart_recommend == 0 | all_data$binary_flipkart_recommend == 1), ]
    all_data$binary_flipkart_recommend = as.factor(all_data$binary_flipkart_recommend)
  }
  
  if (obj == 'binary_last_flipkart_rating') {
    binary_last_flipkart_rating = all_data$last_flipkart_rating - 3
    all_data[, 'binary_last_flipkart_rating'] = ifelse(binary_last_flipkart_rating < 0, 0, ifelse(binary_last_flipkart_rating > 0, 1, -999))
    all_data = all_data[(!is.na(all_data$binary_last_flipkart_rating)) & (all_data$binary_last_flipkart_rating == 0 | all_data$binary_last_flipkart_rating == 1), ]
    all_data$binary_last_flipkart_rating = as.factor(all_data$binary_last_flipkart_rating)
  }
    
  if (obj == 'binary_2_flipkart_rating') {
    binary_2_flipkart_rating = all_data$flipkart_rating - 3
    all_data[, 'binary_2_flipkart_rating'] = ifelse(binary_2_flipkart_rating <= 0, 0, ifelse(binary_2_flipkart_rating > 0, 1, -999))
    all_data = all_data[(!is.na(all_data$binary_2_flipkart_rating)) & (all_data$binary_2_flipkart_rating == 0 | all_data$binary_2_flipkart_rating == 1), ]
    all_data$binary_2_flipkart_rating = as.factor(all_data$binary_2_flipkart_rating)
  }

  if (obj == 'binary_2_flipkart_recommend') {
    binary_2_flipkart_recommend = all_data$flipkart_recommend - 3
    all_data[, 'binary_2_flipkart_recommend'] = ifelse(binary_2_flipkart_recommend <= 0, 0, ifelse(binary_2_flipkart_recommend > 0, 1, -999))
    all_data = all_data[(!is.na(all_data$binary_2_flipkart_recommend)) & (all_data$binary_2_flipkart_recommend == 0 | all_data$binary_2_flipkart_recommend == 1), ]
    all_data$binary_2_flipkart_recommend = as.factor(all_data$binary_2_flipkart_recommend)
  }

  if (obj == 'binary_2_last_flipkart_rating') {
    binary_2_last_flipkart_rating = all_data$last_flipkart_rating - 3
    all_data[, 'binary_2_last_flipkart_rating'] = ifelse(binary_2_last_flipkart_rating <= 0, 0, ifelse(binary_2_last_flipkart_rating > 0, 1, -999))
    all_data = all_data[(!is.na(all_data$binary_2_last_flipkart_rating)) & (all_data$binary_2_last_flipkart_rating == 0 | all_data$binary_2_last_flipkart_rating == 1), ]
    all_data$binary_2_last_flipkart_rating = as.factor(all_data$binary_2_last_flipkart_rating)
  }
    
  if (obj == 'binary_3_flipkart_rating') {
    binary_3_flipkart_rating = all_data$flipkart_rating - 3
    all_data[, 'binary_3_flipkart_rating'] = ifelse(binary_3_flipkart_rating < 0, 0, ifelse(binary_3_flipkart_rating >= 0, 1, -999))
    all_data = all_data[(!is.na(all_data$binary_3_flipkart_rating)) & (all_data$binary_3_flipkart_rating == 0 | all_data$binary_3_flipkart_rating == 1), ]
    all_data$binary_3_flipkart_rating = as.factor(all_data$binary_3_flipkart_rating)
  }
  
  if (obj == 'binary_3_flipkart_recommend') {
    binary_3_flipkart_recommend = all_data$flipkart_recommend - 3
    all_data[, 'binary_3_flipkart_recommend'] = ifelse(binary_3_flipkart_recommend < 0, 0, ifelse(binary_3_flipkart_recommend >= 0, 1, -999))
    all_data = all_data[(!is.na(all_data$binary_3_flipkart_recommend)) & (all_data$binary_3_flipkart_recommend == 0 | all_data$binary_3_flipkart_recommend == 1), ]
    all_data$binary_3_flipkart_recommend = as.factor(all_data$binary_3_flipkart_recommend)
  }

  if (obj == 'binary_3_last_flipkart_rating') {
    binary_3_last_flipkart_rating = all_data$last_flipkart_rating - 3
    all_data[, 'binary_3_last_flipkart_rating'] = ifelse(binary_3_last_flipkart_rating < 0, 0, ifelse(binary_3_last_flipkart_rating >= 0, 1, -999))
    all_data = all_data[(!is.na(all_data$binary_3_last_flipkart_rating)) & (all_data$binary_3_last_flipkart_rating == 0 | all_data$binary_3_last_flipkart_rating == 1), ]
    all_data$binary_3_last_flipkart_rating = as.factor(all_data$binary_3_last_flipkart_rating)
  }
    
  if (obj == 'trinary_flipkart_rating') {
    trinary_flipkart_rating = all_data$flipkart_rating - 3
    all_data[, 'trinary_flipkart_rating'] = ifelse(trinary_flipkart_rating < 0, -1, ifelse(trinary_flipkart_rating > 0, 1, 0))
    all_data = all_data[!is.na(all_data$trinary_flipkart_rating), ]
    all_data$trinary_flipkart_rating = as.factor(all_data$trinary_flipkart_rating)
  }

  if (obj == 'trinary_flipkart_recommend') {
    trinary_flipkart_recommend = all_data$flipkart_recommend - 3
    all_data[, 'trinary_flipkart_recommend'] = ifelse(trinary_flipkart_recommend < 0, -1, ifelse(trinary_flipkart_recommend > 0, 1, 0))
    all_data = all_data[!is.na(all_data$trinary_flipkart_recommend), ]
    all_data$trinary_flipkart_recommend = as.factor(all_data$trinary_flipkart_recommend)
  }

  if (obj == 'trinary_last_flipkart_rating') {
    trinary_last_flipkart_rating = all_data$last_flipkart_rating - 3
    all_data[, 'trinary_last_flipkart_rating'] = ifelse(trinary_last_flipkart_rating < 0, -1, ifelse(trinary_last_flipkart_rating > 0, 1, 0))
    all_data = all_data[!is.na(all_data$trinary_last_flipkart_rating), ]
    all_data$trinary_last_flipkart_rating = as.factor(all_data$trinary_last_flipkart_rating)
  }
  
  if (obj == 'linear_flipkart_rating') {
    all_data$linear_flipkart_rating = as.numeric(all_data$flipkart_rating)
    all_data = all_data[!is.na(all_data$linear_flipkart_rating), ]
  }
  
  if (obj == 'linear_flipkart_recommend') {
    all_data$linear_flipkart_recommend = as.numeric(all_data$flipkart_recommend)
    all_data = all_data[!is.na(all_data$linear_flipkart_recommend), ]
  }
  
  if (obj == 'linear_last_flipkart_rating') {
    all_data$linear_last_flipkart_rating = as.numeric(all_data$last_flipkart_rating)
    all_data = all_data[!is.na(all_data$linear_last_flipkart_rating), ]
  }
  
  
  features_data = all_data[, !names(all_data) %in% objectives]
  features_bad_exp = all_data[, names(all_data) %in% c("last_bad_exp1", "last_bad_exp2", "last_bad_exp3","last_bad_exp4", "last_bad_exp5", "last_bad_exp6", "last_bad_exp7", "last_bad_exp8","last_bad_exp9", "last_bad_exp10", "last_bad_exp11", "last_bad_exp12")]
  features_perf = all_data[names(all_data) %in% c("flipkart_pricing", "amazon_pricing", "none_pricing", "flipkart_selection", "amazon_selection","none_selection", "flipkart_product_quality", "amazon_product_quality", "none_product_quality", "flipkart_navigation","amazon_navigation", "none_navigation", "flipkart_payment", "amazon_payment", "none_payment","flipkart_delivery_quality", "amazon_delivery_quality", "none_delivery_quality", "flipkart_delivery_speed", "amazon_delivery_speed","none_delivery_speed", "flipkart_returns", "amazon_returns", "none_returns", "flipkart_discoverability","amazon_discoverability", "none_discoverability", "differential_pricing", "differential_selection", "differential_product_quality", "differential_payment", "differential_returns", "differential_delivery_quality", "differential_delivery_speed", "differential_navigation", "differential_discoverability")]
  features_exp_perf = cbind(features_bad_exp, features_perf)
  
  objective_data = all_data[, names(all_data) %in% objectives]
  input_data = features_exp_perf
  
  head(input_data)
  head(objective_data)
  dim(input_data)
  dim(objective_data)
  
  
  for (col in colnames(input_data)) {
    #print(col)
    input_data[, col] = as.integer(input_data[, col])
    input_data[is.na(input_data[, col]), col] = -999
    input_data[, col] = as.factor(input_data[, col])
    #print(levels(input_data[, col]))
    #print(class(input_data[, col]))
  }
  
  
  for (col in colnames(objective_data)) {
    #print(col)
    objective_data[, col] = as.integer(objective_data[, col])
    objective_data[is.na(objective_data[, col]), col] = -999
    objective_data[, col] = as.factor(objective_data[, col])
    #print(levels(objective_data[, col]))
    #print(class(objective_data[, col]))
  }
  
  
  ##################################################################################
  ############################### Modelling ########################################
  ##################################################################################
  
  exclude_vars = c('last_bad_exp3')
  #exclude_vars = c()
  grouped_vars = list()
  grouped_vars[[1]] = c('flipkart_delivery_speed',	'amazon_delivery_speed',	'none_delivery_speed',	'last_bad_exp1', 'differential_delivery_speed')
  grouped_vars[[2]] = c('flipkart_selection',	'amazon_selection',	'none_selection',	'last_bad_exp2', 'differential_selection')
  grouped_vars[[3]] = c('flipkart_returns',	'amazon_returns',	'none_returns',	'last_bad_exp4', 'differential_returns')
  grouped_vars[[4]] = c('flipkart_discoverability',	'amazon_discoverability',	'none_discoverability',	'last_bad_exp5', 'differential_discoverability')
  grouped_vars[[5]] = c('flipkart_pricing',	'amazon_pricing',	'none_pricing',	'last_bad_exp6', 'differential_pricing')
  grouped_vars[[6]] = c('flipkart_payment',	'amazon_payment',	'none_payment',	'last_bad_exp7', 'differential_payment')
  grouped_vars[[7]] = c('flipkart_delivery_quality',	'amazon_delivery_quality',	'none_delivery_quality', 'differential_delivery_quality')
  grouped_vars[[8]] = c('flipkart_product_quality',	'amazon_product_quality',	'none_product_quality', 'differential_product_quality')
  grouped_vars[[9]] = c('flipkart_navigation',	'amazon_navigation',	'none_navigation', 'differential_navigation')
  
  
  target_col = obj
  target_var = objective_data[, target_col]
  print(table(target_var))
  model_data1 = cbind(target_var, input_data)
  colnames(model_data1)[1] = target_col
  model_data = model_data1[, !names(model_data1) %in% exclude_vars]
  if (obj %in% c('linear_flipkart_rating', 'linear_last_flipkart_rating', 'linear_flipkart_recommend')) {
    model_data[, obj] = as.numeric(model_data[, obj])
  }
  all_vars = names(model_data)
  rf = eval(parse(text = paste("randomForest(", target_col, " ~ ., data = model_data, importance = TRUE)", sep = '')))
  
  imp = importance(rf)
  if (obj %in% c('linear_flipkart_rating', 'linear_last_flipkart_rating', 'linear_flipkart_recommend')) {
    imp = imp[, '%IncMSE']
  } else {
    imp = imp[, 'MeanDecreaseAccuracy']
  }
  imp = imp[order(-imp)]
  ignore_list = c()
  
  for (var in names(imp)) {
    if (!var %in% ignore_list) {
      for (group_iter in 1:length(grouped_vars)) {
        group_list = grouped_vars[[group_iter]]
        if (var %in% group_list) {
          ignore_list = c(ignore_list, group_list)
          remove_vars = group_list[!group_list == var]
          exclude_vars = c(exclude_vars, remove_vars)
          break
        }
      }
    }
  }
  
  exclude_vars = unique(exclude_vars)
  final_vars = all_vars[!all_vars %in% exclude_vars]
  model_data1 = cbind(target_var, input_data)
  colnames(model_data1)[1] = target_col
  model_data = model_data1[, names(model_data1) %in% final_vars]
  if (obj %in% c('linear_flipkart_rating', 'linear_last_flipkart_rating', 'linear_flipkart_recommend')) {
    model_data[, obj] = as.numeric(model_data[, obj])
  }
  rf = eval(parse(text = paste("randomForest(", target_col, " ~ ., data = model_data, importance = TRUE)", sep = '')))
  
  imp1 = importance(rf)
  if (obj %in% c('linear_flipkart_rating', 'linear_last_flipkart_rating', 'linear_flipkart_recommend')) {
    imp1 = imp1[, '%IncMSE']
  } else {
    imp1 = imp1[, 'MeanDecreaseAccuracy']
  }
  imp1 = imp1[order(-imp1)]
  
  yact = model_data[, target_col]
  yhat = predict(rf)
  if (obj %in% c('linear_flipkart_rating', 'linear_last_flipkart_rating', 'linear_flipkart_recommend')) {
    yhat = round(yhat)
  }
  
  mean_error = mean(yhat != yact)
  accuracy = 1 - mean_error
  roc_obj = roc(as.factor(yhat), as.factor(yact))

  print(mean_error)
  print(accuracy)
  print(table(yhat, yact))
  print(auc(roc_obj))
  
  for (imp_iter in 1:length(imp1)) {
    print(paste(names(imp1)[imp_iter], imp1[imp_iter]))
  }

}

sink()
