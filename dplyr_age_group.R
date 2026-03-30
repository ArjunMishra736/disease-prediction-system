library(dplyr)
source("preprocessing.R")

print("⚙️ Running Experiment 3")

# Count
print(data %>% count(Disease))

# Grouping
result <- data %>%
  group_by(Disease) %>%
  summarise(avg_age = mean(Age))

print(result)

# New column
data <- data %>%
  mutate(Age_Group = ifelse(Age > 40, "Senior", "Young"))

print(head(data))

print("✅ Experiment 3 Completed")