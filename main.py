from pytube import YouTube

path_to_download_directory = "C:/Users/u/Documents/Youtube_MP4"


def download(url: str) -> None:
    youtube_object = YouTube(url)
    youtube_object = youtube_object.streams.get_highest_resolution()

    try:
        youtube_object.download(path_to_download_directory)
        print("Download is completed successfully")
    except Exception as error:
        print(f"An error has occurred: {error}")


if __name__ == "__main__":
    flag: str = "y"
    flag_choice = ["y", "n"]
    while flag == "y":
        link = input("Enter the YouTube video URL: ")
        download(link)
        flag = input("Do you want to download another YouTube video ? [y/n]: ")
        while flag not in flag_choice:
            flag = input("Please choose between 'y' for yes or 'n' for no: ")

    print("Thanks for using our services")
