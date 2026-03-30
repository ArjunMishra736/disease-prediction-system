source("load_dataset.R")

print("🔄 Starting Data Preprocessing...")

# -------------------------------
# CLEAN COLUMN NAMES
# -------------------------------
colnames(data) <- trimws(colnames(data))
colnames(data) <- gsub(" ", "_", colnames(data))

# -------------------------------
# STANDARDIZE IMPORTANT COLUMNS
# -------------------------------
rename_safe <- function(pattern, new_name) {
  col <- grep(pattern, colnames(data), ignore.case = TRUE, value = TRUE)[1]
  if (!is.na(col)) {
    colnames(data)[colnames(data) == col] <- new_name
  }
}

rename_safe("age", "Age")
rename_safe("gender", "Gender")
rename_safe("exercise", "Exercise")
rename_safe("bp", "BP")
rename_safe("disease", "Disease")

# -------------------------------
# CONVERT TO NUMERIC (IMPORTANT)
# -------------------------------
convert_binary <- function(x) {
  ifelse(tolower(x) == "yes", 1, 0)
}

# Gender
if ("Gender" %in% colnames(data)) {
  data$Gender <- ifelse(tolower(data$Gender) == "male", 1, 0)
}

# BP & Disease already numeric → ensure numeric
data$BP <- as.numeric(data$BP)
data$Disease <- as.numeric(data$Disease)

# -------------------------------
# HANDLE MISSING VALUES
# -------------------------------
data[is.na(data)] <- 0

print("✅ Preprocessing Completed")
print(colnames(data))