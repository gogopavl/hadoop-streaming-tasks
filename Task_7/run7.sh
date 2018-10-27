hdfs dfs -rm -r /user/s1884197/data/output/task7/

hadoop jar /opt/hadoop/hadoop-2.9.1/share/hadoop/tools/lib/hadoop-streaming-2.9.1.jar \
	-D mapred.job.name="Task7 s1884197" \
	-D mapred.reduce.tasks=1 \
	-input /data/large/imdb/title.crew.tsv \
	-output /user/s1884197/data/output/task7/ \
	-mapper mapper7.py \
	-reducer reducer7.py \
	-file mapper7.py \
	-file reducer7.py
