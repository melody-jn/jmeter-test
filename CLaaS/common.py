#coding=utf-8
import json

import requests

import settings

headers = {
    "Authorization": "Token " + settings.API_TOKEN,
    'content-type': 'application/json'
}


def send_metrics_case_details(timestamp, casetime, casename, case_flag):
    success = 0
    if case_flag == 'true':
        success = 1
    elif case_flag == 'false':
        success = 0
    else:
        print '====case_flag is error===='
    payload = [
        {
            "metric_name": "e2e.run.case.success",
            "tags": {"casename": casename},
            "timestamp": timestamp,
            "value": success,
            "metric_type": "gauge",
            "unit": None
        },
        {
            "metric_name": "e2e.run.case.time",
            "tags": {"casename": casename},
            "timestamp": timestamp,
            "value": casetime,
            "metric_type": "gauge",
            "unit": None
        }
    ]
    return send_metrics(payload)


def send_metrics_case_total(totalcasenum, totaltime, failedcasesnum, sucesscasenum, timestamp):
    payload = [
        {
            "metric_name": "e2e.run.case.total.number",
            "tags": {"region": settings.REGION_NAME},
            "timestamp": timestamp,
            "value": totalcasenum,
            "metric_type": "gauge",
            "unit": None
        },
        {
            "metric_name": "e2e.run.case.total.time",
            "tags": {"region": settings.REGION_NAME},
            "timestamp": timestamp,
            "value": totaltime,
            "metric_type": "gauge",
            "unit": None
        },
        {
            "metric_name": "e2e.run.case.total.failednumber",
            "tags": {"region": settings.REGION_NAME},
            "timestamp": timestamp,
            "value": failedcasesnum,
            "metric_type": "gauge",
            "unit": None
        },
        {
            "metric_name": "e2e.run.case.total.succeedednumber",
            "tags": {"region": settings.REGION_NAME},
            "timestamp": timestamp,
            "value": sucesscasenum,
            "metric_type": "gauge",
            "unit": None
        }
    ]
    return send_metrics(payload)


def send_metrics(payload):
    url = settings.API_URL.replace('v1', 'v2') + 'monitor/metrics/put'
    r = requests.post(url=url, data=json.dumps(payload), headers=headers)
    print '======post metrics reposne======='
    print r
    if r.status_code != 204:
        return {"success": False,
                "message": '发送metrics失败，错误代码：{}，错误信息：{}'.format(r.status_code, r.text)}

    return {"success": True, "message": "发送metrics成功"}
