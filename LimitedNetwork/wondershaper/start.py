from conf import PhyClusterConf
import os
import sys

theConf = PhyClusterConf()

start_command_middle = "sudo bash /home/swang/workspace/Shell/wondershaper/wondershaper/wondershaper "
start_command_post = "-u " + theConf.upload_rate_inKbps + " -d " + theConf.download_rate_inKbps

i = 0

for slave in theConf.slaves:
	start_command_prev = "ssh swang@" + slave + " "
	start_command_addr = "-a " + theConf.ipaddrs[i] + " "
	start_command = start_command_prev + start_command_middle + start_command_addr + start_command_post
	print start_command
	i = i + 1
	#os.popen(start_command)
