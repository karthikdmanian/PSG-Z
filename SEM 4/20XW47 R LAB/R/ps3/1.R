#
# Load "lpSolve" package
library(lpSolve)

# Set up cost matrix
costs <- matrix(c(2,2,2,1,10,8,5,4,7,6,6,8), nrow = 3, byrow=TRUE)

# Set up constraint signs and right-hand sides
row.signs <- rep("<=", 3)
row.rhs <- c(3,7,5)
col.signs <- rep(">=", 4)
col.rhs <- c(4,3,4,4)

# Run
lptrans <- lp.transport(costs, "min", row.signs, row.rhs, col.signs, col.rhs)
lptrans$solution
lptrans$objval

# 2,10,7,2,8,6,2,5,6,1,4,8