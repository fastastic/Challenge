# After some executions the nginx log has useful information, how would you extract the nginx log? Can you parse the Nginx log and get a sorted list of the HTTP status codes?
import os

os.system('docker logs custom_nginx_container > logs.txt')

status_codes = []
for line in open("logs.txt", "r"):
	split_line = line.split(" ")
	if split_line[0] == "172.17.0.1":
		status_codes.append(split_line[8])

status_codes.sort()

print(status_codes)
