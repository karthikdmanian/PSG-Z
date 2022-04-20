syms y(x)
%yp=diff(y,x)
%ypp=diff(y,x,2);
%eqn=ypp+(4*i+1)*yp+y==0;
%cond=[y(0)==1,yp(0)];
%sol=dsolve(eqn,cond)

%8

%yp=diff(y,x);
%ypp=diff(y,x,2);
%eqn=ypp==4-sin(x)+y-2*yp;
%cond=[y(0)==1,yp(0)==2];
%sol=dsolve(eqn,cond)

%9

%yp=diff(y,x);
%ypp=diff(y,x,2);
%yppp=diff(y,x,3);
%eqn=yppp==y-x*yp+4*ypp;
%cond=[y(2)==1,yp(2)==1/2,ypp(2)==0];
%sol=dsolve(eqn,cond)

%1
%yp=diff(y,x);
%cond=y(0)==48;
%eqn=yp==9.8-0.196*y;
%dsolve(eqn,cond)
