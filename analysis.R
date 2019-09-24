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

hpm <- h[pm]

hpm[hpm<12] <- hpm[hpm<12] + 12 

h[pm] <- hpm

depart_min <- 60*h+m

flights <- mutate(flights, depart_min=depart_min)

#f <- factor(-flights$`days before depart`)
#ggplot(flights, aes(f, flights$price, fill = factor(stops))) + geom_boxplot() + facet_grid(~stops)

flights <- mutate(flights, durations2 = durations)



df <- filter(flights, flights$`days before depart` == 24)
boxplot(df$price ~ df$durations2)


df <- filter(flights, flights$`days before depart` == 21)
ggplot(df, aes(durations2/60, price)) +
        geom_point(aes(color = factor(stops)), size = 3) + geom_smooth() + theme_classic() +xlab("flight duration (Hours)")

df <- filter(flights, flights$`days before depart` == 24)
ggplot(df, aes(depart_min/60, price)) +
  geom_point(aes(color = factor(stops)), size = 3) + geom_smooth() + theme_classic() + xlab("departure time (hours)")



df <- filter(flights, flights$`days before depart` == 24)
ggplot(df, aes(depart_min/60, price, color = factor(stops))) +
  geom_point(aes(color = factor(stops)), size = 3) + geom_smooth(method = "lm", se = FALSE) + theme_classic() 
  



# rest of entire will be the whole dataset graphs 


hist(depart_min / 60)

r <- round(depart_min/60)

r <- factor(r, levels = 0:24)


barplot(table(r))
abline(h=0)

id <- paste(flights$depart, flights$arrive, sep = "-")

flights <- mutate(flights, id = id)

ggplot(flights, aes(-flights$`days before depart`, flights$price, col = id)) + 
  geom_line() + theme(legend.position = "none")


sel <- filter(flights, flights$stops == 1)
ggplot(sel, aes(-sel$`days before depart`, sel$price, col = id)) + 
  geom_line() + theme(legend.position = "none")


f <- factor(-flights$`days before depart`)



#ggplot(flights, aes(f, flights$price, fill = factor(stops))) + 
#  geom_boxplot() + facet_wrap(~stops + dayofweek, nrow = 8, ncol=7)
ggplot(flights, aes(dayofweek, price, fill = factor(dayofweek))) + 
  geom_boxplot() + facet_wrap(~stops, ncol = 3)


name=c(flights$price)
feature=paste("feature ", c(flights$dayofweek) , sep="")
dat <- data.frame(name,feature)
dat <- with(dat, table(name, feature))

# Charge the circlize library
library(circlize)

# Make the circular plot
chordDiagram(as.data.frame(dat), transparency = 0.5)


s <- split(flights, id)

getBestDay <- function(x) {
  w <- which.min(x$price)
  paste(-x$`days before depart`[w], x$dayofweek[w], sep = ":")
}

bestdays <- sapply(s, getBestDay)
barplot((table(bestdays)), axis.lty = 1, xlab = "days before flight", 
        ylab = "frequency", main = "Best day to buy a plane ticket from NYC to SHA")

