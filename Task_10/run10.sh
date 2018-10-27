hdfs dfs -rm -r /user/$USER/data/output/task10/

hadoop jar /opt/hadoop/hadoop-2.9.1/share/hadoop/tools/lib/hadoop-streaming-2.9.1.jar \
	-D mapred.job.name="Task10 s1884197" \
	-D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
	-D mapreduce.map.output.key.field.separator=. \
	-D stream.map.output.field.separator=. \
	-D stream.num.map.output.key.fields=2 \
	-D num.key.fields.for.partition=1 \
	-input /data/large/imdb/name.basics.tsv \
	-input /data/large/imdb/title.basics.tsv \
	-output /user/s1884197/data/output/task10/ \
	-mapper mapper10.py \
	-reducer reducer10.py \
	-file mapper10.py \
	-file reducer10.py \
	-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner

