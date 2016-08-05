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

sing_street = media.Movie("Sing Street",
                    "Sing Street is a 2016 Irish musical comedy-drama film written, produced, and directed by John Carney.",
                    "https://upload.wikimedia.org/wikipedia/en/2/2c/Sing_Street_poster.jpeg",
                    "https://www.youtube.com/watch?v=jYk2Vx1z6lk")

spectre = media.Movie("Spectre",
                    "Spectre (2015) is the twenty-fourth James Bond film produced by Eon Productions.",
                    "https://upload.wikimedia.org/wikipedia/en/thumb/c/c3/Spectre_poster.jpg/220px-Spectre_poster.jpg",
                    "https://www.youtube.com/watch?v=LTDaET-JweU")

a_beautiful_mind = media.Movie("A Beautiful Mind",
                    "A Beautiful Mind is a 2001 American biographical drama film based on the life of John Nash, a Nobel Laureate in Economics.",
                    "https://upload.wikimedia.org/wikipedia/en/thumb/b/b8/A_Beautiful_Mind_Poster.jpg/220px-A_Beautiful_Mind_Poster.jpg",
                    "https://www.youtube.com/watch?v=aS_d0Ayjw4o")
#gotg.show_trailer()

movies = [toy_story, avatar, gotg, sing_street, spectre, a_beautiful_mind]
fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
##print(media.Movie.__doc__)
##print("the name of my class is: " + media.Movie.__name__)
##print("the name of my module is: " + media.Movie.__module__)
