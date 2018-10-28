hdfs dfs -rm -r /user/s1884197/assignment/task8/

hadoop jar /opt/hadoop/hadoop-2.9.1/share/hadoop/tools/lib/hadoop-streaming-2.9.1.jar \
	-D mapred.job.name="Task8_Job1 s1884197" \
	-input /data/large/imdb/title.basics.tsv \
	-input /data/large/imdb/title.ratings.tsv \
	-output /user/s1884197/assignment/task8/job1_out/ \
	-mapper mapper1.py \
	-reducer reducer1.py \
	-file mapper1.py \
	-file reducer1.py

hadoop jar /opt/hadoop/hadoop-2.9.1/share/hadoop/tools/lib/hadoop-streaming-2.9.1.jar \
	-D mapred.job.name="Task8_Job2 s1884197" \
	-input /user/s1884197/assignment/task8/job1_out/ \
	-output /user/s1884197/assignment/task8/out/ \
	-mapper mapper2.py \
	-reducer reducer2.py \
	-file mapper2.py \
	-file reducer2.py

hdfs dfs -cat /user/s1884197/assignment/task8/out/* | sort -k1,1 > output.out

