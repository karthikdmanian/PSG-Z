# Import lpSolve package
library(lpSolve)

# Set coefficients of the objective function
f.obj <- c(5000,8500,2400,2800)
 
# Set matrix corresponding to coefficients of constraints by rows
# Do not consider the non-negative constraint; it is automatically assumed
f.con <- matrix(c(800,925,290,380,
                  1,0,0,0,
			0,1,0,0,
			0,0,1,0,
			0,0,0,1,
			0,0,1,1,
			0,0,290,380), nrow = 7, byrow = TRUE)

# Set unequality signs
f.dir <- c("<=",
           "<=",
		"<=",
		"<=",
		"<=",
		">=",
		"<=")

# Set right hand side coefficients
f.rhs <- c(8000,
           12,
		5,
		25,
		20,
		5,
		1800)

# Final value (z) (decimal)
lp("max", f.obj, f.con, f.dir, f.rhs)

# Variables final values
lp("max", f.obj, f.con, f.dir, f.rhs)$solution

# Final value (z) (integer)
lp("max", f.obj, f.con, f.dir, f.rhs,int.vec=1:4)

# Variables final values
lp("max", f.obj, f.con, f.dir, f.rhs,int.vec=1:4)$solution