hdfs dfs -rm -r /user/s1884197/data/output/task6/

hadoop jar /opt/hadoop/hadoop-2.9.1/share/hadoop/tools/lib/hadoop-streaming-2.9.1.jar \
	-D mapred.job.name="Task6 s1884197" \
	-D mapred.reduce.tasks=1 \
	-input /data/large/imdb/title.ratings.tsv \
	-output /user/s1884197/data/output/task6/ \
	-mapper mapper6.py \
	-reducer reducer6.py \
	-file mapper6.py \
	-file reducer6.py

