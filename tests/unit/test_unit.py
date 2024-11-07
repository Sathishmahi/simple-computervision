from simple_computervision import track_detect_video
import pytest
import cv2
import glob,os
import uuid


@pytest.mark.parametrize("video_file_name",[glob.glob(r"sample_videos/*.mp4")[0]])
def test_track_and_detect_video(video_file_name):
    out_file_name = f"out_{uuid.uuid1()}.mp4"
    track_detect_video(video_file_name,out_dir_name="test_out",out_filename=out_file_name)
    
    video_file_path = os.path.join("test_out",out_file_name)

    assert cv2.VideoCapture(video_file_path).isOpened()



failed_videos = ["demo.mp4"]
@pytest.mark.parametrize("video_file_name",failed_videos)
def test_track_and_detect_fail(video_file_name):
    with pytest.raises(FileNotFoundError):
        track_detect_video(video_file_name)

