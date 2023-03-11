import movie_recommendation_system

another = input("Do you want another recommendation? (y/n) ")
while another.lower() == "y":
    genre = input("What is your favorite movie genre? ")
    movie_recommendation_system.recommend_movies(genre)
    another = input("Do you want another recommendation? (y/n) ")