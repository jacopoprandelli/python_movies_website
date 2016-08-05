import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "Toy Story is a 1995 American computer-animated adventure buddy comedy film.",
			"https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

#print(toy_story.storyline)
avatar = media.Movie("Avatar",
                    "Avatar is a 2009 American epic science fiction film.",
                    "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",
                    "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

#print(avatar.storyline)
#avatar.show_trailer()
gotg = media.Movie("Guardians of the Galaxy",
                    "Guardians of the Galaxy is a 2014 American superhero film based on the Marvel Comics superhero team of the same name.",
                    "https://upload.wikimedia.org/wikipedia/en/thumb/8/8f/GOTG-poster.jpg/220px-GOTG-poster.jpg",
                    "https://www.youtube.com/watch?v=B16Bo47KS2g")
#gotg.show_trailer()

movies = [toy_story, avatar, gotg]
fresh_tomatoes.open_movies_page(movies)
