hdfs dfs -rm -r /user/s1884197/data/output/task5/

hadoop jar /opt/hadoop/hadoop-2.9.1/share/hadoop/tools/lib/hadoop-streaming-2.9.1.jar \
	-D mapred.job.name="Task5 s1884197" \
	-D mapred.reduce.tasks=1 \
	-input /data/large/imdb/title.basics.tsv \
	-output /user/s1884197/data/output/task5/ \
	-mapper mapper5.py \
	-reducer reducer5.py \
	-file mapper5.py \
	-file reducer5.py
