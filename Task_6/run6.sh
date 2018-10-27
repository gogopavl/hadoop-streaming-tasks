hadoop jar /opt/hadoop/hadoop-2.9.1/share/hadoop/tools/lib/hadoop-streaming-2.9.1.jar \
	-D mapred.job.name="AAA_gogopavl_T6" \
	-D mapred.reduce.tasks=1 \
	-input /data/large/imdb/title.ratings.tsv \
	-output /user/s1884197/data/output/task6/out \
	-mapper mapper6.py \
	-reducer reducer6.py \
	-file mapper6.py \
	-file reducer6.py

