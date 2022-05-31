library(lpSolve)
f.obj<-c(8,5)
f.con<-matrix(c(2,1,
		    1,0,
		    0,1),nrow=3,byrow=TRUE)
f.dir<-c("<=","<=","<=")
f.rhs<-c(400,150,200)
optimum<-lp("max",f.obj,f.con,f.dir,f.rhs)
var_solution<-lp("max",f.obj,f.con,f.dir,f.rhs)$solution
opt<-optimum$objval
cat("Optimum value is ",opt)
