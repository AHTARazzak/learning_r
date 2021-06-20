# Reading & Writing CSV Files

carSpeeds <- read.csv(file = "car-speeds.csv")
head(carSpeeds)

carSpeeds[1, ]

carSpeeds <- read.csv(file = "car-speeds.csv", header = FALSE)

carSpeeds[1, ]

carSpeeds <- read.csv(file = "car-speeds.csv", stringsAsFactors = TRUE)
carSpeeds$Color <- ifelse(carSpeeds$Color == "Blue", "Green", carSpeeds$Color)
carSpeeds$Color

str(carSpeeds)

carSpeeds <- read.csv(file = 'car-speeds.csv', stringsAsFactors = FALSE)
str(carSpeeds)

carSpeeds$Color <- ifelse(carSpeeds$Color == 'Blue', 'Green', carSpeeds$Color)
carSpeeds$Color

carSpeeds <- read.csv(file = 'car-speeds.csv', as.is = 1)
str(carSpeeds)

carSpeeds$Color <- ifelse(carSpeeds$Color == 'Blue', 'Green', carSpeeds$Color)
carSpeeds$Color

carSpeeds$State <- ifelse(carSpeeds$State == 'Arizona', 'Ohio', carSpeeds$State)
carSpeeds$State

carSpeeds <- read.csv(file = "car-speeds.csv", as.is = 1)
carSpeeds$Color <- ifelse(carSpeeds$Color == 'Blue', 'Green', carSpeeds$Color)
carSpeeds$Color

unique(carSpeeds$Color)

carSpeeds <- read.csv(
  file = 'car-speeds.csv',
  stringsAsFactors = FALSE, 
  strip.white = TRUE,
  sep = ','
)

unique(carSpeeds$Color)

write.csv(carSpeeds, file = 'car-speeds-cleaned.csv')
write.csv(carSpeeds, file = 'car-speeds-cleaned.csv', row.names = FALSE)

carSpeeds$Speed[3] <- 3
head(carSpeeds)

write.csv(carSpeeds, file = 'car-speeds-cleaned.csv', row.names = FALSE)
write.csv(carSpeeds, file = 'car-speeds-cleaned.csv', row.names = FALSE, na = '-9999')

#Import data from .csv file usibg read.csv() function
# Understand some key arguments available for importing data properly, including header, stringAsFactors, as.is, strip.white
# Write data to new.csv file using write.csv() function
# Understand ket argumetns available for exporting data properly such as row.names, col.names, & NA

