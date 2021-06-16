
setwd("/Users/alirazzak/Desktop/Code/rstudio_learn")
getwd()
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

#Investigating a dataframe
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

fahrenheit_to_celsius(32)
fahrenheit_to_celsius(212)

celsius_to_kelvin <- function(temp_C) {
  temp_K <- temp_C + 273.15
  return(temp_K)
}

celsius_to_kelvin(0)

fahrenheit_to_kelvin <- function (temp_F) {
  temp_C <- fahrenheit_to_celsius(temp_F)
  temp_K <- celsius_to_kelvin(temp_C)
  return(temp_K)
}

celsius_to_kelvin(fahrenheit_to_celsius(32.0))

highlight <- function(content, wrapper) {
  answer <- c(wrapper, content, wrapper)
  return(answer)
  }

highlight("fun","cool")

edges <- function(the_vector){
  answer <-c(the_vector[1], the_vector[length(the_vector)])
  return(answer)
}

dry_principle <- c("Don't", "repeat", "yourself", "or", "others")
edges(dry_principle)

input_1 <- 20
mySum <- function(input_1, input_2 = 10) {
  output <- input_1 + input_2
  return(output)
}

center <- function(data, midpoint) {
  new_data <- (data-mean(data)) + midpoint
  return(new_data)
}

z <- c(0, 0, 0, 0)
center(z,3)

centered <- center(dat[,4], 0)
head(centered)

mean(dat[,4])
mean(centered)
sd(dat[,4])
sd(centered)
sd(dat[,4]) - sd(centered)
all.equal(sd(dat[,4]), sd(centered))
datNA <- dat
datNA[10, 4] <- NA
center(datNA[,4], 0)

center <- function(data,midpoint) {
  new_data <- (data - mean(data, na.rm = TRUE)) + midpoint
  return(new_data)
}

center(datNA[,4], 0)

datNA[,1] <- as.factor(datNA[,1])
datNA[,2] <- as.character(datNA[,2])
center(datNA[,1],0)
center(datNA[,2], 0)

center <- function(data, midpoint) {
  new_data <- (data - mean(data)) + midpoint
  return(new_data)
}

analyze <- function(filename) {
  this_file <- read.csv(file = filename, header=FALSE)
  max_day_inflammation <- apply(this_file, 2, max)
  plot(max_day_inflammation)
  
  min_day_inflammation <- apply(this_file, 2, min)
  plot(min_day_inflammation)
  
  sd_day_inflammation <- apply(this_file, 2, sd)
  plot(sd_day_inflammation)
}

analyze("inflammation-01.csv")
analyze("inflammation-02.csv")

rescale <- function(this_vector) {
  lowest <- min(this_vector)
  highest <- max(this_vector)
  result <- (this_vector - lowest) / (highest - this_vector)
  return(result)
}

center <- function(data, midpoint = 0) {
  new_data <- (data - mean(data)) + midpoint
  return(new_data)
}

test_data <- c(0, 0, 0, 0)
center(test_data, 3)

more_data <- 5 + test_data
more_data

center(more_data)

display <- function(a=1, b=2, c=3){
  result <- c(a, b, c)
  names(result) <- c("a", "b", "c")
  return(result)
}

display(55)
display(55,66)
display(55,66,77)
display(c = 77)

rescale <- function(this_vector, lowest = min(this_vector), highest = max(this_vector)) {
  result <- (this_vector - lowest) / (highest - this_vector)
  return(result)
}
