class Song:
    
    count= 0
    genres=[]
    artists=[]
    genre_count={}
    artist_count={}
    
    def __init__(self,name, artist, genre):
        self.name=name
        self.artist=artist
        self.genre=genre
        Song.add_song_to_count()
        Song.add_to_genre(genre)
        Song.add_to_artist(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)
        
    @classmethod
    def add_song_to_count(cls,increment=1):
        cls.count += increment
        
    @classmethod
    def add_to_genre(cls,genre):
        if genre not in Song.genres:
         Song.genres.append(genre)
        
    @classmethod
    def add_to_artist(cls,artist):
        if artist not in Song.artists:
         Song.artists.append(artist)
    
    @classmethod
    def add_to_genre_count(cls,genre):
        if genre in Song.genre_count:
            Song.genre_count[genre] += 1
        else:
            Song.genre_count[genre] = 1
            
    @classmethod
    def add_to_artist_count(cls,artist):
        if artist in Song.artist_count:
            Song.artist_count[artist] +=1
        else:
            Song.artist_count[artist] =1
        
     
song1 = Song("Song 1", "Artist A", "Rap")
song2 = Song("Song 2", "Artist B", "Rap")
song3 = Song("Song 3", "Artist C", "Rock")
song4 = Song("Song 4", "Artist D", "Country")
song5 = Song("Song 5", "Artist E", "Country")
song6 = Song("Song 6", "Artist F", "Country")

print(Song.artist_count)
     
     
        
    
