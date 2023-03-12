# Set working directory
setwd("C:/Users/rubi_/OneDrive/Desktop/Ricardo/MIS581-1/MAUDE_Data/MAUDE_Final")

#Install the Graphing package ggplots and tidyverse
install.packages("ggplot2")
install.packages("tidyverse")
#load the graphing library gglot2 and tidyverse
library(ggplot2)
library(tidyverse)

#direct r which excel file to read
MAUDEttest <-read.csv("MAUDE_ttest.csv", header = TRUE, sep =",")


#To view data graph a box plot
ggplot(Maudettest,aes(x = Group, y = NumberofEvents)) + geom_boxplot()

#To conduct a t-test write the code
t.test(NumberofEvents ~ Group, data = MAUDEttest, Var.equal = TRUE, Paired = False)

