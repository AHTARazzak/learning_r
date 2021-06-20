# Understanding Factors

sex <- factor(c("male", "female", "female", "male"))

levels(sex)
nlevels(sex)

food <- factor(c("low", "high", "medium", "high", "low", "medium", "high"))
levels(food)

food <- factor(food, levels = c("low","medium","high"))
levels(food)

food <- factor(food, levels = c("low", "medium", "high"), ordered = TRUE)
levels(food)

min(food)

f <- factor(c(3.4, 1.2, 5))
as.numeric(f)
f <-levels(f)[f]
f <- as.numeric(f)

dat <- read.csv(file="sample.csv", stringsAsFactors = TRUE)

str(dat)

summary(dat)

barplot(table(dat$Group))

barplot(table(dat$Gender))

dat$Gender[dat$Gender == "M"] <- "m"

plot(x = dat$Gender, y = dat$BloodPressure)
levels(dat$Gender)

dat$Gender <- droplevels(dat$Gender)
plot(x = dat$Gender, y = dat$BloodPressure)

levels(dat$Gender)[2] <- 'f'
plot(x = dat$Gender, y = dat$BloodPressure)
