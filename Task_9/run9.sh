hdfs dfs -rm -r /user/s1884197/data/output/task9/

hadoop jar /opt/hadoop/hadoop-2.9.1/share/hadoop/tools/lib/hadoop-streaming-2.9.1.jar \
	-D mapred.job.name="Task9 s1884197" \
	-D mapred.reduce.tasks=1 \
	-input /data/large/imdb/title.basics.tsv \
	-output /user/s1884197/data/output/task9/ \
	-mapper mapper9.py \
	-reducer reducer9.py \
	-file mapper9.py \
	-file reducer9.py
