# Required Modules Importing
from yt_dlp import YoutubeDL
import os


def format_choice():
    user_choice = input("Enter 'v' for video only, 'a' for audio only, or 'b' for both (default: b): ") or 'b'
    
    if user_choice == 'v':
        return 'bestvideo[ext=mp4]'
    elif user_choice == 'a':
        return 'bestaudio/best'
        
    return 'bestvideo[ext=mp4]+bestaudio[m4a]/best'


def downloadVideo():
    try:
        print('*'*50)
        print("Welcome to Youtube Video Downloader")
        print('*'*50)
        
        playlist_url = input("\nEnter the Youtube Video Url: ")
        
        print("Now Enter your directory path in which you wants to save your downloaded files.\n")
        
        output_path = input("Enter Directory Name (default: downloads): ") or 'downloads/'
        
        # if not os.path.isdir(output_path):
        #     print("Invalid directory entered. Using default 'downloads/' directory.")
        #     output_path = 'downloads/'
            
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        
        print("Video Downloading Process Starts...\n")
        ydl_options = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best',
            'quiet': True,
            'noplaylist': True,
            'download_archive': 'archive.txt',
            'outtmpl': os.path.join(output_path, '%(resolution)s - %(title)s.%(ext)s'),
            'merge_output_format': 'mp4',
            'postprocessors': [
                {
                    'key': 'EmbedThumbnail',
                    'already_have_thumbnail': True
                },
            ]
        }
        with YoutubeDL(ydl_options) as ydl:
            ydl.download(playlist_url)
            print("Video Successfully Downloaded...\n")
            return
    except Exception as e:
        print("Video Download Failed due to an Error !")
        print(f"Error : {e}")

# This is a Youtube Playlist Downloader
def progress_hook(download):
    if download['status'] == 'downloading':
        print(f"Downloading: {download['filename'][:30]} at {download['_percent_str']} {download['_eta_str']}")

def downloadPlaylist():
    try:
        print('*'*50)
        print("Welcome to Youtube Playlist Downloader")
        print('*'*50)
        
        playlist_url = input("\nEnter the Youtube Playlist Url: ")
        
        print("Now Enter your directory path in which you wants to save your downloaded files.\n")
        
        output_path = input("Enter Directory Name (default: downloads): ") or 'downloads/'
        
        if not os.path.isdir(output_path):
            print("Invalid directory entered. Using default 'downloads/' directory.")
            output_path = 'downloads/'
            
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        
        ydl_options = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best',
        'quiet': True,
        'outtmpl': os.path.join(output_path, '%(playlist_title)s/%(playlist_index)s - %(resolution)s %(title)s.%(ext)s'),
        'nooverwrites': True,
        'download_archive': 'archive.txt',
        'ignoreerrors': True,
        'retries': 3,
        # 'progress_hooks': [progress_hook],
        'merge_output_format': 'mp4',
        'postprocessors': [
            {
                'key': 'EmbedThumbnail',
                'already_have_thumbnail': False
            },
        ],
        }
    
        # Download Now
        print('Download Process Starts...\n')
        with YoutubeDL(ydl_options) as ydl:
            ydl.download([playlist_url])
            print('Playlist Successfully Downloaded....\n')
    except Exception as e:
        print('Download Operation Failed Due to Some Errors\n')
        print(f'Error: {e}')
        




def main():
    print('Welcome to Our App\n')
    print('What would you like to Use:')
    print('Enter 1: Youtube Single Video Downloader')
    print('Enter 1: Youtube Complete Playlist Downloader')
    user_choice = int(input("Enter your Choice '1' or '2' (default: '1'): ")) or 1
    
    if user_choice == 1:
        # For Single Video Download
        downloadVideo()
    elif user_choice == 2:
        # For Playlist Video Download
        downloadPlaylist()
    else:
        # For Single Video Download
        downloadVideo()
    
    print("App Closed\n")
    return


if __name__ == '__main__':
    main()