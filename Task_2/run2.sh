hadoop jar /opt/hadoop/hadoop-2.9.1/share/hadoop/tools/lib/hadoop-streaming-2.9.1.jar \
<<<<<<< HEAD
	-D mapred.job.name="AAA_gogopavl_T2" \
	-input /data/large/gutenberg/ \
	-output /user/s1884197/data/output/task2/out \
	-mapper mapper2.py \
	-reducer reducer2.py \
	-file mapper2.py \
	-file reducer2.py
=======
	-D mapred.job.name="gogopavl-word-line" \
	-D mapred.reduce.tasks=1 \
	-input /data/small/gutenberg/8830902613096153013.txt \
	-output /user/s1884197/data/output/task1/out \
	-mapper mapper1.py \
	-reducer reducer1.py \
	-file mapper1.py \
	-file reducer1.py
>>>>>>> c6849e9bded7996b647936969a736cc117dfe8fc
