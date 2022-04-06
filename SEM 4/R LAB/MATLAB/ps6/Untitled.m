syms x y z
f2=1/(x^2+5*x+6);
f3=power(9-(4*x*x),0.5);
f4=log(tan(x));
f5=1/(1+sqrt(cot(x)));
f6=sin(x)*cos(x)^4;
f7=@(x,y) 12.*x.^2.*y.^3;
f8=@(x,y) x.*exp(x.*y);
f9=@(x,y,z) 8.*x.*y.*z ;
f10=@(x,y,z) (x+y);
zmax=@(x,z) 4-x.^2;
int(sin(2*x)*cos(x));
%int(f2)
%int(f3)
%int(f4,0,pi/2)
%int(f5,pi/6,pi/3);
%int(f6,-1,1);
%integral2(f7,1,2,-1,0);
%integral2(f8,1,2,1,3)
integral3(f9,0,1,0,2,0,3);
integral3(f10,0,2,0,1,0,zmax)