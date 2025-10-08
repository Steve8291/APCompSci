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

## Redirects `>` `>>` and Pipes `|`
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

## Relative Paths and Absolute (Full) Paths
An absolute path is any path that starts with the root directory and goes all the way to your file or directory:  
```bash
/home/bilbo/Desktop/my_file.txt
```
You can also use a path that is relative to the directory you are in. For example, if you changed into the Desktop directory you could specify the same file like so:  
```bash
my_file.txt
./my_file.txt
../file_in_bilbo_dir.txt
```
The second method that uses the `./` specifies the directory you are currently in and then the file name. This is useful when you are trying to run an executable file like `./my_script.sh`  
The third method uses the `../` to specify a file that is sitting in the directory above the one you are currently in. In this case the `bilbo` dir since you are in the `Desktop` dir.  

When files get named poorly as in the case with a filename that starts with a `-` you will need to use the absolute path name or `./` to reference the file.  

If a file name has spaces in it you must either enclose the entire path in quotes or escape all the spaces.  
The second example shows using the `\` to escape spaces:  
```bash
"/home/bilbo/Desktop/poorly named file.txt"
/home/bilbo/Desktop/poorly\ named\ file.txt
```

## mv
Used to move or rename files and directories.  
To move a file or directory:  
```bash
mv /path/to/source/file.txt /path/to/destination/
mv /home/bilbo/Desktop/my_file.txt /tmp/  # Would move my_file.txt to /tmp/my_file.txt
```
To rename a file or directory:  
```bash
mv my_file.txt new_name.txt  # Note: this assumes you are inside of the directory containing the file.
mv my_file.txt /tmp/new_name.txt  # Would rename and move the file to /tmp/
```

## rm
This command will remove files and directories. Be careful, there is no undo!  
```bash
rm filename.txt  # Delete a file
rm file1.txt file2.txt file3.txt  # Delete multiple files
rm -r my_directory/  # Deletes an entire directory (-r is recursive)
```

## file
Tells you the type of a file like ASCII text or Binary. Useful because file extensions do not determine file type in linux.  
```bash
file filename.txt  # Prints the type of file.
file *  # Lists the file types of all files in the current directory.
```

## sort
Sorts the contents of a file and prints the sorted output.  
```bash
sort filename.txt     # Sorts alphanumerically
sort -r filename.txt  # Sorts in reverse
sort -u filename.txt  # Suppresses duplicate lines
sort -k 2 data.csv    # Sort spreadsheet data by the second field
```

## man
Used to display the manual pages (man pages) for commands.  
```bash
man ls  # Opens the man page for the command "ls"
```
- `/search_term` Type `/` to search the page.
    - `n` or `enter` Jumps to the next search match.
    - `N` Jump to the previous search match.
- `G` Jump back to the beginning of the page.
- `g` Jump to the end of the page.
- `q` Exit the man page.

## uniq
Detects duplicate lines in a file. The lines must be right next to each other. It is often best to pipe from `sort` to `uniq`.  
```bash
uniq filename.txt  # Prints all lines except duplicates.
uniq input.txt output.txt  # Removes duplicate lines and saves as new file "output.txt"
sort filename.txt | uniq  # The safest way to use uniq is to pipe sorted output to it.
```

## less
Used to read text files. Does not allow you to edit the file. This is the same pager that opens with a man page so the commands are similar.  
```bash
less textfile.txt
```
- `/search_term` Type `/` to search the page.
    - `n` or `enter` Jumps to the next search match.
    - `N` Jump to the previous search match.
- `G` Jump back to the beginning of the page.
- `g` Jump to the end of the page.
- `q` Exit the man page.

## nano
Command line text editor.  
```bash
nano filename.txt  # Creates filename.txt if it doesn't exist and opens it.
```
- `Ctrl+K` Cuts a line.
- `Ctrl+U` Pastes a line.
- `Ctrl+O` Saves file.
- `Ctrl+X` Exits with option to save.
- `Ctrl+W` Search file for term.
    - `Alt+W` Find the next match for search.
- `Alt+T` Cuts all text from the cursor to end of file. Can be used to clear the file if you do it on the first line of the file.