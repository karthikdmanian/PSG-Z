BEGIN{
print "Report";
}
{
deptsales[$2]+=$3;
}
END{
for(x in deptsales)
	print x,deptsales[x]
}
