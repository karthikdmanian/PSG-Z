# Import lpSolve package
library(lpSolve)

# Set coefficients of the objective function
#the one who enters in the first week will be there for all 5 weeks
f.obj <- c(5,4,3,2,1)
 
# Set matrix corresponding to coefficients of constraints by rows
# Do not consider the non-negative constraint; it is automatically assumed
f.con <- matrix(	1, 1, 1, 1, 1,
			-1/3, 0, 0 ,0, 0,
			-1/3, -1/3 , 0, 0, 0,
			1, -1/3, -1/3 , 0, 0,
			1, 1, -1/3, -1/3 , 0,
			1, 1, 1, -1/3, -1/3 
                  ), nrow = 6, byrow = TRUE)

# Set unequality signs
f.dir <- c("=",
           ">=",
		">=",
		">=",
		">=",
		">=")

# Set right hand side coefficients
f.rhs <- c(150,
           -20,
		-2,
		5,
		60,
		100)

# Final value (z)
lp("max", f.obj, f.con, f.dir, f.rhs)

# Variables final values
lp("max", f.obj, f.con, f.dir, f.rhs)$solution