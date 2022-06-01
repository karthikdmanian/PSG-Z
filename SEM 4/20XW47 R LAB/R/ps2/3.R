library(lpSolve)
f.obj<-c(20,50)
f.con<-matrix(c(2,4,
		    1,0,
		    -0.2,0.8),nrow=3,byrow=TRUE)
f.dir<-c("<=","<=","<=")
f.rhs<-c(240,100,0)
optimum<-lp("max",f.obj,f.con,f.dir,f.rhs)
var_solution<-lp("max",f.obj,f.con,f.dir,f.rhs)$solution
opt<-optimum$objval
cat("Optimum value is ",opt)
cat("variables final value is ",var_solution[1],var_solution[2])

lp("max",f.obj,f.con,f.dir,f.rhs,compute.sens=TRUE)$duals

