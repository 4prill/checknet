import time
import speedtest

def check_speed():
    st = speedtest.Speedtest()
    st.get_best_server()

    download_speed = st.download() / 1_000_000  
    upload_speed = st.upload() / 1_000_000  
    ping = st.results.ping

    return download_speed, upload_speed, ping

def write_to_file(file_path, data):
    with open(file_path, 'a') as f:
        f.write(data + '\n')

def main():
    file_path = 'speed_log.txt'

    try:
        while True:
            download_speed, upload_speed, ping = check_speed()
            timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
            result_str = f'{timestamp}, Download: {download_speed:.2f} Mbps, Upload: {upload_speed:.2f} Mbps, Ping: {ping} ms'
            print(result_str)
            write_to_file(file_path, result_str)
            time.sleep(60)  # Wait for 1 minute before checking again

    except KeyboardInterrupt:
        print("Speed test stopped.")
        pass

if __name__ == "__main__":
    main()
