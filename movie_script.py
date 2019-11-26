import imdb
hr=imdb.IMDb()
movie_name=input('Enter the movie name : ')
print()
movies=hr.search_movie(str(movie_name))
index=movies[0].getID()
movie=hr.get_movie(index)
title=movie['title']
year=movie['year']
cast=movie['cast']
cast_list=','.join(map(str,cast))

#print(cast)

print('Title : ',title)
print('Year :',year)
print('Full Cast : ',cast_list)