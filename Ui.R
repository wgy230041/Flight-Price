# Rely on the 'WorldPhones' dataset in the datasets
# package (which generally comes preloaded).
library(datasets)
library(readxl)
# Use a fluid Bootstrap layout
fluidPage(    
  
  # Give the page a title
  titlePanel("The flight price based on the search the duration and stops"),
  
  # Generate a row with a sidebar
  sidebarLayout(      
    
    # Define the sidebar with one input
    sidebarPanel(
      selectInput("dayofweek","the search day of week", choices=NULL),
      #The choices argument is NULL because we are not going to set the choices value here; 
      #we will do this on the server-side.
      hr(),
      helpText("Data from yang's github.wgy230041"),
      
      
      sliderInput("Daysbefore", 
                  label = "Range of the days before depart day check in:",
                  min = 21, max = 28, value = 21)
      
      #dateRangeInput('dateRange',
      #               label = 'Date range input: yyyy-mm-dd',
      #               start = Sys.Date() - 8, end = Sys.Date() - 1
      #)
    ),
    
    
    # Create a spot for the barplot
    mainPanel(
      plotOutput("flightsplot")
    
    )
  )
)

