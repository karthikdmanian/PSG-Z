library(lpSolve)
a <- matrix(c(17,25,31,10,25,16,12,14,11), nrow = 3, byrow = TRUE)
cost.mat <- a
cost.mat
# Run

lpassign <- lp.assign (cost.mat)
lpassign$solution
lpassign$objval