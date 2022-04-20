hw=[];
mid_term=[];
final_grade=0;
function[marks]=marksCalc(R)
    for i=1:1:6
        hw(i)= R(i);
    end
    for i=7:1:9
        mid_term(i)=R(i);
    end
    final_grade=R(10);
    
    marks=R;
    return marks;
end