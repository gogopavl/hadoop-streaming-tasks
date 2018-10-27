hdfs dfs -rm -r /user/$USER/data/output/task8/outJob1
hdfs dfs -rm -r /user/$USER/data/output/task8/out

hadoop jar /opt/hadoop/hadoop-2.9.1/share/hadoop/tools/lib/hadoop-streaming-2.9.1.jar \
	-D mapred.job.name="AAA_gogopavl_T8_1" \
	-input /data/large/imdb/title.basics.tsv \
	-input /data/large/imdb/title.ratings.tsv \
	-output /user/s1884197/data/output/task8/outJob1 \
	-mapper mapper8Task1.py \
	-reducer reducer8Task1.py \
	-file mapper8Task1.py \
	-file reducer8Task1.py

hadoop jar /opt/hadoop/hadoop-2.9.1/share/hadoop/tools/lib/hadoop-streaming-2.9.1.jar \
	-D mapred.job.name="AAA_gogopavl_T8_2" \
	-input /user/s1884197/data/output/task8/outJob1 \
	-output /user/s1884197/data/output/task8/out \
	-mapper mapper8Task2.py \
	-reducer reducer8Task2.py \
	-file mapper8Task2.py \
	-file reducer8Task2.py

