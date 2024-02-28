def print_header(title):
    print()
    print(title.center(80, "#"))
    #print("\n"+"#"*30+" " + f"{title}" +" "+ "#"*30)


### 1. Introduction to Variables and Strings

# Introduce a variable storing Taylor Swift's name
print_header("String demonstration")
artist_name = "Taylor Swift"
print(artist_name)

# A string literal representing one of her album titles
album_title = "Folklore"
print("One of " + artist_name + "'s albums is called " + album_title + ".")
album_message = "One of " + artist_name + "'s albums is called " + album_title + "."
print(album_message)

album_message2 = f"One of {artist_name}'s albums is called {album_title}."
print(album_message2)
print(album_message2.upper())
print(album_message2.capitalize())
print(album_message2.partition("albums"))


### 2. Working with Numbers (Integers and Floats)
print_header("Integer demonstration")
year_of_birth = 1990
current_year = 2024

age = current_year - year_of_birth
voting_since = year_of_birth + 18 #Legal age for voting and (alcohol purchase) in Czechia
leap_years_experienced = (age-18)//4


print(f"I am now {age}, and since I could vote, I have experienced {leap_years_experienced} leap years")
print(f"I was using {type(age)}, to represent the numbers.")

print_header("Float demonstration")
# The length of one of her songs in minutes (floating point number)
song_length = 3.45  # Length of "Cardigan" in minutes
leap_years_experienced = (age-18)/4
print(f"Had I used simple division, answer would be {leap_years_experienced}")
print(f"This number would be of type {type(leap_years_experienced)}")

infinity = float("inf")
large_number = 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
print("Is infinity larger than large number?",infinity>large_number)


### 4. Sequences
#### 4.1. Lists
print_header("List demonstration")
# List of some programming languages
langs = ["Python", "C++", "Rust", "C", "FizzBuzz", "R", "mathscript"]
print("These are programming languages listed:", langs)

# Adding a new language
langs.append("C#")
print("Updated langueages:", langs)

# Removing a language
langs.remove("C")
print("Updated langueages:", langs)

#indexing example: 
print(f"printing nth (0) element: {langs[0]}")
print(type(langs[0]))

# Slicing examples
print(f"printing nth to mth [1:4]  element: {langs[1:4]}")
print(f"printing fist to mth [:4]  element: {langs[:4]}")
print(f"printing nth to end [4:] element: {langs[4:]}")
print(f"printing nth to 2nd to end [2:-2] element: {langs[2:-2]}")

# +operator 
print(f"Using + to concatenate {[langs[0]]+langs[:2]+langs[5:]}")


#### 4.2 Tuples
print_header("Tuple demonstration")
# A tuple storing information about me
about_me = ("Michal", 42, True)
print(f"Name: {about_me[0]}, Favorite Number: {about_me[1]}, plays DnD: {about_me[2]} ")

#### 4.3 Ranges
start = 1
stop = 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999
step = 3
my_range = range(start, stop, step)

print(f"2nd element in range is {my_range[888888888888888888888888]}")
#print([ele for ele in my_range])

#### 4.3 Sets
print_header("Set demonstration")
# Subset of pokemons
pokemons = {"Bulbasaur", "Charmander", "Squirtle", "Charmander"}
print("Unique starting pokemons:", pokemons)
pokemons.add("Pikachu")
print("Updated starting pokemons after adding Pikachu:", pokemons)
pokemons.add("Charmander")
print("Updated starting pokemons after adding Charmander:", pokemons)
pokemons.add("Saitama")
print("Updated starting pokemons after adding Saitama:", pokemons)
pokemons.remove("Saitama")
print("Updated starting pokemons after removing Saitama:", pokemons)

official_starting_pokemons= frozenset({"Bulbasaur", "Charmander", "Squirtle", "Charmander"})

imutable_tuple = (1, "john", True, pokemons)
print(imutable_tuple)



#### 4.4. Mapping types
print_header("Dictionary demonstration")
# Dictionary storing Taylor Swift's album release years
favorite_things = {
    "Movie": "Wag the dog",
    "TV series": "Scrubs",
    "Number": 42,
    "Song": "What I've done",
    "Shoes": False
}
print(f"My favorite things: {favorite_things}")
print(f"My favorite movie: {favorite_things["Movie"]}")
favorite_things["Movie"] = "Avengers: Infinity War"
print(f"After changing my favorite movie: {favorite_things["Movie"]}")
favorite_things["Language"] = "Chinese"
print(f"After adding my favorite language: {favorite_things}")


### 5. Boolean Values and NoneType
print_header("Boolean demonstration")
# A boolean value representing facts about TS
am_I_always_lying = True
is_that_paradox = False

#answer = input("So am I lying or not?: ")
#print(type(answer))


### 6. Special operators
list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 4, 5]
list3 = list1
list4 = list1[:]

print(f"is list1 list 2", list1 is list2)
print(f"is list1 list 3", list1 is list3)
print(f"is list1 list 4", list1 is list4)

### 7. Flow controll
### 7.1 Flow controll if else elif
list = [1,32,68]
if 68 in list:
    print("there is 68 in list")
elif 32 in list:
    print("there is 32 in list")
else:
    print("Neither 32 or 68 are in the list")


### 7.2 Flow controll for cycle
for pokemon in pokemons:
    print(pokemon)

for val in range(5):
    print(val)

print()
### 7.2 Flow controll while cycle
idx = 0
while(idx<10):
    print(f"{idx}- Still cycling")
    idx+=1

### 8 Functions
def this_is_function(this_is_argument, this_is_second_argument):
    return this_is_argument * this_is_second_argument

print(this_is_function("Hello", 10))
print(this_is_function(10, 10))
print(this_is_function(False, 10))
