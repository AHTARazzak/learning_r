
#setwd("/Users/alirazzak/Desktop/Code/rstudio_learn")
#getwd()
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

#Analyzing multiple Data Sets
analyze("inflammation-01.csv")

best_practice <- c("Let", "the", "computer", "do", "the", "work")
print_words <- function(sentence) {
  print(sentence[1])
  print(sentence[2])
  print(sentence[3])
  print(sentence[4])
  print(sentence[5])
  print(sentence[6])
}
print_words(best_practice)
best_practice[-6]
print_words(best_practice[-6])

print_words <- function(sentence) {
  for (word in sentence) {
    print(word)
  }
}

print_words(best_practice)

len <- 0
vowels <- c("a", "e", "i", "o", "u")
for (v in vowels) {
  len <- len +1
}
len

letter <- "z"
for (letter in c("a", "b", "c")) {
  print(letter)
}

length(vowels)

for (i in  seq(3)){
  print(i)
}

total <- function(this_vector){
  the_sum <- 0
  for (i in this_vector){
    the_sum <- the_sum + i
  }
  return(the_sum)
}
ex_vec <- c(4, 8, 15, 16, 23, 42)
total(ex_vec)

expo <- function(base, exponent){
  this_base <- 1
  for (i in seq(exponent)){
    this_base <- this_base * base
  }
  return(this_base)
}
expo(2, 4)

filenames <- list.files(pattern = "csv", full.names=TRUE)

filenames <- filenames[1:3]
for (f in filenames) {
  print(f)
  analyze(f)
}

#Making Choices
analyze_all <- function(folder = "data", pattern) {
  filenames <- list.files(path = folder, pattern = pattern, full.names = TRUE)
  for (f in filenames) {
    analyze(f)
  }
}

pdf("inflammation-01.pdf")
analyze("inflammation-01.csv")
dev.off()

num  <- 37
num > 100
num < 100
num <- 37
if (num > 100) {
  print("greater")
} else {
  print("not greater")
}
print("done")

num <- 53
if (num > 100) {
  print("num is greater than 100")
}

sign <- function(num) {
  if (num > 0) {
    return(1)
  } else if (num == 0){
    return(0)
  } else {
    return(-1)
  }
}

sign(-3)
sign(2/3)
if (1 > 0 && -1 > 0){
  print("both parts are true")
} else {
  print("at least one part is not true")
}

if (1 > 0 || -1 > 0) {
  print("at least one part is true")
} else {
  print("neither part is true")
}

a <- NA
a == 1

if (is.na(a)){
  print("Hi!")
}
help(boxplot)
plot_dist <- function(x, threshold, use_boxplot = TRUE) {
  if (length(x) > threshold && use_boxplot) {
    boxplot(x)
  } else if (length(x) < threshold && !use_boxplot) {
    hist(x)
  } else {
    stripchart(x)
  }
}

dat <- read.csv("inflammation-01.csv", header = FALSE)
plot_dist(dat[, 10], threshold = 10) 

filenames <- list.files(path = "data", pattern = "inflammation-[0-4]{2}.csv", full.names = TRUE)
filename_max <- ""
patient_max <- 0
average_inf_max <- 0
for (f in filenames) {
  dat <- read.csv(file = f, header = FALSE)
  dat.means <- apply(dat, 1, mean)
  for (patient_index in 1:length(dat.means)){
    patient_average_inf <- dat.means[patient_index]
    if (patient_average_inf  > average_inf_max) {
      average_inf_max <- patient_average_inf
      filename_max <- f
      patient_max <- patient_index
    }
  }
}
print(filename_max)
print(patient_max)
print(average_inf_max)

analyze <- function(filename, output = NULL) {
  if (!is.null(output)) {
    pdf(output)
  }
  dat <- read.csv(file = filename, header = FALSE)
  avg_day_inflammation <- apply(dat, 2, mean)
  plot(avg_day_inflammation)
  max_day_inflammation <- apply(dat, 2, max)
  plot(max_day_inflammation)
  min_day_inflammation <- apply(dat, 2, min)
  plot(min_day_inflammation)
  if (!is.null(output)) {
    dev.off()
  }
}

output <- NULL
is.null(output)
!is.null(output)
analyze("inflammation-01.csv")
dir.create("results")
analyze("inflammation-01.csv", output = "results/inflammation-01.pdf")

f <- "inflammation-01.csv"
sub("csv", "pdf", f)

analyze_all <- function(pattern) {
  data_dir <- "data"
  results_dir <- "results"
  filenames <- list.files(path = data_dir, pattern = pattern)
  for (f in filenames) {
    pdf_name <- file.path(results_dir, sub("csv", "pdf", f))
    analyze(file.path(data_dir, f), output = pdf_name)
  }
}

analyze <- function(filename, output = NULL) {
  if (!is.null(output)) {
    pdf(output)
  }
  dat <- read.csv(file = filename, header = FALSE)
  avg_day_inflammation <- apply(dat, 2, mean)
  plot(avg_day_inflammation, type = "l")
  max_day_inflammation <- apply(dat, 2, max)
  plot(max_day_inflammation, type = "l")
  min_day_inflammation <- apply(dat, 2, min)
  plot(min_day_inflammation, type = "l")
  if (!is.null(output)) {
    dev.off()
  }
}
