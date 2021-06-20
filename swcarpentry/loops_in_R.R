# Loops in R

analyze <- function(filename) {
  # Plots the average, min, and max inflammation over time.
  # Input is character string of a csv file.
  dat <- read.csv(file = filename, header = FALSE)
  avg_day_inflammation <- apply(dat, 2, mean)
  plot(avg_day_inflammation)
  max_day_inflammation <- apply(dat, 2, max)
  plot(max_day_inflammation)
  min_day_inflammation <- apply(dat, 2, min)
  plot(min_day_inflammation)
}

filesnames <- list.files(path = "data", pattern = "inflammation-[0-9]{2}.csv", full.names=TRUE)
a <- 1:10
b <- 1:10

res <- numeric(length = length(a))
for (i in seq_along(a)) {
  res[i] <- a[i] + b[i]
}

res

res2 <- a + b
all.equal(res, res2)

a <- 1:10
b <- 1:5
a + b

a <-  1:10
b <- 1:7
a + b

# apply: apply over margins of an array
# lapply: apply over an object & return list
# sapply: aapply over object & return simplified object if possible
# vapply: similar to sapply but specify type of object returned by iterations

sapply(filenames, FUN = analyze)

analyze2 <- function(filenames) {
  for (f in seq_along(filenames)) {
    fdata <- read.csv(filenames[f], header = FALSE)
    res <- apply(fdata, 2, mean)
    if (f == 1) {
      out <- res
    } else {
      # The loop is slowed by this call to cbind that grows the object
      out <- cbind(out, res)
    }
  }
  return(out)
}

filenames <- list.files(  
                        # Now follows a regular expression that matches:
                        pattern = "inflammation-[0-9]{2}.csv",
                        #          |            |        the standard file extension of comma-separated values
                        #          |            the variable parts (two digits, each between 0 and 9)
                        #          the static part of the filenames
                        full.names = TRUE)

system.time(avg2 <- analyze2(filenames))

analyze3 <- function(filenames) {
  out <- matrix(ncol = length(filenames), nrow = 40) # assuming 40 here from files
  for (f in seq_along(filenames)) {
    fdata <- read.csv(filenames[f], header = FALSE)
    out[, f] <- apply(fdata, 2, mean)
  }
  return(out)
}

system.time(avg3 <- analyze3(filenames))

# Use vectorised operations instead of forloops to make code faster & more concise
# Use functions such as apply instead of for to operate on values in data structure