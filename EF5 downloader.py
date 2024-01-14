from pytube import YouTube
import os
import yt_dlp
from datetime import timedelta
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System, Col

System.Clear()
System.Title("EF5 Downloader")
System.Size(70, 20)

banner = r"""
███████ ███████ ███████ 
██      ██      ██      
█████   █████   ███████ 
██      ██           ██ 
███████ ██      ███████  
"""[1:]


Anime.Fade(Center.Center(banner), Colors.rainbow, Colorate.Vertical, enter=True)




def download_video(url, save_path='./output', file_format='mp4'):
    try:
        audio_status = 'No'
        if not os.path.exists(save_path):
            os.makedirs(save_path)

        yt = YouTube(url)

        if file_format.lower() in ['mp4', 'webm']:
            if file_format.lower() == 'mp4':
                download_with_audio = Write.Input("Audio? - lower quality(yes/no): ", Colors.white_to_green, interval=0.005)

                if download_with_audio.lower() == 'yes':
                    selected_stream = yt.streams.get_highest_resolution()
                    audio_status = 'Yes'
                else:
                    video_streams = yt.streams.filter(file_extension=file_format).order_by('resolution').desc()
                    unique_qualities = set()

                    os.system("cls")
                    Write.Print(f'Title: {yt.title}\n', Colors.white_to_red, interval=0.005)
                    Write.Print(f'Format: {file_format}\n', Colors.white_to_red, interval=0.005)
                    Write.Print(f'Audio: No\n', Colors.white_to_red, interval=0.005)
                    Write.Print(f'Length: {str(timedelta(seconds=yt.length))}\n', Colors.white_to_red, interval=0.005)

                    for stream in video_streams:
                        if stream.resolution not in unique_qualities:
                            unique_qualities.add(stream.resolution)
                            print(f"{len(unique_qualities)}. {stream.resolution}")

                    selected_quality = int(Write.Input("Video Quality: ", Colors.white_to_green, interval=0.005)) - 1

                    if 0 <= selected_quality < len(video_streams):
                        selected_stream = next(stream for i, stream in enumerate(video_streams) if i == selected_quality)
                    else:
                        print("Invalid quality selection.")
                        return

                System.Title(f"EF5 Downloader ({yt.title})")
                os.system("cls")
                Write.Print(f'Title: {yt.title}\n', Colors.white_to_red, interval=0.005)
                Write.Print(f'Format: {file_format}\n', Colors.white_to_red, interval=0.005)
                Write.Print(f'Resolution: {selected_stream.resolution}\n', Colors.white_to_red, interval=0.005)
                Write.Print(f'Audio: {audio_status}\n', Colors.white_to_red, interval=0.005)
                Write.Print(f'Length: {str(timedelta(seconds=yt.length))}\n', Colors.white_to_red, interval=0.005)
                print()
                print(f"Downloading..")

                selected_stream.download(save_path)
                Write.Print('Saved --> output', Colors.white_to_green, interval=0.001)

            else:
                video_streams = yt.streams.filter(file_extension=file_format).order_by('resolution').desc()
                unique_qualities = set()

                os.system("cls")
                Write.Print(f'Title: {yt.title}\n', Colors.white_to_red, interval=0.005)
                Write.Print(f'Format: {file_format}\n', Colors.white_to_red, interval=0.005)
                Write.Print(f'Audio: {audio_status}\n', Colors.white_to_red, interval=0.005)
                Write.Print(f'Length: {str(timedelta(seconds=yt.length))}\n', Colors.white_to_red, interval=0.005)

                for stream in video_streams:
                    if stream.resolution not in unique_qualities:
                        unique_qualities.add(stream.resolution)
                        print(f"{len(unique_qualities)}. {stream.resolution}")

                selected_quality = int(Write.Input("Video Quality: ", Colors.white_to_green, interval=0.005)) - 1

                if 0 <= selected_quality < len(video_streams):
                    selected_stream = next(stream for i, stream in enumerate(video_streams) if i == selected_quality)
                else:
                    print("Invalid quality selection.")
                    return

                System.Title(f"EF5 Downloader ({yt.title})")
                os.system("cls")
                Write.Print(f'Title: {yt.title}\n', Colors.white_to_red, interval=0.005)
                Write.Print(f'Format: {file_format}\n', Colors.white_to_red, interval=0.005)
                Write.Print(f'Resolution: {selected_stream.resolution}\n', Colors.white_to_red, interval=0.005)
                Write.Print(f'Audio: {audio_status}\n', Colors.white_to_red, interval=0.005)
                Write.Print(f'Length: {str(timedelta(seconds=yt.length))}\n', Colors.white_to_red, interval=0.005)
                print()
                print(f"Downloading..")

                selected_stream.download(save_path)
                Write.Print('Saved --> output', Colors.white_to_green, interval=0.001)

        elif file_format.lower() == 'mp3':
            os.system("cls")
            Write.Print(f'Title: {yt.title}\n', Colors.white_to_red, interval=0.005)
            Write.Print(f'Format: {file_format}\n', Colors.white_to_red, interval=0.005)
            Write.Print(f'Audio: Yes\n', Colors.white_to_red, interval=0.005)
            Write.Print(f'Length: {str(timedelta(seconds=yt.length))}\n', Colors.white_to_red, interval=0.005)
            Write.Print(f'Note: Don\'t worry about ERROR\n', Colors.white_to_red, interval=0.005)
            download_audio_with_yt_dlp(url, save_path)

        else:
            print("Invalid file format. Supported formats are MP3, MP4, and WEBM.")

    except Exception as e:
        print(f"Error: {str(e)}")
def download_audio_with_yt_dlp(url, save_path='./output'):
    try:
        if not os.path.exists(save_path):
            os.makedirs(save_path)

        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(save_path, '%(title)s.mp3'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
            }],
            'quiet': True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)

            if 'mp3' in info.get('ext', ''):
                mp3_path = os.path.join(save_path, f"{info['title']}.mp3")
                System.Title(f"EF5 Downloader ({info['title']})")
                print(f"Downloading..")
                print(f"Saved --> {mp3_path}")
            else:
                print("Error: No MP3 audio stream available.")

    except yt_dlp.DownloadError as e:
        pass
    except Exception as e:
        pass

if __name__ == "__main__":
    youtube_url = Write.Input("URL: ", Colors.white_to_green, interval=0.005)
    file_format = Write.Input("MP3/MP4/WEBM: ", Colors.white_to_green, interval=0.005)
    save_path = './output'

    download_video(youtube_url, save_path, file_format)
#by .ef5
#discord: .ef5
#github.com/venuzik