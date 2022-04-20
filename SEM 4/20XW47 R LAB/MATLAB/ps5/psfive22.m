sum=0;
tog=1;
for i=1:2:9999
    if(tog==1)
      sum=sum+i^2
      tog=0;
    else(tog==0)
      sum=sum-i^2
      tog=1;
    end
end
disp(sum)

    