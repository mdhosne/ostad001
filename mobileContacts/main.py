import json

# Function to save data to a file
def save_data(filename, name, mobile_number):
    data = {
        "name": name,
        "mobile_number": mobile_number
    }
    with open(filename, 'w') as file:
        json.dump(data, file)
    print(f"Data saved to {filename}")


# Function to load data from a file
def load_data(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            print(f"Name: {data['name']}")
            print(f"Mobile Number: {data['mobile_number']}")
    except FileNotFoundError:
        print(f"File {filename} not found.")
    except json.JSONDecodeError:
        print(f"File {filename} is not in the correct format.")


# Main program
if __name__ == "__main__":
    filename = "user_data.json"

    # Save data
    name = "John Doe"
    mobile_number = "1234567890"
    save_data(filename, name, mobile_number)

    # Load and display data
    load_data(filename)

