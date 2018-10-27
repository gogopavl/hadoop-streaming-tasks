<<<<<<< HEAD
hdfs dfs -rm -r /user/$USER/data/output/task9/out

hadoop jar /opt/hadoop/hadoop-2.9.1/share/hadoop/tools/lib/hadoop-streaming-2.9.1.jar \
	-D mapred.job.name="gogopavl-word-line" \
	-D mapred.reduce.tasks=1 \
	-input /data/large/imdb/title.basics.tsv \
	-output /user/s1884197/data/output/task9/out \
	-mapper mapper9.py \
	-reducer reducer9.py \
	-file mapper9.py \
	-file reducer9.py
=======
hadoop jar /opt/hadoop/hadoop-2.9.1/share/hadoop/tools/lib/hadoop-streaming-2.9.1.jar \
	-D mapred.job.name="gogopavl-word-line" \
	-D mapred.reduce.tasks=1 \
	-input /data/small/gutenberg/8830902613096153013.txt \
	-output /user/s1884197/data/output/task1/out \
	-mapper mapper1.py \
	-reducer reducer1.py \
	-file mapper1.py \
	-file reducer1.py
>>>>>>> c6849e9bded7996b647936969a736cc117dfe8fc
