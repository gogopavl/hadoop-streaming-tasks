hdfs dfs -rm -r /user/s1884197/assignment/task9/

hadoop jar /opt/hadoop/hadoop-2.9.1/share/hadoop/tools/lib/hadoop-streaming-2.9.1.jar \
	-D mapred.job.name="Task9 s1884197" \
	-input /data/large/imdb/title.basics.tsv \
	-output /user/s1884197/assignment/task9/ \
	-mapper mapper.py \
	-reducer reducer.py \
	-file mapper.py \
	-file reducer.py

hdfs dfs -cat /user/s1884197/assignment/task9/part-00000 | head -20 > output.out
