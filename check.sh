#!/bin/bash
rm report.txt
touch report.txt

for i in {1..10}
do
	echo "In directory $i" >> report.txt
	
	if [ $i = 8 ]; then
	     hdfs dfs -ls assignment/task$i/out >> report.txt
		hdfs dfs -cat assignment/task$i/out/* | wc -l >> report.txt
	else
	     hdfs dfs -ls assignment/task$i >> report.txt
		hdfs dfs -cat assignment/task$i/* | wc -l >> report.txt
  	fi
	
done
