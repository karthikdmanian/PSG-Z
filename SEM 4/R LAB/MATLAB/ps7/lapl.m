%1

%syms t;
%f(t) = 3*t^2 + 4*t +5;
%g(t) = cos(t)^2 + 2*exp(-3*t) - 7;
%h(t) = exp(3*t)*cosh(2*t);
%j(t) = sinh(t)*cos(3*t);
%k(t) = (t + 1)^2 *exp(3*t);

%laplace(f)
%laplace(g)
%laplace(h)
%laplace(j)
%laplace(k)

%2

%syms s;

%F1(s) = (-s-10)/(s^2 - s - 2);
%F2(s) = (s-2)/(s^2 - 16);
%F3(s) = 3/(s^2 + 6*s + 18);
%F4(s) = (s^4 + 6*s - 18)/(s^5 - 3*s^4);
%F5(s) = 4/(s^2 - 2*s - 3);

%ilaplace(F1)
%ilaplace(F2)
%ilaplace(F3)
%ilaplace(F4)
%ilaplace(F5)

%3

%syms t;

%f1=t*cos(2*t);
%f2=t*sin(3*t)-2;
%f3=sin(2*t)-2*t*cos(2*t);
%f4=sin(3*t)+3*t*cos(3*t);
%f5=t*exp(-2*t)*cos(3*t);

%function_plot
%fplot(f1)
%fplot(f2)
%fplot(f3)
%fplot(f4)
%fplot(f5)

%after_laplace
%fplot(laplace(f1));
%fplot(laplace(f2))
%fplot(laplace(f3));
%fplot(laplace(f4));
%fplot(laplace(f5))

%4

%syms s;
%F1=s^2/(s-1)^2;
%F2=s/(s^2-9)^2;
%F3=2*s/(s^2-s-2)^2;
%F4=s/(s^2+9)^2;
%F5=s^2/(s^2+16)^2;
%F6=4/(s^+25)^2;

%function_plot
%fplot(F1);
%fplot(F2);
%fplot(F3)
%fplot(F4);
%fplot(F5);

%after_INVERSE_laplace
%fplot(ilaplace(F1));
%fplot(ilaplace(F2));
%fplot(ilaplace(F3));
%fplot(ilaplace(F4));
%fplot(ilaplace(F5));

%5
syms t;
 
f1(t) = 3* (heaviside(t-0) - heaviside(t-2)) + 5* (heaviside(t-2));
f2(t) = 2* (heaviside(t-0) - heaviside(t-2)) - 1* (heaviside(t-2) - heaviside(t-3));
f3(t) = 15 * t * (heaviside(t-0) - heaviside(t-3));
f4(t) = sin(t)*(heaviside(t - 2*pi)); 
f5(t) = t^2 * (heaviside(t-3));
f6(t) = 2 * (heaviside(t-0) - heaviside(t-4)) + (t-1) * (heaviside(t-4) - heaviside(t-6));


%fplot(f1);
%fplot(laplace(f1))
%fplot(f2);
%fplot(laplace(f2))
%fplot(f3);
%fplot(laplace(f3))
%fplot(f4);
%fplot(laplace(f4))
%fplot(f5);
%fplot(laplace(f5))
%fplot(f6);
%fplot(laplace(f6))

%6

syms t s;
one(t) = t^0; %1
F1(s) = laplace(one) * laplace(one);
F2(s) = laplace(one) * laplace(sin(2*t));
F3(s) = laplace(exp(t)) * laplace(exp(-t));
F4(s) = laplace(exp(t)) * laplace(t);
F5(s) = laplace(cos(2*t)) * laplace(sin(3*t));
    

%fplot(ilaplace(F1))

%fplot(ilaplace(F2))

%fplot(ilaplace(F3))

%fplot(ilaplace(F4))

fplot(ilaplace(F5))

