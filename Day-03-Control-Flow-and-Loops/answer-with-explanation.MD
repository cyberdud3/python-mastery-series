[Home](../README.md) | [Task >>](./assignment.MD)

# Day 3 Task: Control Flow and Loops

This task involves using control flow statements such as if, elif, and else, and loops such as for and while to make the movie recommendation system more interactive and dynamic.

## Step 1: Create a variable to store the user's favorite movie genre

- Add the following code to the `movie_recommendation.py` file to ask the user for their favorite movie genre:
    ```
    genre = input("What is your favorite movie genre? ")
    ```

## Step 2: Use if, elif, and else statements to recommend movies based on the user's favorite genre

- Use if, elif, and else statements to recommend movies based on the user's favorite genre:
    ```
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
 - This code will recommend movies based on the user's favorite genre, or display a message if the genre is not recognized

## Step 3: Use a while loop to ask the user for another recommendation

- Use a while loop to ask the user if they want another recommendation, and exit the loop if they say no:
    ```
    another = input("Do you want another recommendation? (y/n) ")
    while another.lower() == "y":
        genre = input("What is your favorite movie genre? ")
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
        another = input("Do you want another recommendation? (y/n) ")
    ```
- This code will continue asking the user for recommendations until they say no

If everything is set up correctly, you should see personalized movie recommendations and be able to request additional recommendations.

### This marks the completion of Day 3 task.
