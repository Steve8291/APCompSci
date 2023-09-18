#!/bin/bash
# The shebang

# This is a comment
echo "Hello World!" # This line should print something!

# Bash Scripting

# Talk about the command prompt '$' regular user, '#' root

date

pwd

ls

echo "Hello World!"

cd ..

# Try out a different flag for ls
man ls

touch my_file

nano

echo "New line here" >> my_file

mv

rm

which bash

ls /bin

# Everything in Linux is a file. Extensions are not mandatory but a convention.
nano my_script.sh



# Reading File Permissions:
# Owner, Group, World
# Using Binary References (add these for the permission you want to set)
# r = 4
# w = 2
# x = 1
# Example 740

ls -l my_script
chmod 700 my_script.sh
ls -l my_script
./my_script



# Variables
country="Canada"
echo "$country"

province="Alberta"
address="${province}, ${country}"
echo "Your address is: $address"


#!/bin/bash
echo "Today is $(date)"

echo -e "\nenter the path to directory"
read the_path

echo -e "\n you path has the following files and folders: "
ls "$the_path"


# Can you find a way to run your script when we move back up the file tree?
cd /home
/home/my_script


# Challenge to print a message, read in user input of a number and print the addition:
#!/bin/bash
echo "Let's do some addition"
echo "Please enter a number"

read -p "Please enter a number: " num


total=$((5 + num))

echo "5 + $num = $total"

# Integer Comparison Operators:
-eq 	Integer equality
-ne 	Integer inequality
-lt 	Integer less than
-le 	Integer less than or equal to
-gt 	Integer greater than
-ge 	Integer greater than or equal to

# Arithmetic Expansion Operators:
(( a > b ))
(( a >= b ))
(( a == b ))
(( a != b ))
&& 	Logical AND
|| 	Logical OR

# String Comparison Operators:
== (also =) 	String equality
!= 	String inequality


# If statements:
if [[ "$num" -gt 100 ]]; then
	echo Hey that\'s a large number.
fi



# Nested if statements
if [ "$num" -gt 100 ]; then
	echo Hey that\'s a large number.
	if (( $1 % 2 == 0 )); then
		echo And is also an even number.
	fi
fi

# else example
if [ "$num" -eq 1 ]; then
	echo "It's equal to 1"
else
	echo "You didn't enter 1"
fi



# elif statements
if [ "$num" -ge 18 ]; then
	echo You may go to the party.
elif [ "$num" == 'yes' ]; then
	echo "You may go to the party but be back before midnight."
else
	echo "You may not go to the party."
fi


# and example
if (( $num >= 8 )) && (( $num <= 10 )); then
	echo "You picked a number betweeen 8 and 10"
fi




echo "Enter an input integer Variable1: "
read variable1
echo "Enter an input integer variable2: "
read variable2
if (( $variable1 < $variable2 )); then
    echo "The Condition is True"
    echo "Return 0"
 else
    echo "The Condition is False"
    echo "Return 1"
fi


user_num=0
while [[ $user_num -le 4 ]]
do
	read -p "Enter a number between 5 and 10: " user_num
done

echo "Good job, your number was $user_num"


# Infinite Loop!
while true
do
	echo "Press [CTRL+C] to stop.."
	sleep 1
done