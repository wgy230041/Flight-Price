
# Rely on the 'WorldPhones' dataset in the datasets
# package (which generally comes preloaded).
library(shiny)
library(datasets)
library(readxl)

function(input, output, session) {
  
  
  cat("reading in flights informatuion...\n")
  

  flights <- read_excel("D:/ECSU CSC-360  Advanced Web Development and Web Scraping/Assingment/final projects/flightprices.csv")

  flights <- flights[!is.na(flights$`recorded date`),]
  
  # // intead of blank space
  # Define a server for the Shiny app
  
  cat("got data!\n")
  dayofw <- sort(unique(flights$dayofweek))
  
  
  updateSelectizeInput(session, inputId= "dayofweek", choices = dayofw, server = TRUE)
  
  
  
  # Fill in the spot we created for  plot
  output$flightsplot <- renderPlot({
    
    # create data frame with results for desired data
    #df <- flights[flights$dayofweek == input$dayofweek & flights$`recorded date` == input$dateRange | flights$`days before depart` == input$dayofweek, ]
   
    df <- flights[flights$dayofweek == input$dayofweek & flights$`days before depart` ==input$Daysbefore, ]
    
    cat("number of rows = ", nrow(df), "\n")
    
    cat("first matching day of week:\n")
    print(head(df))
    
    # generate a bar graph of frequency of that duratio with prices
    main <- paste("The prices summary based on the search day of week --", input$dayofweek, " and how many stops.")
    #barplot(df$price, col = "lightblue", 
    #       xlab = "sumer", ylab = "price", 
    #        main = main)
    
    if (nrow(df) == 0) {
      return()
    }
    
    boxplot(df$price ~ df$stops, col = "lightblue", 
            xlab = "stops", ylab = "price", 
            main = main)
    
    
  })
  
  

  
}