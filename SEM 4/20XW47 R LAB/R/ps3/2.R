#
# Load "lpSolve" package
library(lpSolve)

# Set up cost matrix
costs <- matrix(c(464,352,995,513,416,682,654,690,388,867,791,685), nrow = 3)

# Set up constraint signs and right-hand sides
row.signs <- rep("<=", 3)
row.rhs <- c(75,125,100)
col.signs <- rep(">=", 4)
col.rhs <- c(80,65,70,85)

# Run
lptrans <- lp.transport(costs, "min", row.signs, row.rhs, col.signs, col.rhs)
lptrans$solution
lptrans$objval