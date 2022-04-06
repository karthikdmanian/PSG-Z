function[area]=area_tri(a,b,c)
    s=(a+b+c)/2
    area=power(s*(s-a)*(s-b)*(s-c),0.5)
end