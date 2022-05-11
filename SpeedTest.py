import speedtest
s = speedtest.Speedtest()
print("Testing....")

down = s.download() / 1048576
up = s.upload() / 1048576
pingResult = round(s.results.ping)
print(f"Download Speed : {down : .2f} Mbps")
print(f"Up Speed       : {up : .2f} Mbps")