setwd("/Users/alirazzak/Desktop/Code/learning/rstudio_learn/swcarpentry")

dat <- read.csv(file = 'sample.csv', header = TRUE, stringsAsFactors = FALSE)
class(dat)

str(dat)

head(dat)

dim(dat)

dat[,6:9]

dat[c(1, 5, 7, 9), 1:5]

dat$Gender
class(dat$Gender)
class(dat$BloodPressure)
head(dat[,c("Age", "Gender")])

dat2 <- read.csv(file='sample.csv', header = TRUE, stringsAsFactors = FALSE, row.names = 1)
rownames(dat2)

dat2["Sub072", ]

dat2[c("Sub009", "Sub072"), ]

dat2 <- read.csv(file = 'data/sample.csv', header = TRUE, stringsAsFactors = FALSE, row.names=3)

c(TRUE, TRUE, FALSE, FALSE, TRUE)

x <- c(1, 2, 3, 11, 12, 13)
x <- 10

x %in% 1:10
index <- dat$Group == "Control"
dat$Group
dat[index, ]$BloodPressure
plot(dat[dat$Group == 'Control', ]$BloodPressure)

plot(dat[dat$Group != 'Control', ]$BloodPressure)

x <- c(1, 2, 3, 11, 12, 13)
x[x < 10] <- 0
x

dat$Gender
dat[dat$Gender == "M", ]$Gender <- "m"
dat[dat$Gender == "F", ]$Gender <- "f"

#Data in data frames addressed by index by logical vector, or by name
#Use $ operator to address column by name