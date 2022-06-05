library(lpSolve)
f.obj<-c(2,3)
f.con<-matrix(c(2,3,
		    2,6),nrow=2,byrow=TRUE)
f.dir<-c("<=","<=")
f.rhs<-c(8,18)
optimum<-lp("max",f.obj,f.con,f.dir,f.rhs)
var_solution<-lp("max",f.obj,f.con,f.dir,f.rhs)$solution
opt<-optimum$objval
cat("Optimum value is ",opt)
cat("variables final value is ",var_solution[1],var_solution[2])
dcons<-lp("max",f.obj,f.con,f.dir,f.rhs,compute.sens=TRUE)$duals
cat("Dual values are \n",dcons[1],"\n",dcons[2])

# Duals lower and upper limits
lowerLimit<-lp("max", f.obj, f.con, f.dir, f.rhs, compute.sens=TRUE)$duals.from
upperLimit<-lp("max", f.obj, f.con, f.dir, f.rhs, compute.sens=TRUE)$duals.to

cat("Dual values Limits are :\n",lowerLimit[1]," ",lowerLimit[2])
cat(upperLimit[1]," ",upperLimit[2])

d1<-dcons[1]-.30

if(f.rhs[1]+4>=lowerLimit[1]&&f.rhs[1]+4<=upperLimit[1]){
	newopt=opt+(d1*4);
	if(newopt>opt){
		print("Recommended")
	}
	else{
		print("Not Recommended")
	}
}

#as the dual price of m2 is 0 the optimum will not change.


