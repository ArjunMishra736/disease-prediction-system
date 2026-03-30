# -------------------------------
# SET WORKING DIRECTORY (OPTIONAL)
# -------------------------------
# Uncomment this only if needed
# setwd("C:/Users/anind/OneDrive/Documents/SOFTWARE X PDS/PDS")

# -------------------------------
# LOAD DATASET
# -------------------------------
data <- read.csv("Dataset.csv", stringsAsFactors = FALSE)

# -------------------------------
# CHECK DATA
# -------------------------------
print("✅Dataset Loaded Successfully")

# Show first few rows
print(head(data))

# Show structure
print(" Structure of Dataset:")
str(data)

# Show summary
print(" Summary of Dataset:")
print(summary(data))
