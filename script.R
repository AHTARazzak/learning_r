#reading in CSV
dat <- read.csv(file = "inflammation-01.csv", header = FALSE)

#Defining a variable
weight_kg <- 57.5

#Making a function
make_kg_lb <- function(amount) {
  in_lb <- amount * 2.2
  return(in_lb)
}

#Calling a function
make_kg_lb(weight_kg)

Investigating a dataframe
head(dat)

#Playing with variables
mass <- 47.5
age <- 122
mass <- mass *2.0
age <- age -20

#Different ways of inspecting dataframes
class(dat)
dim(dat)
dat[1,1]
dat[30,20]

#Combining rows & columns from dataframes
dat[c(1, 3, 5), c(10, 20)]
#Slices
1:5
3:12
dat[1:3,1:3]
dat[1:3,1:10]
dat[1:5,1:10]
dat[5,]
dat[,16:18]

#Selecting subset of data
patient_1 <- dat[1,]

#Different ways of manipulating subsets
max(patient_1)
max(dat[2,])
min(dat[,7])
mean(dat[,7])
median(dat[,7])
sd(dat[,7])
summary(dat[,1:4])

#Applying function to a column
avg_patient_inflammation <- apply(dat, 1, mean)
avg_day_inflammation <- apply(dat, 2, mean)

#Playing with slices
animal <- c("m", "o", "n", "k", "e", "y")
animal[1:3]
animal[4:6]

#Learning seq & playing w data
affected_patients <- seq(2, 60, 2)
which_days <- seq(1, 5)
dat2 <- dat
dim(dat2[affected_patients, which_days])
dat2[affected_patients, which_days] <- dat2[affected_patients, which_days]/2
dat2

mean_inflamm_1 <- apply(dat[1:5,],1, mean)
mean_inflamm_2 <- apply(dat[,1:10],2, mean)
mean_inflamm_1 <- apply(dat[,seq(1,40,2)],2, mean)

#Plotting data
plot(avg_day_inflammation)

max_day_inflammation <- apply(dat, 2, max)
plot(max_day_inflammation)

min_day_inflammation <- apply(dat, 2, min)
plot(min_day_inflammation)

sd_day_inflammation <- apply(dat, 2, sd)
plot(sd_day_inflammation)

#Creating Functions
fahrenheit_to_celsius <- function(temp_F) {
  temp_C <- (temp_F - 32) * 5 / 9
  return(temp_C)
}