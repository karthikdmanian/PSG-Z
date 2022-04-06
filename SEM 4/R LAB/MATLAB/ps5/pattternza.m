x=['*' '*' '*' '*' '*'];
hax=[0 0 0 0 0];
k=ceil(5/2)
for i=1:1:5
    hax(k)=1
    for j=1:1:5
        if(hax(j))
            fprintf(x(j));
        end
    end
    fprintf("\n");
end