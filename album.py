BigDict = {}

def wannaQuit(user_input):
    if user_input.lower() == 'q':
        print("Quitting the program.")
        print("BigDict content:", BigDict)
        exit()

def album(artist_name, album_title, number_of_songs):
    if artist_name not in BigDict:
        BigDict[artist_name] = []
    BigDict[artist_name].append({
        'Album Title': album_title,
        'Number of Songs': number_of_songs
    })

while True:
    print("Any time you wanna quit enter 'q'")
    artist_name = input("Enter artist's name: ")
    wannaQuit(artist_name)
    
    album_title = input("Enter album title: ")
    wannaQuit(album_title)
    
    songs = input("Enter the number of songs in the album: ")
    wannaQuit(songs)
    
    album(artist_name, album_title, songs)


print(BigDict)