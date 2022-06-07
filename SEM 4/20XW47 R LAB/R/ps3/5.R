library(lpSolve)
a <- matrix(c(10,14,16,13,12,13,15,12,9,12,12,11,14,16,18,16), nrow = 4, byrow = TRUE)
cost.mat <- a
cost.mat
# Run

lpassign <- lp.assign (cost.mat)
lpassign$solution
lpassign$objval