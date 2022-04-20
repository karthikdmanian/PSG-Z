age=25;
initial=5000;
sum=initial;
while(sum<10^6)
   age=age+1;
   sum=sum+(9/100)*(sum)+5000;
end
disp(age)