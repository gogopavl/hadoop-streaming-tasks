hdfs dfs -rm -r /user/s1884197/assignment/task2/

hadoop jar /opt/hadoop/hadoop-2.9.1/share/hadoop/tools/lib/hadoop-streaming-2.9.1.jar \
	-D mapred.job.name="Task2 s1884197" \
	-input /data/large/gutenberg/ \
	-output /user/s1884197/assignment/task2/ \
	-mapper mapper.py \
	-reducer reducer.py \
	-file mapper.py \
	-file reducer.py

hdfs dfs -cat /user/s1884197/assignment/task2/part-00000 | head -20 > output.out
