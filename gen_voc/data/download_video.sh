#!/bin/bash
cat $1 | while read line
do
	echo $line
	dirpath=${line%/*}
	filename=${line##*/}
	echo $dirpath
	if [ -d "$dirpath/video" ];then  
		rm -rf $dirpath/video
	fi
	continue
	if [ ! -d "$dirpath/video" ];then  
		mkdir -p $dirpath/video
	fi
	cat $line | while read info
	do
		vurl=${info%	*}
		echo $vurl
		you-get -o $dirpath/video $vurl
	done
done
