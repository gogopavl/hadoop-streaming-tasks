hdfs dfs -rm -r /user/s1884197/data/output/task4/

hadoop jar /opt/hadoop/hadoop-2.9.1/share/hadoop/tools/lib/hadoop-streaming-2.9.1.jar \
	-D mapred.job.name="Task4 s1884197" \
	-D mapred.reduce.tasks=1 \
	-input /data/large/imdb/title.basics.tsv \
	-output /user/s1884197/data/output/task4/ \
	-mapper mapper4.py \
	-reducer reducer4.py \
	-file mapper4.py \
	-file reducer4.py
