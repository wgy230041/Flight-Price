library(readxl)
library(dplyr)
library(ggplot2)

flights <- read_excel("D:/ECSU CSC-360  Advanced Web Development and Web Scraping/Assingment/final projects/flightprices.csv")

flights <- flights[!is.na(flights$`recorded date`),]

keep <- grepl(".M", flights$depart)

flights <- flights[keep,]

times <- strsplit(flights$duration, "h")

getHours <- function(x) {
  as.integer(x[1])
}

hours <- sapply(times,getHours)

getMinutes <- function(x) {
  x <- strsplit(x[2], "m")
  as.integer(x[[1]])
}

mins <- sapply(times, getMinutes)

durations <- 60*hours + mins


pm <- grepl("PM", flights$depart)
flights <- mutate(flights, depart_pm = pm)

depart <- flights$depart
depart <- gsub(".M", "", depart)

d <- strsplit(depart, ":")

h <- sapply(d, function(x) as.double(x[1]))
m <- sapply(d, function(x) as.double(x[2]))

h[pm] <- h[pm] + 12

depart_min <- 60*h+m

flights <- mutate(flights, depart_min=depart_min)

#f <- factor(-flights$`days before depart`)
#ggplot(flights, aes(f, flights$price, fill = factor(daysofweek))) + 
#  geom_boxplot() + facet_grid(~daysofweek)

flights <- mutate(flights, durations2 = durations)



df <- filter(flights, flights$`days before depart` == 21)
boxplot(df$price ~ df$durations2)


ggplot(df, aes(durations2, price)) +
        geom_point(aes(color = factor(stops))) + geom_smooth()


ggplot(df, aes(depart_min, price)) +
  geom_point(aes(color = factor(stops))) + geom_smooth()


hist(depart_min)


id <- paste(flights$depart, flights$arrive, sep = "-")

flights <- mutate(flights, id = id)

ggplot(flights, aes(-flights$`days before depart`, flights$price, col = id)) + 
  geom_line() + theme(legend.position = "none")

f <- factor(-flights$`days before depart`)

ggplot(flights, aes(f, flights$price, fill = factor(stops))) + 
  geom_boxplot() + facet_wrap(~stops + dayofweek, nrow = 4, ncol=7)

s <- split(flights, id)

getBestDay <- function(x) {
  w <- which.min(x$price)
  paste(-x$`days before depart`[w], x$dayofweek[w], sep = ":")
}

bestdays <- sapply(s, getBestDay)
barplot((table(bestdays)), axis.lty = 1, xlab = "days before flight", 
        ylab = "frequency", main = "Best day to buy a plane ticket from NYC to SHA")

