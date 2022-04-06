v_odd=[1:2:9999];
disp(v_odd);
i=1;
sum=0;
while(v_odd(i)<9999)
    if mod(i,2)==0
        sum=sum+v_odd(i)*v_odd(i);
    elseif mod(i,2)==1
        sum=sum-v_odd(i)*v_odd(i);
    end
    i=i+1;
end
sum=sum-9999*9999;
disp(sum);