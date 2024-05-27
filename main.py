from moviepy.editor import VideoFileClip
import os

from config import INPUT_PATH, OUTPUT_PATH

def get_filenames(path:str) -> list:
    filenames = []
    for filename in os.listdir(path):
        if os.path.isfile(os.path.join(path, filename)):
            filenames.append(filename)
    return filenames

def main() -> None:
    files = get_filenames(INPUT_PATH)
    for file in files:
        try:
            video_path = os.path.join(INPUT_PATH, file)
            video = VideoFileClip(video_path)
            audio_name, extension = os.path.splitext(file)
            audio_name += '.mp3'
            audio_path = os.path.join(OUTPUT_PATH, audio_name)
            audio = video.audio
            audio.write_audiofile(audio_path)
        except Exception as e:
            print(f'Erro: {file} -> {e}')

if __name__ == '__main__':
    main()
