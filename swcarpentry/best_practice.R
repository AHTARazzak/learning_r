library(ggplot2)
library(reshape)
library(vegan)

input_file <- "name_of_data.csv"
output_file <- "output_of_data.csv"

# read input
input_data <- read.csv(input_file)

# get number of samples in data
sample_number <- nrow (input_data)

# generate results
results <- some_other_function(input_file, sample_number)

# write results
write.table(results, output_file)

# Be careful when used set wd for script, ideally have all scripts in consistent directory & path from it
# It effects reproducibility

# Can call different functions from other R files using "source"
source("my_genius_fxns.R")

# Sample dataset of 1000 rows
interim_object <- data.frame(rep(1:100, 10),
                             rep(101:200, 10),
                             rep(201:300, 10))
object.size(interim_object) # Reports the memory size allocated to the object
rm("interim_object") # Removes only the object itself and not necessarily the memory allotted to it
gc() # Force R to release memory it is no longer using
ls() # Lists all the objects in your current workspace

# Rule breakdown
# 1) Consistent style within code (naming convenrtions, format, etc)
# 2) Keep code in bite-sized chunks, break loops into smaller pieces
# 3) Dont Repeat Yourself (automate)
# 4) Try keep source files in same project directory & navigate to files from it
# 5) Keep memory usage in mind
# 6) Don't save a sessions history
# 7) Keep track of sessionInfo in project folder
# 8) Practice code review- used for preparing experiments & manuscripts.
rm(list = ls()) # If you want to delete all the objects in the workspace and start with a clean slate

# Start each program w description of what it does
# Then load packages
# Consider working directory when writing script
# Use comments to mark off sections of code
# Put functions definitions at top of file, or in seperate file if many
# Name & style code consistently
# Break code into small, discrete pieces
# Factor out common operations rather tjan repeating them
# Keep all of source files for project in one & use relative paths to access them
# Keep track fo the memory used by your program
# Always start w clean environment instead of saving workspace
# Keep track of session information in your project folder
# Someone else review your code
# Use version control