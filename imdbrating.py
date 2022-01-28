import imdb
moviesDB = imdb.IMDb()
moviename =input("Enter movie name: ")
movies = moviesDB.search_movie(moviename)

id = movies[0].getID()
movie = moviesDB.get_movie(id)

title = movie['title']
rating = movie['rating']

print('Movie:')
print(f'Name of the movie:{title}')
print(f'rating: {rating}')
