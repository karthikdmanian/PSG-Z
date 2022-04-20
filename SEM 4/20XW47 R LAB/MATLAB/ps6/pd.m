syms x y
f=cos(2*x)-(x^2*exp(5*y))+3*(y^2);
px=diff(f,x)
py=diff(f,y)
pxx=diff(px,x)
pyy=diff(py,y)
pxy=diff(py,x)
pyx=diff(px,y)
pyyy=diff(pyy,y);
pyyyy=diff(pyyy,y)
pxyx=diff(pyx,x)