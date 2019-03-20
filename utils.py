# 数据集制作
# 2018/12/18

import glob
import cv2


def resize_img(img_dir, save_dir):
    # 批量修改图片大小
    resize_factor = (224, 224)
    img_paths = glob.glob(img_dir)
    for img_path in img_paths:
        img_name = img_path.split('\\')[-1]
        img = cv2.imread(img_path)
        resized_img = cv2.resize(img, resize_factor)
        save_name = save_dir + img_name
        cv2.imwrite(save_name, resized_img)


def clip_video(video_path, output_size, output_dir, fps, video_count):
    # 截取某一目录下所有视频，按照ucf1的命名标准进行重命名
    video_cls = video_path.split('\\')[-1].split('_')[0]
    videoCapture = cv2.VideoCapture(video_path)
    total_frame = videoCapture.get(7)
    is_open, frame = videoCapture.read()
    if not is_open:
        raise RuntimeError('Can not find any .avi format video, please set correct video file path.')
    if total_frame <201:
        raise RuntimeError('video {} is too short, please remove this file from the directory'.format(video_path))
    frame_count = 1
    clip_count = 1
    # windows仅在使用MJPG的编码格式时，视频才能正常保存，使用XVID编码格式保存的视频无法打开，原因不明，linux下未验证
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    video_name = output_dir + '\\' + '{}_g{}_c{}.avi'.format(video_cls, str(video_count).zfill(3),
                                                         str(clip_count).zfill(4))
    videoWriter = cv2.VideoWriter(video_name, fourcc, fps, output_size)
    # 基于ucf-101的数据集格式保存视频，每200帧保存为一个视频，fps为25，视频大小为320x240，视频总长度或剩余长度不足100帧的直接丢弃
    while is_open:
        # 每隔200帧重新保存一个视频
        if frame_count % 200 == 0 and (total_frame - frame_count > 100):
            # 打印上一个写完的视频
            print('{} has been written to path:{}'.format(video_name, output_dir))
            clip_count += 1
            video_name = output_dir + '\\' + '{}_g{}_c{}.avi'.format(video_cls, str(video_count).zfill(3),
                                                                     str(clip_count).zfill(4))
            videoWriter = cv2.VideoWriter(video_name, fourcc, fps, output_size)
        # 不事先resize 保存的视频无法打开，原因不明
        new_frame = cv2.resize(frame, output_size)
        videoWriter.write(new_frame)
        is_open, frame = videoCapture.read()
        frame_count += 1
    cv2.destroyAllWindows()
    videoCapture.release()



def scan_video(video_dir):
    # 打印出每个视频的总帧数
    video_list = glob.glob(video_dir)
    for video_path in video_list:
        video = cv2.VideoCapture(video_path)
        if video.get(7) != 200:
            print(video_path.split('\\')[-1], video.get(7))
    return


def main():
    need_resize = False
    if need_resize:
        img_dir = 'E:\\flp\data_three_cls\\video\\news\\*.jpg'
        save_dir = 'E:\\flp\data_three_cls\\video_resize\\news\\'
        resize_img(img_dir, save_dir)

    need_clip_video = False
    if need_clip_video:
        clip_size = (320, 240)
        fps = 25
        video_dir = 'E:\GE\\flp\\video_2\\news\\*.avi'
        output_dir = 'E:\\GE\\flp\\output\\news\\'
        video_files = glob.glob(video_dir)
        for video_count, video_file in enumerate(video_files):
            clip_video(video_file, clip_size, output_dir, fps, video_count+15)

    need_scan_video = True
    if need_scan_video:
        video_dir = 'E:\\GE\\flp\output\\news\\*.avi'
        scan_video(video_dir)
if __name__ == '__main__':
    main()