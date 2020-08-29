import speedtest

obj = speedtest.Speedtest()

down = obj.download()//1024
up = obj.upload()//1024

print(f'Downloading speed {down}')
print(f'Uploading speed {up}')
