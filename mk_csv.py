import configparser
import subprocess
import time,os


# file = '../failover.conf'
# config = configparser.ConfigParser()
# config.read(file)
# test_type = config.get('route_umts', 'gw_route').split(';')
# print(test_type)
# for test in test_type:
#   print(test)
#   gw_route = config.get('route_umts', test)
#   call_desc = gw_route.split(';')[0]
#   call_num = gw_route.split(';')[1]
#   with open('auto_call_test.csv','w') as f:
#       f.write(f'SEQUENTIAL\n{call_desc};{call_num};[authentication username={call_num} password=123456];10086')
#   time.sleep(2)
#   # nowtime = subprocess.Popen('cd /home/ray/p_file/SIPp_test && python3 test_sipp.py SIPp.conf sipp',stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
#   # out,err = nowtime.communicate()
#   # print(out.decode('utf-8'))
out = os.popen('python3 test_sipp.py SIPp.conf sipp').read()
# out = os.popen('').read()

print(out)
