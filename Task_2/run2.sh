hdfs dfs -rm -r /user/s1884197/data/output/task2/

hadoop jar /opt/hadoop/hadoop-2.9.1/share/hadoop/tools/lib/hadoop-streaming-2.9.1.jar \
	-D mapred.job.name="Task2 s1884197" \
	-input /data/large/gutenberg/ \
	-output /user/s1884197/data/output/task2/ \
	-mapper mapper2.py \
	-reducer reducer2.py \
	-file mapper2.py \
	-file reducer2.py
