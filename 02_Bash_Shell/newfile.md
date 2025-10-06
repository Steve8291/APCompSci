# Bash Notes
## echo
Prints to standard output.  
```bash
echo "Hello World"
```
You can also display the value of a variable
```bash
my_variable="This is my variable"
echo "$my_variable"
```

## ls
Lists the contents of a directory.  
```bash
ls # lists current directory contents
ls /var/log # lists content of var directory
ls -h # lists human readable size and dates
ls -a # lists all files including hidden files that start with '.'
ls .. # lists the content of the parent directory
ls . # lists the content of the current directory
```

## Redirects (> >>) and Pipes (|)
You can use a redirect to send the output of any command to a file.  
You could even create a long pipeline with multiple commands and then redirect the final output to a file. For example you could use grep to find all matches, pipe to sort and then redirect to a file.  

`command > file` Redirects the output of `command` to `file`. If `file` exists, it is emptied before writing.  
`command >> file` Redirects the output of `command` to `file`. If `file` exists, it is appended to.
```bash
echo "Hello" > output.txt  # Creates or overwrites output.txt with "Hello"
echo "World" >> output.txt  # Appends "World" to output.txt
```
Pipes connect output of one command to the input of another command, creating a pipeline!  
`command1 | command2` Output from `command1` becomes input of `command2`
```bash
ls /var/log | grep ".log" # Lists files, then filters for lines containing ".log"
ls /var/log | grep ".log" | sort # Sorts the final output
```

## ssh
Used to connect to a remote server with a username and port.  
```bash
ssh -p 4666 bob@bandit.labs.overthewire.org  # Connect to server bandit.labs.overthewire.org on port 4666 with username bob
```

## cat
Print out the contents of a file.  
```bash
cat readme.txt # prints the contents of readme.txt to screen
cat readme.txt > newfile.txt # Copies the contents of one file into another.
```


## pwd
Simple command to print the path to the present working directory.  
```bash
pwd
```

## grep
Used to search for text patterns within files.  
```bash
grep 'dogs' myanimals.txt # Seach myanimals.txt for the word 'dogs'
grep -i 'dogs' myanimals.txt # Ignore case
grep -r 'dogs' ~/Desktop # Search recursively through all files in Desktop
grep -v 'dogs' myanimals.txt # Inverts match. Everything but 'dogs'
```

## cd 
Changes your directory.  
```bash
cd /path/to/directory
cd ~  # Takes you to your home directory
cd ..  # Takes you up one directory
cd -  # Takes you back to last directory
```

## mv

## rm

## file

## sort

## man

## uniq

## less

## nano

