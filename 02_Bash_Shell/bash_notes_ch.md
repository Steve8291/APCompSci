# Bash 注释
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
ls # 列出当前目录的内容
ls /var/log # 列出 var 目录的内容
ls -h # 列出可读的大小和日期
ls -a # 列出所有文件，包括以“.”开头的隐藏文件
ls .. # 列出父目录的内容
ls . # 列出当前目录的内容
```

## 重定向 `>` `>>` 和管道 `|`
您可以使用重定向将任何命令的输出发送到文件。
您甚至可以创建一个包含多个命令的长管道，然后将最终输出重定向到文件。例如，您可以使用 grep 查找所有匹配项，使用管道进行排序，然后重定向到文件。

`command > file` 将 `command` 的输出重定向到 `file`。如果 `file` 存在，则在写入之前清空它。
`command >> file` 将 `command` 的输出重定向到 `file`。如果 `file` 存在，则将其附加到该文件。
```bash
echo "Hello" > output.txt # 创建或用“Hello”覆盖 output.txt
echo "World" >> output.txt # 将“World”附加到 output.txt
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
ssh -p 4666 bob@bandit.labs.overthewire.org # 使用用户名 bob 连接到 bandit.labs.overthewire.org 服务器的 4666 端口。
```

## cat
打印文件内容。
```bash
cat readme.txt # 将 readme.txt 的内容打印到屏幕上。
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
```

## rm
此命令将删除文件和目录。请注意，无法撤消！
```bash
rm filename.txt # 删除一个文件
rm file1.txt file2.txt file3.txt # 删除多个文件
rm -r my_directory/ # 删除整个目录（-r 为递归）
```

## file
显示文件类型，例如 ASCII 文本或二进制文件。这很有用，因为在 Linux 中文件扩展名并不能决定文件类型。
```bash
file filename.txt # 打印文件类型。
file * # 列出当前目录中所有文件的文件类型。
```

## sort
对文件内容进行排序并打印排序后的输出。
```bash
sort filename.txt # 按字母数字顺序排序
sort -r filename.txt # 反向排序
sort -u filename.txt # 抑制重复行
sort -k 2 data.csv # 按第二个字段对电子表格数据进行排序
```

## man
用于显示命令的手册页（man pages）。
```bash
man ls # 打开命令“ls”的手册页
```
- `/search_term` 输入 `/` 以搜索页面。
- `n` 或 `enter` 跳转到下一个搜索匹配项。
- `N` 跳转到上一个搜索匹配项。
- `g` 跳回到页面开头。
- `G` 跳转到页面结尾。
- `q` 退出手册页。

## uniq
检测文件中的重复行。行必须紧挨着。通常最好通过管道从 `sort` 到 `uniq`。
```bash
uniq filename.txt # 打印除重复行之外的所有行。
uniq input.txt output.txt # 删除重复行并保存为新文件“output.txt”
sort filename.txt | uniq # 使用 uniq 最安全的方式是通过管道将排序后的输出传递给它。
```

## less
用于读取文本文件。不允许您编辑文件。这与使用手册页打开的分页器相同，因此命令类似。
```bash
less textfile.txt
```
- `/search_term` 输入 `/` 以搜索页面。
- `n` 或 `enter` 跳转到下一个搜索匹配项。
- `N` 跳转到上一个搜索匹配项。
- `g` 跳回到页面开头。
- `G` 跳转到页面结尾。
- `q` 退出手册页。

## nano
命令行文本编辑器。
```bash
nano filename.txt # 如果 filename.txt 不存在，则创建并打开它。
```
- `Ctrl+K` 剪切一行。
- `Ctrl+U` 粘贴一行。
- `Ctrl+O` 保存文件。
- `Ctrl+X` 退出并显示保存选项。
- `Ctrl+W` 搜索文件中的术语。
- `Alt+W` 查找下一个匹配项。
- `Alt+T` 剪切从光标到文件末尾的所有文本。如果在文件第一行执行此操作，则可以清除文件。
