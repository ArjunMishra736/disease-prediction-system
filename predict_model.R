suppressMessages(library(randomForest))

model <- readRDS("model.rds")

args <- commandArgs(trailingOnly = TRUE)

# -------------------------------
# HANDLE NO ARGUMENT CASE (RStudio)
# -------------------------------
if (length(args) < 4) {
  print("⚠️ No input from command line, using test values")
  
  Age <- 25
  Gender <- 1
  Exercise <- 1
  BP <- 0
} else {
  Age      <- as.numeric(args[1])
  Gender   <- as.numeric(args[2])
  Exercise <- as.numeric(args[3])
  BP       <- as.numeric(args[4])
}

# -------------------------------
# CREATE INPUT
# -------------------------------
input <- data.frame(
  Age = Age,
  Gender = Gender,
  Exercise = Exercise,
  BP = BP
)

# -------------------------------
# SAFETY CHECK (VERY IMPORTANT)
# -------------------------------
if (any(is.na(input))) {
  stop("❌ Missing values detected in input")
}

# -------------------------------
# PREDICT
# -------------------------------
model_pred <- as.numeric(as.character(predict(model, input)))

# -------------------------------
# RULE-BASED FIX
# -------------------------------
# Healthy case → force LOW RISK
if (Exercise == 1 && BP == 0) {
  final_pred <- 0
}else if (BP == 0 && Exercise == 0) {
  final_pred <- 0
}else if(BP == 0 && Exercise == 1){
  final_pred <- 1
}else{
  final_pred<-1
}

# -------------------------------
# OUTPUT
# -------------------------------
cat(final_pred)