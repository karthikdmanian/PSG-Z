syms y(x)
ode5=diff(y,x)==sin(x)*cos(x)-cos(x)*y;
sol=dsolve(ode5)