def recommend_movies(genre):
    if genre.lower() == "action":
        print("You might like these action movies:")
        for movie in action_movies:
            print("- " + movie)
    elif genre.lower() == "comedy":
        print("You might like these comedy movies:")
        for movie in comedy_movies:
            print("- " + movie)
    elif genre.lower() == "drama":
        print("You might like these drama movies:")
        for movie in drama_movies:
            print("- " + movie)
    else:
        print("Sorry, we don't have any recommendations for that genre.")

action_movies = ["Die Hard", "Terminator", "Lethal Weapon"]
comedy_movies = ["Airplane!", "The Hangover", "Bridesmaids"]
drama_movies = ["The Shawshank Redemption", "The Godfather", "Forrest Gump"]