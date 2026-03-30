source("preprocessing.R")

print("🔬 Running Experiment 1")

# String
print(nchar(as.character(data$Age)))
print(paste(data$Age, data$Gender))

# Stats
print(sum(data$Age))
print(mean(data$Age))
print(min(data$Age))
print(max(data$Age))

# Classification (UPDATED FOR YOUR DATASET)
data$Level <- ifelse(data$BP == 1 & data$Disease == 1, "Severe",
                     ifelse(data$BP == 1, "Mild", "Normal"))

print(head(data$Level))

print("✅ Experiment 1 Completed")