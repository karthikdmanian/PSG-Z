i=1;
sum=0;
while(i<1000)
    
    if(isprime(i)==1)
        sum=sum+i;
    end
    i=i+1;
end
disp(sum);