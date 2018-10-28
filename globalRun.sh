#!/bin/bash

for i in {1..10}
do
	cd task$i
	./run.sh
	cd ..
done

echo "Finished :)"
