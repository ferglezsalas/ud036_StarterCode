import webbrowser

class Movie():
	"""The class Movie is designed to store information about movies"""

	def __init__(self, movie_title, movie_storyline, poster_image_url, trailer_youtube_url):
		"""Creates a new instance of the class. 
			Every parameter must be a string and none of them are optional"""
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube_url

	def show_trailer(self):
		"""Opens a browser and displays the movie's youtube trailer"""
		webbrowser.open(self.youtube_trailer_url)