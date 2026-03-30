source("preprocessing.R")

print("📊 Running Experiment 2")

# Show 2 plots together
par(mfrow = c(1,2))

# AGE HISTOGRAM
hist(data$Age,
     col = "blue",
     main = "Age Distribution",
     xlab = "Age",
     ylab = "Frequency")

# DISEASE BARPLOT
print(table(data$Disease))

barplot(table(data$Disease),
        col = c("green","blue"),
        main = "Disease Distribution",
        xlab = "Disease (0/1)",
        ylab = "Count")

# FIXED PRINT
print(paste("NA count:", sum(is.na(data))))

print("✅ Experiment 2 Completed")