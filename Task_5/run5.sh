hadoop jar /opt/hadoop/hadoop-2.9.1/share/hadoop/tools/lib/hadoop-streaming-2.9.1.jar \
<<<<<<< HEAD
	-D mapred.job.name="AAA_gogopavl_T5" \
	-D mapred.reduce.tasks=1 \
	-input /data/large/imdb/title.basics.tsv \
	-output /user/s1884197/data/output/task5/out \
	-mapper mapper5.py \
	-reducer reducer5.py \
	-file mapper5.py \
	-file reducer5.py
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
