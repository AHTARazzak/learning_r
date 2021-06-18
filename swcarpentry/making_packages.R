library("devtools")
library("roxygen2")

# Making Packages in R

# Four main components of R package
# 1) Description with metadata about package
# 2) R directory with code
# 3) Main directory with documentation
# 4) Namespace file listing user-level functions in package

# Place functions into different R scripts

# Description file:
# Package: Package name
# Title: Brief package description
# Description: Longer package description
# Version: Version number(major.minor.patch)
# Author: Name and email of package creator
# Maintainer: Name and email of package maintainer (who to contact with issues)
# License: Abbreviation for an open source license

# Functions don't have to be in one file or each in separate files.

# Template

setwd(parentDirectory)
create_package("tempConvert")

setwd("./tempConvert")
document()