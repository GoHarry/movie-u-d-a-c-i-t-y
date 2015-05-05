import fresh_tomatoes

#This class creates a Movie instance and provides a way to save Movie information.

class Movie():
	
	def __init__(self, title, poster_image, trailer_url):
		self.title=title
		self.poster_image_url=poster_image
		self.trailer_youtube_url=trailer_url

#Below are the instances of class Movie. Each instance refers to a different movie. The instances of class contain their titles, 
# links to their image posters and their trailer youtube links.

sholay = Movie("Sholay", "http://indiaopines.com/wp-content/uploads/2013/11/Sholay-poster.jpg", "https://www.youtube.com/watch?v=36SMdfwisLg")
ddlj   = Movie("Dilwale Dulhaniya Le Jaayenge","http://www.du360.in/wp-content/uploads/2014/12/Dilwale-Dulhania-Le-Jayenge-poster.jpg",
	"https://www.youtube.com/watch?v=RCS5NlDIqME")
titanic = Movie("Titanic",
	"http://www.movie-poster-artwork-finder.com/posters/titanic-poster-artwork-leonardo-dicaprio-kate-winslet-billy-zane-small.jpg",
	"https://www.youtube.com/watch?v=Jkjrh4EWW4E")
spiderman = Movie("The Amazing Spider-Man 2","https://pmcdeadline2.files.wordpress.com/2014/06/amazing-spider-man-2-poster__140603232341.jpg",
	"https://www.youtube.com/watch?v=DlM2CWNTQ84")
ironman = Movie("Iron Man 3","http://www.impawards.com/2013/posters/iron_man_three_ver11.jpg","https://www.youtube.com/watch?v=Ke1Y3P9D0Bc")
avengers = Movie("Avengers","http://www.theaterhopper.com/wordpress/wp-content/uploads/2012/02/avengers_poster.jpg","https://www.youtube.com/watch?v=eOrNdBpGMv8")
babysdayout = Movie("Baby's Day Out (1994)","http://ia.media-imdb.com/images/M/MV5BMjE1NTU3OTAyM15BMl5BanBnXkFtZTcwNDg0NDMyMQ@@._V1_SX640_SY720_.jpg",
	"https://www.youtube.com/watch?v=AYkvarLxatM")
skyfall = Movie("Skyfall","http://t2.gstatic.com/images?q=tbn:ANd9GcTSNSk0M1z_CZ1UKTnfE2nHmk4Oxqh_gKO0dAHZHwrfLX6D9Y4s",
	"https://www.youtube.com/watch?v=A82nMyFLdtQ")
lifeofpi = Movie("Life of Pi","http://www.impawards.com/2012/posters/life_of_pi.jpg","https://www.youtube.com/watch?v=j9Hjrs6WQ8M")


#This list stores information of all movies

movies = [sholay, ddlj, titanic, spiderman, ironman, avengers, babysdayout, skyfall, lifeofpi]

# The movies list is passed as an argument to open movies page method

fresh_tomatoes.open_movies_page(movies)
