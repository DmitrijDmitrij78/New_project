#!/bin/bash
MY_DIRECTORIES="/home"
echo "Top Ten Disk Space Usage"
for DIR in $MY_DIRECTORIES
do
echo "Домашняя директория состоит из:"
du -S $DIR 2>/dev/null | sort -rn | cat -n | head
done
exit

