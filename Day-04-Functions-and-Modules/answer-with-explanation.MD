[Home](../README.md) | [Task >>](./assignment.MD)

# Day 4 Task: Functions and Modules

This task involves using functions to make the code more modular and reusable, and importing modules to add more functionality to the movie recommendation system.

## Step 1: Create a function to recommend movies based on genre

- Create a function called `recommend_movies` that takes a genre as an argument and recommends movies based on that genre:

  ```
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
  ```
  
 - This function takes a genre as an argument, recommends movies based on that genre, or displays a message if the genre is not recognized.

## Step 2: Use the function to recommend movies based on user input

- Replace the if, elif, and else statements in the while loop with a call to the `recommend_movies` function:

  ```
  another = input("Do you want another recommendation? (y/n) ")
  while another.lower() == "y":
      genre = input("What is your favorite movie genre? ")
      recommend_movies(genre)
      another = input("Do you want another recommendation? (y/n) ")
  ```
 
 ## Step 3: Create a module for the movie recommendation system
 
 - Create a module called `movie_recommendation_system.py` to contain the movie recommendation system code:
 
  ```
  # movie_recommendation_system.py

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
  ```
  
 - This code defines the `recommend_movies` function and creates lists of action, comedy, and drama movies.
 
 ## Step 4: Import the module and use the function in another file

- Create a new file called 'main.py' and import the 'movie_recommendation_system' module:

  ```
  # main.py

  import movie_recommendation_system

  another = input("Do you want another recommendation? (y/n) ")
  while another.lower() == "y":
      genre = input("What is your favorite movie genre? ")
      movie_recommendation_system.recommend_movies(genre)
      another = input("Do you want another recommendation? (y/n) ")
  ```
  
- This code imports the `movie_recommendation_system` module and uses the `recommend_movies` function to recommend movies based on user input.
- Running the `main.py` file will execute the movie recommendation system and allow the user to get recommendations based on their favorite genre.

That's it for the Day 4 task! By creating a function and module, we made the code more modular and reusable, and by importing the module, we added more functionality to the movie recommendation system.
