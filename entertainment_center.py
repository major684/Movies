# Movies Project
# Title:Entertainment Center
# Author:Lucas Velasquez

# Import files below
import fresh_tomatoes
import media


# Bring in a new instance of the movie class in the media file
toy_story = media.Movie(
    "Toy Story",
    "A story of a boy and his toys that come to life",
    "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",  # noqa
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")  # noqa

avatar = media.Movie(
    "Avatar",
    "A marine on an alien planet",
    "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",  # noqa
    "https://www.youtube.com/watch?v=a0CDJZu4M5I")  # noqa

big_hero_six = media.Movie(
    "Big Hero 6",
    "A gifted boy creates cool tech",
    "https://upload.wikimedia.org/wikipedia/en/thumb/4/4b/Big_Hero_6_%28film%29_poster.jpg/220px-Big_Hero_6_%28film%29_poster.jpg",  # noqa
    "https://www.youtube.com/watch?v=d2S8D_SCAJY")  # noqa

chef = media.Movie(
    "Chef",
    "A chef who loses his restaurant job starts up a food truck in \
    an effort to reclaim his creative promise, while piecing \
    back together his estranged family",
    "http://ia.media-imdb.com/images/M/MV5BMTY5NTYzNTA1M15BMl5BanBnXkFtZTgwODIwODU1MTE@._V1_SY317_CR1,0,214,317_AL_.jpg",  # noqa
    "https://www.youtube.com/watch?v=mJiN6a7K5fI")  # noqa

master_and_commander = media.Movie(
    "Master and Commander: The far Side of the World",
    "Captain Lucky Jack Aubrey of HMS Surprise has orders to \
    pursue the French privateer Acheron, and Sink, Burn, \
    or take her as a Prize",
    "https://upload.wikimedia.org/wikipedia/en/thumb/b/bf/Master_and_Commander-The_Far_Side_of_the_World_poster.png/220px-Master_and_Commander-The_Far_Side_of_the_World_poster.png",  # noqa
    "https://www.youtube.com/watch?v=C2YiRxujr_Q")  # noqa

million_dollar_arm = media.Movie(
    "Million Dollar Arm",
    "A sports agent stages an unconventional recruitment \
    strategy to get talented Indian cricket players to play \
    Major League Baseball",
    "https://upload.wikimedia.org/wikipedia/en/thumb/a/a8/Million_Dollar_Arm_poster.jpg/220px-Million_Dollar_Arm_poster.jpg",  # noqa
    "https://www.youtube.com/watch?v=lEtNIoPxcq8")  # noqa

# Put all objects in a list to pass to the fresh tomatoes method
movies = [toy_story, avatar, big_hero_six,
          chef, master_and_commander, million_dollar_arm
          ]

# use the method open_movies_page to generate the html
fresh_tomatoes.open_movies_page(movies)
