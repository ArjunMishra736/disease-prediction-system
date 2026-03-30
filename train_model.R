library(randomForest)
library(caret)

source("preprocessing.R")

print("🤖 Training Model...")

# -------------------------------
# SELECT FEATURES
# -------------------------------
model_data <- data[, c("Age","Gender","Exercise","BP","Disease")]

# Convert target
model_data$Disease <- as.factor(model_data$Disease)

# -------------------------------
# SPLIT
# -------------------------------
set.seed(123)
trainIndex <- createDataPartition(model_data$Disease, p = 0.8, list = FALSE)

train <- model_data[trainIndex, ]
test  <- model_data[-trainIndex, ]

# -------------------------------
# TRAIN (IMPORTANT CHANGE HERE)
# -------------------------------
x_train <- train[, c("Age","Gender","Exercise","BP")]
y_train <- train$Disease

model <- randomForest(x = x_train, y = y_train)

print("✅ Model Trained")

# -------------------------------
# TEST
# -------------------------------
x_test <- test[, c("Age","Gender","Exercise","BP")]
pred <- predict(model, x_test)

cm <- confusionMatrix(pred, test$Disease)

print(cm)

# -------------------------------
# SAVE
# -------------------------------
saveRDS(model, "model.rds")

print("✅ Model Saved")
