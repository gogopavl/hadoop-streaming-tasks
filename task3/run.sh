hdfs dfs -rm -r /user/s1884197/assignment/task3/

hadoop jar /opt/hadoop/hadoop-2.9.1/share/hadoop/tools/lib/hadoop-streaming-2.9.1.jar \
	-D mapred.job.name="Task3 s1884197" \
	-D mapred.reduce.tasks=1 \
	-input /data/large/imdb/name.basics.tsv \
	-output /user/s1884197/assignment/task3/ \
	-mapper mapper.py \
	-reducer reducer.py \
	-combiner reducer.py \
	-file mapper.py \
	-file reducer.py

hdfs dfs -cat /user/s1884197/assignment/task3/* > output.out
