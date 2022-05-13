# Import lpSolve package
library(lpSolve)

# Set coefficients of the objective function
# 3x1+8x2+2x3 - (x4)
f.obj <- c(3,8,2,-1)
 
# Set matrix corresponding to coefficients of constraints by rows
# Do not consider the non-negative constraint; it is automatically assumed
f.con <- matrix(c(0, 0, 1,  0,
                  0, 3, -1, -1, 
			3, 4, 0 , 0, 
			3, 5, 0 , 0), nrow = 4, byrow = TRUE)

# Set unequality signs
f.dir <- c("<=",
           "=",
	     "<=",
	     "<=")

# Set right hand side coefficients
f.rhs <- c(5,
           0,
		18,
		21)

# Final value (z)
lp("max", f.obj, f.con, f.dir, f.rhs)

# Variables final values
lp("max", f.obj, f.con, f.dir, f.rhs)$solution