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
cat("variables final value is ",var_solution[1],var_solution[2])

lp("max",f.obj,f.con,f.dir,f.rhs,compute.sens=TRUE)$duals

# Duals lower and upper limits
lp("max", f.obj, f.con, f.dir, f.rhs, compute.sens=TRUE)$duals.from
lp("max", f.obj, f.con, f.dir, f.rhs, compute.sens=TRUE)$duals.to

if(f.rhs[1]-30>=lowerLimit[1]&&f.rhs[1]-30<=upperLimit[1]){
	cat("New optimal:",opt-(30*opt$duals[1])
}