# Import lpSolve package
library(lpSolve)

# Set coefficients of the objective function
f.obj <- c(24, 18, 24)
 
# Set matrix corresponding to coefficients of constraints by rows
# Do not consider the non-negative constraint; it is automatically assumed
f.con <- matrix(c(5, 1, 3
                  2, 6, 3
                  ), nrow = 2, byrow = TRUE)

# Set unequality signs
f.dir <- c("<=",
           "<=",)

# Set right hand side coefficients
f.rhs <- c(600,
           500)

# Final value (z)
lp("max", f.obj, f.con, f.dir, f.rhs)

# Variables final values
lp("max", f.obj, f.con, f.dir, f.rhs)$solution

# Sensitivities
lp("max", f.obj, f.con, f.dir, f.rhs, compute.sens=TRUE)$sens.coef.from
lp("max", f.obj, f.con, f.dir, f.rhs, compute.sens=TRUE)$sens.coef.to
