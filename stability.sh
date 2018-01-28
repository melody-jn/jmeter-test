#!/usr/bin/env bash
cd /app
rm -rf ./result/stability.jtl
rm -rf ./result/stability.log
/opt/jmeter/bin/jmeter.sh -n -t ./jmeter/stability.jmx -l ./result/stability.jtl -j ./result/stability.log
python ./CLaaS/send_metrics.py
