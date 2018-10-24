hadoop jar /opt/hadoop/hadoop-2.9.1/share/hadoop/tools/lib/hadoop-streaming-2.9.1.jar \
	-D mapred.job.name="Word counter" \
	-D mapred.reduce.tasks=1 \
	-input <input> \
	-output <output> \
	-mapper mapper.py \
	-reducer reducer.py \
	-file mapper.py \
	-file reducer.py