main <- function() {
  args <- commandArgs(trailingOnly = TRUE)
  arg_1 <- as.numeric(args[1])
  operation <- args[2]
  args_3 <- as.numeric(args[3])
  if (operation == "+") {
    answer <- arg_1 + args_3
    cat(answer)
  } else if (operation == "-") {
    answer <- arg_1 - args_3
    cat(answer)
  } else {
    stop("Invalid input. Use + for addition or - for subtraction.")
  }
}

main()