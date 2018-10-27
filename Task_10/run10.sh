<<<<<<< HEAD
hdfs dfs -rm -r /user/$USER/data/output/task10/out

hadoop jar /opt/hadoop/hadoop-2.9.1/share/hadoop/tools/lib/hadoop-streaming-2.9.1.jar \
	-D mapred.job.name="AAA_gogopavl_T10" \
	-D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
	-D mapreduce.map.output.key.field.separator=. \
	-D stream.map.output.field.separator=. \
	-D stream.num.map.output.key.fields=2 \
	-D num.key.fields.for.partition=1 \
	-input /data/large/imdb/name.basics.tsv \
	-input /data/large/imdb/title.basics.tsv \
	-output /user/s1884197/data/output/task10/out \
	-mapper mapper10.py \
	-reducer reducer10.py \
	-file mapper10.py \
	-file reducer10.py \
	-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner
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
