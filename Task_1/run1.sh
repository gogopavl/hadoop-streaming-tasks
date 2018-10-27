hdfs dfs -rm -r /user/s1884197/data/output/task1/

hadoop jar /opt/hadoop/hadoop-2.9.1/share/hadoop/tools/lib/hadoop-streaming-2.9.1.jar \
	-D mapred.job.name="Task1 s1884197" \
	-D mapred.reduce.tasks=1 \
	-input /data/large/gutenberg \
	-output /user/s1884197/data/output/task1/ \
	-mapper mapper1.py \
	-reducer reducer1.py \
	-combiner reducer1.py \
	-file mapper1.py \
	-file reducer1.py
