### 1. Introduction to Variables and Strings
print("\n"+"#"*30 + "String demonstration" + "#"*30)
# Introduce a variable storing Taylor Swift's name
artist_name = "Taylor Swift"
print(artist_name)

# A string literal representing one of her album titles
album_title = "Folklore"
print("One of " + artist_name + "'s albums is called " + album_title + ".")


### 2. Working with Numbers (Integers and Floats)
print("\n"+"#"*30 + "Integer demonstration" + "#"*30)
# Year Taylor Swift was born
year_of_birth = 1989
print("Taylor Swift was born in", year_of_birth)

print("\n"+"#"*30 + "Float demonstration" + "#"*30)
# The length of one of her songs in minutes (floating point number)
song_length = 3.45  # Length of "Cardigan" in minutes
print("The song 'Cardigan' is", song_length, "minutes long.")


### 3. Boolean Values
print("\n"+"#"*30 + "Boolean demonstration" + "#"*30)
# A boolean value representing whether Taylor Swift is a singer
is_singer = True
print("Is Taylor Swift a singer?", is_singer)

# Another boolean representing whether she has won a Grammy
has_won_grammy = True
print("Has Taylor Swift won a Grammy?", has_won_grammy)

### 4. Containers
#### 4.1. Lists
print("\n"+"#"*30 + "List demonstration" + "#"*30)
# List of Taylor Swift's genres
genres = ["Pop", "Country", "Indie Folk"]
print("Taylor Swift has performed in these genres:", genres)

# Adding a new genre
genres.append("Electropop")
print("Updated genres:", genres)


#### 4.2. Tuples
print("\n"+"#"*30 + "Tuple demonstration" + "#"*30)
# A tuple storing the names of Taylor Swift's first three albums
first_three_albums = ("Taylor Swift", "Fearless", "Speak Now")
print("Taylor Swift's first three albums are:", first_three_albums)

# Accessing elements in a tuple
print("Her second album is:", first_three_albums[1])


#### 4.3 Sets
print("\n"+"#"*30 + "Set demonstration" + "#"*30)
# A set of genres Taylor Swift has explored
genres = {"Pop", "Country", "Indie Folk", "Country", "Pop"}
print("Unique genres Taylor Swift has explored:", genres)

# Adding a new genre to the set
genres.add("Electropop")
print("Updated genres with Electropop added:", genres)

#### 4.4. Dictionaries
print("\n"+"#"*30 + "Dictionary demonstration" + "#"*30)
# Dictionary storing Taylor Swift's album release years
album_release_years = {
    "Fearless": 2008,
    "1989": 2014,
    "Lover": 2019,
    "Folklore": 2020,
}

print("The album 'Folklore' was released in", album_release_years["Folklore"])