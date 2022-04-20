arr_main=[];
arr=[3:10];
i=1;
r=floor(rand()*length(arr))+1;
while(i<=10)
    arr_main(i)=arr(r);
    r=floor(rand()*length(arr))+1;
    i=i+1;
end
disp(arr_main)
    