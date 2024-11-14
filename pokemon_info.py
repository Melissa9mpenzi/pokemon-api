import requests

response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")

pikachu_data = response.json()  # Pikachu's reply in JSON format

# Now, you can access Pikachu's abilities
abilities = pikachu_data["abilities"]

# Display the first 3 abilities of Pikachu
for ability in abilities[:3]:
    print(ability["ability"]["name"])
    
# let the user type in the name of any Pokémon to learn about its abilities

# Step 1: Get Pokemon name from user
pokemon_name = input("Enter a Pokemon name: ").lower()

# Step 2: Send a request to the API to get details for the specified Pokemon
response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")

# Step 3: Check if the request was successful
if response.status_code == 200:
    pokemon_data = response.json()  # Parse JSON response
    abilities = pokemon_data["abilities"]  # Get abilities list

    print(f"\n{pokemon_name.capitalize()} has the following abilities:")
    for ability in abilities[:3]:  # Only show up to 3 abilities
        print(ability["ability"]["name"])  # Print each ability name
else:
    print("Pokemon not found! Check the spelling and try again.")
