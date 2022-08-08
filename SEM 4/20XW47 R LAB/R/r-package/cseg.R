path<-"D:/PSG/PSG-Z/SEM 4/20XW47 R LAB/R/r-package/customer-segmentation-dataset/Mall_Customers.csv"
customer_data=read.csv(path)

#The str() command is designed to help you examine the structure of a data object rather than providing a statistical summary. The summary() command will provide you with a statistical summary of your data. The output of summary command depends on the object you are looking at.

str(customer_data)
names(customer_data)

#The head() function in R is used to display the first n rows present in the input data frame.
head(customer_data)
#summary(customer_data$Age)

#std. dev
sd(customer_data$Age)
#summary(customer_data$Annual.Income..k..)
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
pct
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

#K-means Elbow method

library(purrr)
set.seed(123)
# function to calculate total intra-cluster sum of square 
iss <- function(k) {
  kmeans(customer_data[,3:5],k,iter.max=100,nstart=100,algorithm="Lloyd" )$tot.withinss
}

k.values <- 1:10


iss_values <- map_dbl(k.values, iss)

plot(k.values, iss_values,
    type="b", pch = 19, frame = FALSE, 
    xlab="Number of clusters K",
    ylab="Total intra-clusters sum of squares")

#Average Silhouette Method

#2 clusters
library(cluster) 
library(gridExtra)
library(grid)
k2<-kmeans(customer_data[,3:5],2,iter.max=100,nstart=50,algorithm="Lloyd")
s2<-plot(silhouette(k2$cluster,dist(customer_data[,3:5],"euclidean")))

#3 clusters
k3<-kmeans(customer_data[,3:5],3,iter.max=100,nstart=50,algorithm="Lloyd")
s3<-plot(silhouette(k3$cluster,dist(customer_data[,3:5],"euclidean")))

#4 clusters
k4<-kmeans(customer_data[,3:5],4,iter.max=100,nstart=50,algorithm="Lloyd")
s4<-plot(silhouette(k4$cluster,dist(customer_data[,3:5],"euclidean")))

#5 clusters
k5<-kmeans(customer_data[,3:5],5,iter.max=100,nstart=50,algorithm="Lloyd")
s5<-plot(silhouette(k5$cluster,dist(customer_data[,3:5],"euclidean")))

#6 clusters
k6<-kmeans(customer_data[,3:5],6,iter.max=100,nstart=50,algorithm="Lloyd")
s6<-plot(silhouette(k6$cluster,dist(customer_data[,3:5],"euclidean")))

#7 clusters
k7<-kmeans(customer_data[,3:5],7,iter.max=100,nstart=50,algorithm="Lloyd")
s7<-plot(silhouette(k7$cluster,dist(customer_data[,3:5],"euclidean")))

#fviz_nbclust() function to determine and visualize the optimal number of clusters
library(NbClust)
library(factoextra)

fviz_nbclust(customer_data[,3:5], kmeans, method = "silhouette")

#Visualizing the Clustering Results using the First Two Principle Components
pcclust=prcomp(customer_data[,3:5],scale=FALSE) #principal component analysis
summary(pcclust)

pcclust$rotation[,1:2]


#Cluster visualization - spending score - annual income
set.seed(1)
ggplot(customer_data, aes(x =Annual.Income..k.., y = Spending.Score..1.100.)) + 
  geom_point(stat = "identity", aes(color = as.factor(k6$cluster))) +
  scale_color_discrete(name=" ",
              breaks=c("1", "2", "3", "4", "5","6"),
              labels=c("Cluster 1", "Cluster 2", "Cluster 3", "Cluster 4", "Cluster 5","Cluster 6")) +
  ggtitle("Segments of Mall Customers", subtitle = "Using K-means Clustering")


#classless - kmeans visualization

#We developed this using a class of machine learning known as unsupervised learning. 
#Specifically, we made use of a clustering algorithm called K-means clustering. 
#We analyzed and visualized the data and then proceeded to implement our algorithm


