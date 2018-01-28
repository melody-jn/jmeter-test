from common import send_metrics_case_details

f = open("./result/stability.jtl", "rb")
while True:
    line = f.readline()
    content = line.split(',')
    print content
    if len(content) > 8:
        timeStamp = content[0]
        elapsed = content[1]
        label = content[2]
        success = content[7]
        print "{} {} {} {}".format(timeStamp, elapsed, label, success)
        send_metrics_case_details(timeStamp, elapsed, label, success)
    else:
        break
