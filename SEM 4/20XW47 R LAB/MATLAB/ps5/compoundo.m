initial=1000;
sum=initial;
v=[];
for i=1:1:30
    v(i)=sum;
    sum = sum+(8/100)*sum;
end
disp(sum)
x=[1:1:30];
plot(x,v);