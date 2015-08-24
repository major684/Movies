#Movies Project
#Title:Classes
#Author: Lucas Velasquez

#Import the webbrowser for the show_trailer function
import webbrowser

#Create a class Movie 
class Movie():
    #Initialize an instance of the class and give it properties or arguements
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        #Self refers to the instance when the class is invoked
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    #Creates a new function called show_trailer where we open a web browser to show the
    #Trailer of the movie.
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
