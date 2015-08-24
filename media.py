# Movies Project
# Title:Classes
# Author: Lucas Velasquez

# Import the webbrowser for the show_trailer function
import webbrowser

# Create a class Movie


class Movie():
    """
    Movie class that stores important information about a movie and
    has a method to show the trailer of the movie.
    """
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        # Self refers to the instance when the class is invoked
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

        def show_trailer(self):
            webbrowser.open(self.trailer_youtube_url)
