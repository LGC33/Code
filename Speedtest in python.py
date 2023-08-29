import speedtest

speed_is = speedtest.Speedtest()

def bytes_to_mb(bytes):
    KB = 1024
    MB = KB *1024
    return int(bytes/MB)

download_speed = bytes_to_mb(speed_is.download())
print("Your Download speed is", download_speed, "MB")