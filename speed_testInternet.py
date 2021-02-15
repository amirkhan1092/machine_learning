import speedtest

obj = speedtest.Speedtest()

down = obj.download()
up = obj.upload()

print(f'Downloading speed {down//1000000} mbps')
print(f'Uploading speed {up//1000000} mbps')
