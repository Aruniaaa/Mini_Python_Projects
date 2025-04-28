import numpy as np

action_like = int(input("On a scale of 10, how much do you like action? "))
romance_like = int(input("On a scale of 10, how much do you like romance? "))
category = input("""Are you in the mood for hollywood, bollywood, or mixed?
H - Hollywood
B - Bollywood
M - Mixed
Your answer --> """).lower()

def recommend_movies(action_like, romance_like, movies_dict):
    user = np.array([action_like, romance_like])
    
    dot_products = []
    movie_vectors = movies_dict.keys()
    new_movie_vectors = []
    dic = {}

    for i in movie_vectors:
        i = np.array(i)
        new_movie_vectors.append(i)
        dot_product = np.dot(i, user)
        dot_products.append(dot_product)


    for index in range(len(dot_products)):
     dic[dot_products[index]] = new_movie_vectors[index]



    sorted_dic = (sorted(dic.keys()))
    item = sorted_dic[-1]
    movie = dic.get(item)
    movie = tuple(movie)
    item2 = sorted_dic[-2]
    movie2 = dic.get(item2)
    movie2 = tuple(movie2)
    item3 = sorted_dic[-3]
    movie3 = dic.get(item3)
    movie3 = tuple(movie3)


    print(f"""Film recommendations based on your choices:
1. {movies_dict.get(movie)}
2. {movies_dict.get(movie2)}
3. {movies_dict.get(movie3)}
Enjoy watching!🍿💗""")



if category == 'h':
    from movies import hollywood_movies
    recommend_movies(action_like, romance_like, hollywood_movies)
elif category == 'b':
    from movies import bollywood_movies
    recommend_movies(action_like, romance_like, bollywood_movies)
elif category == 'm':
    from movies import mixed_movies
    recommend_movies(action_like, romance_like, mixed_movies)
else:
    print("Please enter a valid category and try again!")
