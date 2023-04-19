import m3u8_To_MP4  # m3u8 변환
import os  # 동영상 저장, 이름짓기
import os.path

if __name__ == '__main__':
    print('m3u8download try...')
    m3u8_To_MP4.multithread_download('https://fcbjngaswqol4996171.cdn.ntruss.com/hls/66b40105-f197-4353-bf15-1abc42095695/mp4/66b40105-f197-4353-bf15-1abc42095695.mp4/index.m3u8')