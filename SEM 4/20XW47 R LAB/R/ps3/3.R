#
# Load "lpSolve" package
library(lpSolve)

# Set up cost matrix
costs <- matrix(c(5,7,6,2,3,5), nrow = 2,byrow=TRUE)

# Set up constraint signs and right-hand sides
row.signs <- rep("<=", 2)
row.rhs <- c(60,40)
col.signs <- rep(">=", 3)
col.rhs <- c(50,30,20)

# Run
lptrans <- lp.transport(costs, "max", row.signs, row.rhs, col.signs, col.rhs)
lptrans$solution
lptrans$objval