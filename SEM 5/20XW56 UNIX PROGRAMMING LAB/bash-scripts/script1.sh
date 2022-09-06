echo "UNIX SUN OS"
echo "LINUX REDHAT"
echo "Enter ur choice 1 or 2"
read osch

if [ $osch -eq 1 ]
then
	echo "You picked unix";
elif [ $osch -eq 2 ]
then
	echo "You picked Linux";
else
	echo "Not an option";
fi

