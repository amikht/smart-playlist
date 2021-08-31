import server.api.psql_util as psql


def fetch_library(token): # Spotify
    """
    Takes in an OAuth2 token resulting from a Spotify authentication
    and uses that token to fetch and digest a user's library into the
    database.
    """


def fetch_song(song_name, song_artist=""): # RYM
    """
    Fetches a song with a given name from the Rate Your Music database
    and uses that information to assign the appropriate genre information
    to the song.

    NOTE ABOUT THIS FUNCTION:
    RYM will ban my IP if I try to automatically do this for every single
    song in my library. For this reason, it will be best to delay getting
    genre information for a song until the moment it is appearing on the
    screen for the user to tag and categorize.

    song_name -> Song to find
    song_artist -> Name of the song's artist to resolve any discrepencies
                   with songs with the same name, optional.
    """
    pass


def get_song_by_id(song_id):
    """
    Returns all database information about a given song ID excluding the ID
    and with all foreign keys translated into their human-readable text version.
    """
    pass


def get_songs_by_ids(song_ids):
    """
    Identical functionality to get_song_by_id, but a list of IDs is provided and
    a 2-dimensional list of song contents is returned, processing each ID into
    song metadata.
    """
    pass


def get_songs_by_name(song_name, song_artist_name=""):
    """
    Gets all songs with titles that match the provided name. If an artist
    is provided, one song - the first match - is returned.
    """
    pass


def get_songs_by_artist(artist_id):
    """
    Returns all songs that were written by the given artist. Returns a list
    of song IDs.
    """
    pass


def get_artist_by_name(artist_name):
    """
    Returns the integer ID of an artist given their name

    NOTE this database assumes that artist names are unique.
    """
    pass


def get_tags(song_id):
    """
    Returns all the tags associated with a given song as a list of strings
    """
    pass


def drop_artist(artist_id):
    """
    Drops an artist, along with all of their albums and songs, from the
    database. Because all songs and albums by an artist are connected to
    the artist behind the scenes, dropping an artists requires the dropping
    of all that data also. 
    """