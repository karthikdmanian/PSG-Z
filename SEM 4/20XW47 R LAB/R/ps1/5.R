# Import lpSolve package
library(lpSolve)

# Set coefficients of the objective function
f.obj <- c(68.8, 68)
 
# Set matrix corresponding to coefficients of constraints by rows
# Do not consider the non-negative constraint; it is automatically assumed
f.con <- matrix(c(320, 240,
                  1, 0,
                  0, 1), nrow = 3, byrow = TRUE)

# Set unequality signs
f.dir <- c(">=",
           "<=",
           "<=")

# Set right hand side coefficients
f.rhs <- c(2000,
           9,
           11)

# Final value (z)
lp("min", f.obj, f.con, f.dir, f.rhs)

# Variables final values
lp("min", f.obj, f.con, f.dir, f.rhs)$solution