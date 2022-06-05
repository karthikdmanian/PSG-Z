path<-"D:/PSG/PSG-Z/SEM 4/20XW47 R LAB/R/r-package/customer-segmentation-dataset/Mall_Customers.csv"
customer_data=read.csv(path)

#The str() command is designed to help you examine the structure of a data object rather than providing a statistical summary. The summary() command will provide you with a statistical summary of your data. The output of summary command depends on the object you are looking at.

str(customer_data)
names(customer_data)

#The head() function in R is used to display the first n rows present in the input data frame.
head(customer_data)
summary(customer_data$Age)

#std. dev
sd(customer_data$Age)
summary(customer_data$Annual.Income..k..)
sd(customer_data$Annual.Income..k..)

#gender visualization
#bar-plot
a=table(customer_data$Gender)
a
barplot(a,main="Using BarPlot to display Gender Comparision",
       ylab="Count",
       xlab="Gender",
       col=rainbow(2),
       legend=rownames(a))

#gender visualization
#pie-chart (plotrix)
pct=round(a/sum(a)*100)
lbs=paste(c("Female","Male")," ",pct,"%",sep=" ")
library(plotrix)
pie3D(a,labels=lbs,
   main="Pie Chart Depicting Ratio of Female and Male")

#age-visualization
#histogram
hist(customer_data$Age,
    col="yellow",
    main="Histogram to Show Count of Age Class",
    xlab="Age Class",
    ylab="Frequency",
    labels=TRUE)

#annual-income-visualization
#histogram
hist(customer_data$Annual.Income,
  col="brown",
  main="Histogram for Annual Income",
  xlab="Annual Income Class",
  ylab="Frequency",
  labels=TRUE)

#spending-score-visualization
#histogram
hist(customer_data$Spending.Score..1.100.,
    main="HistoGram for Spending Score",
    xlab="Spending Score Class",
    ylab="Frequency",
    col="purple",
    labels=TRUE)




