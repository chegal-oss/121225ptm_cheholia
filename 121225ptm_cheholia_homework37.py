print("\nPython Fundamentals 2025: Домашнее задание 37")
print("\n1. Воспроизведение мультимедиа")


class AudioFileMixin:
    def play_audio(self):
        if not hasattr(self, "audio_tracks"):
            raise AttributeError("Need audio_tracks attr")
        print(f"Воспроизведение аудио для {self.__class__.__name__}")
        for track in getattr(self, "audio_tracks"):
            print(track)
        return self


class VideoFileMixin:
    def play_video(self):
        if not hasattr(self, "video_files"):
            raise AttributeError("Need video_files attr")
        print(f"Воспроизведение видео для {self.__class__.__name__}")
        for video in getattr(self, "video_files"):
            print(video)
        return self


class MediaPlayer(AudioFileMixin):
    def __init__(self, audio_tracks):
        self.audio_tracks = audio_tracks


class Laptop(AudioFileMixin, VideoFileMixin):
    def __init__(self, video_files, audio_files):
        self.video_files = video_files
        self.audio_tracks = audio_files


tracks = ["track1.mp3", "track3.mp3"]
movies = ["movie.mp4", "trailer.mov"]

MediaPlayer(tracks).play_audio()
Laptop(movies, tracks).play_audio().play_video()
