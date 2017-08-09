import media
import fresh_tomatoes


# Movies that are going to be in the website.
deadpool = media.Movie("Deadpool",
                       """The story of a man trying to get the
                       girl of his dreams back.""",
                       "https://pbs.twimg.com/media/Cx5hnQMXUAA_YSX.jpg",
                       "https://www.youtube.com/watch?v=Xithigfg7dA")
spiderman = media.Movie("Spider-Man: Homecoming",
                        """A boy faces the strggules
                        of growing up with superpowers""",
                        "http://blogdesuperheroes.es/wp-content/plugins/BdSGallery/BdSGaleria/54586.jpg",
                        "https://www.youtube.com/watch?v=39udgGPyYMg")
batman = media.Movie("The Dark Night", "Nana nana nana nana Batman!",
                     "https://pics.filmaffinity.com/the_dark_knight-102763119-large.jpg",
                     "https://www.youtube.com/watch?v=EXeTwQWrcwY")
inception = media.Movie("Inception", """A thief, who steals corporate secrets
                        through use of dream-sharing technology,
                        is given the inverse task of planting
                        an idea into the mind of a CEO.""",
                        "http://4.bp.blogspot.com/_BgiiIgUM9wY/TR4J66q0JRI/AAAAAAAAAb8/F_6vGdol_rg/s1600/inception-origen.jpg",
                        "https://www.youtube.com/watch?v=YoHD9XEInc0")
madmax = media.Movie("Mad Max: Fury Road",
                     """Mad Max joins a group of women
                     scaping from Immortan Joe""",
                     "http://www.madmaxmovies.com/mad-max-fury-road/soundtrack/mad-max-fury-road-soundtrack.jpg",
                     "https://www.youtube.com/watch?v=hEJnMQG9ev8")
get_out = media.Movie("Get Out", """A young African American man visits his
                       Caucasian girlfriend's cursed family estate""",
                      "https://pbs.twimg.com/media/C_4bkYfXgAEwfFA.jpg",
                      "https://www.youtube.com/watch?v=A2JbO9lnVLE")

# Add them into a list
movies = [deadpool, spiderman, batman, inception, madmax, get_out]


# Create and open the movies page
fresh_tomatoes.open_movies_page(movies)
