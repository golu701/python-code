# pip install speedtest-cli

import speedtest

s = speedtest.Speedtest()
print("Testing..\n")

downloadSpeed = s.download()/1048576
uploadSpeed = s.upload()/1048576
pingResult = round(s.results.ping)

print(f"Download Speed: {downloadSpeed: .2f}Mbps")
print(f"Upload Speed: {uploadSpeed: .2f}Mbps")
print(f"Ping: {pingResult}ms")
