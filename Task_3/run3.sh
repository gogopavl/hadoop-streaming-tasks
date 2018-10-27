hadoop jar /opt/hadoop/hadoop-2.9.1/share/hadoop/tools/lib/hadoop-streaming-2.9.1.jar \
	-D mapred.job.name="AAA_gogopavl_T3" \
	-D mapred.reduce.tasks=1 \
	-input /data/large/imdb/name.basics.tsv \
	-output /user/s1884197/data/output/task3/out \
	-mapper mapper3.py \
	-reducer reducer3.py \
	-file mapper3.py \
	-file reducer3.py
