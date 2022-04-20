arr=[3:10];
i=floor(rand()*length(arr))+1;
while(~(arr(i)==5))
    disp(arr(i));
    i=floor(rand()*length(arr))+1;
end
disp(5);
disp("loop end");