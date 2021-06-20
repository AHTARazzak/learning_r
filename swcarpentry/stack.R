# The Call Stack

original <- 32
span <- function(a) {
  diff <- max(a) - min(a)
  return(diff)
}

dat <- read.csv(file = "inflammation-01.csv", header=FALSE)
span(dat)

inner_vec <- "carbon"
outer_vec <- "+"
result <- edges(highlight(inner_vec, outer_vec))

#R keeps track of active function calls using a call stack comprised of stack frames
# Only global variables & variables in current stackf rame can be accessed directly