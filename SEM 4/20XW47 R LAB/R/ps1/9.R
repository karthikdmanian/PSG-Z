# Import lpSolve package
library(lpSolve)

# Set coefficients of the objective function
f.obj <- c(7/100,11/100,19/100,15/100)
 
# Set matrix corresponding to coefficients of constraints by rows
# Do not consider the non-negative constraint; it is automatically assumed
f.con <- matrix(c(1, 1, 1, 1,
			1, 0, 0, 0,
			0, 1, 0, 0,
			0, 0, 1, 0,
			0, 0, 0, 1,
			-55/100,-55/100,45/100,45/100,
                  85/100, -15/100,-15/100,-15/100), nrow = 7, byrow = TRUE)

# Set unequality signs
f.dir <- c("<=",
		"<=",
           "<=",
		"<=",
		"<=",
		">=",
		">=")

# Set right hand side coefficients
f.rhs <- c(5000000,
		1000000,
           2500000,
		1500000,
		1800000,
		0,
		0)

# Final value (z)
lp("max", f.obj, f.con, f.dir, f.rhs)

# Variables final values
lp("max", f.obj, f.con, f.dir, f.rhs)$solution