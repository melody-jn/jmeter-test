#!/usr/bin/env bash
docker rm -f stability
docker run -t --name stability \
	-v $(pwd):/app/ \
	-v $(pwd)/result:/app/result/ \
	-v /etc/localtime:/etc/localtime:ro \
	--env-file=./local-test.env \
	index.alauda.cn/alaudaorg/jmeter_test /bin/sh /app/stability.sh
