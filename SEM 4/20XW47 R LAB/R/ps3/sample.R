# Transportation problem, Frederick & Mark (2014, p.95)
#
# Load "lpSolve" package
library(lpSolve)

# Set up cost matrix
costs <- matrix(c(700, 800, 900, 900, 800, 700), nrow = 2)

# Set up constraint signs and right-hand sides
row.signs <- rep("<=", 2)
row.rhs <- c(12, 15)
col.signs <- rep(">=", 3)
col.rhs <- c(10, 8, 9)

# Run
lptrans <- lp.transport(costs, "min", row.signs, row.rhs, col.signs, col.rhs)
lptrans$solution
lptrans$objval