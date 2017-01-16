#!/usr/bin/env bash
cd a1/
make
for i in {0..9}
do
	./run.sh test/$i.in > /tmp/tmpfile
	diff test/$i.out /tmp/tmpfile
done
