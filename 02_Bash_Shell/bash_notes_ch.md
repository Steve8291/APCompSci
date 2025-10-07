# Bash Notes
## echo
打印到标准输出。  
```bash
echo "Hello World"
```
您还可以显示变量的值
```bash
my_variable="This is my variable"
echo "$my_variable"
```

## ls
列出目录的内容。  
```bash
ls # 列出当前目录内容
ls /var/log # 列出 var 目录的内容
ls -h # 列出人类可读的大小和日期
ls -a # 列出所有文件，包括以 开头的隐藏文件 '.'
ls .. # 列出父目录的内容
ls . # 列出当前目录的内容
```

## Redirects `>` `>>` and Pipes `|`
您可以使用重定向将任何命令的输出发送到文件。
您甚至可以创建一个包含多个命令的长管道，然后将最终输出重定向到文件。例如，您可以使用 grep 查找所有匹配项，使用管道进行排序，然后重定向到文件。  

`command > file` 将 `command` 的输出重定向到 `file`。如果 `file` 存在，则在写入之前清空它。
`command >> file` 将 `command` 的输出重定向到 `file`。如果 `file` 存在，则将其附加到其中。
```bash
echo "Hello" > output.txt  # 使用“Hello”创建或覆盖 output.txt
echo "World" >> output.txt  # 将“World”附加到 output.txt
```
管道将一个命令的输出连接到另一个命令的输入，从而创建一个管道！
`command1 | command2` `command1` 的输出成为 `command2` 的输入
```bash
ls /var/log | grep ".log" # 列出文件，然后过滤包含 ".log" 的行
ls /var/log | grep ".log" | sort # 对最终输出进行排序
```

## ssh
用于使用用户名和端口连接到远程服务器。
```bash
ssh -p 4666 bob@bandit.labs.overthewire.org # 使用用户名 bob 连接到 bandit.labs.overthewire.org 服务器的 4666 端口
```

## cat
打印文件内容。
```bash
cat readme.txt # 将 readme.txt 的内容打印到屏幕上
cat readme.txt > newfile.txt # 将一个文件的内容复制到另一个文件。
```

## pwd
打印当前工作目录路径的简单命令。
```bash
pwd
```

## grep
用于在文件中搜索文本模式。
```bash
grep 'dogs' myanimals.txt # 在 myanimals.txt 中搜索单词 'dogs'
grep -i 'dogs' myanimals.txt # 忽略大小写
grep -r 'dogs' ~/Desktop # 递归搜索 Desktop 中的所有文件
grep -v 'dogs' myanimals.txt # 反转匹配。除了 'dogs' 之外的所有匹配项
```

## cd
更改目录。
```bash
cd /path/to/directory
cd ~ # 回到你的主目录
cd .. # 回到上一级目录
cd - # 回到上一级目录
```

## 相对路径和绝对（完整）路径
绝对路径是指从根目录开始，一直到你的文件或目录的路径：
```bash
/home/bilbo/Desktop/my_file.txt
```
你也可以使用相对于当前目录的路径。例如，如果你切换到桌面目录，你可以像这样指定同一个文件：
```bash
my_file.txt
./my_file.txt
../file_in_bilbo_dir.txt
```
第二种方法使用 `./` 指定你当前所在的目录，然后指定文件名。当您尝试运行像 `./my_script.sh` 这样的可执行文件时，这很有用。
第三种方法使用 `../` 来指定当前所在目录的上一级目录中的文件。在本例中，由于您当前位于 `Desktop` 目录中，因此上一级目录中的文件是 `bilbo` 目录。

如果文件命名不当，例如文件名以 `-` 开头，则需要使用绝对路径名或 `./` 来引用该文件。

如果文件名中包含空格，则必须将整个路径括在引号中或转义所有空格。
第二个示例显示使用 `\` 转义空格：
```bash
"/home/bilbo/Desktop/poorly named file.txt"
/home/bilbo/Desktop/poorly\ named\ file.txt
```

## mv
用于移动或重命名文件和目录。
移动文件或目录：
```bash
mv /path/to/source/file.txt /path/to/destination/
mv /home/bilbo/Desktop/my_file.txt /tmp/ # 将 my_file.txt 移动到 /tmp/my_file.txt
```
重命名文件或目录：
```bash
mv my_file.txt new_name.txt # 注意：此命令假设您位于包含该文件的目录中。
mv my_file.txt /tmp/new_name.txt # 将文件重命名并移动到 /tmp/

## rm

## file

## sort

## man

## uniq

## less

## nano

