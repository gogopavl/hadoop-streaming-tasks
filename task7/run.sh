hdfs dfs -rm -r /user/s1884197/assignment/task7/

hadoop jar /opt/hadoop/hadoop-2.9.1/share/hadoop/tools/lib/hadoop-streaming-2.9.1.jar \
	-D mapred.job.name="Task7 s1884197" \
	-D mapred.reduce.tasks=1 \
	-input /data/large/imdb/title.crew.tsv \
	-output /user/s1884197/assignment/task7/ \
	-mapper mapper.py \
	-reducer reducer.py \
	-file mapper.py \
	-file reducer.py

hdfs dfs -cat /user/s1884197/assignment/task7/* > output.out
