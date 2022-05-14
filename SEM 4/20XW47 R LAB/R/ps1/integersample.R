# Import lpSolve package
library(lpSolve)

# Set coefficients of the objective function
f.obj <- c(5,4)
 
# Set matrix corresponding to coefficients of constraints by rows
# Do not consider the non-negative constraint; it is automatically assumed
f.con <- matrix(c(1, 1,
                  10, 6), nrow = 2, byrow = TRUE)

# Set unequality signs
f.dir <- c("<=",
           "<=")

# Set right hand side coefficients
f.rhs <- c(5,
           45)

#decimal solution
# Final value (z)
lp("max", f.obj, f.con, f.dir, f.rhs)

# Variables final values
lp("max", f.obj, f.con, f.dir, f.rhs)$solution

#proper integer solution
# Final value (z)
lp("max", f.obj, f.con, f.dir, f.rhs,int.vec=1:2)

# Variables final values
lp("max", f.obj, f.con, f.dir, f.rhs,int.vec=1:2)$solution