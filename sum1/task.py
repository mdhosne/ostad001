import os

# Directory to store operation result files
DATA_DIR = "operations"
os.makedirs(DATA_DIR, exist_ok=True)  # Create directory if it doesn't exist

# Function to get the file path for an operation
def get_file_path(operation):
    return os.path.join(DATA_DIR, f"{operation}.txt")

# Function to write result to a file
def write_result(operation, result):
    file_path = get_file_path(operation)
    with open(file_path, "w") as file:
        file.write(str(result))
    print(f"Result of '{operation}' saved as {result} in {file_path}.")

# Function to read result from a file
def read_result(operation):
    file_path = get_file_path(operation)
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return int(file.read())  # Assuming all results are integers
    print(f"File for '{operation}' not found.")
    return None

# Function to perform addition, subtraction, or multiplication
def perform_operation(operation, a, b):
    if operation == "add":
        result = a + b
    elif operation == "subtract":
        result = a - b
    elif operation == "multiply":
        result = a * b
    else:
        raise ValueError(f"Unknown operation: {operation}")
    
    write_result(operation, result)
    return result

# Example usage
if __name__ == "__main__":
    # Perform operations
    a, b = 10, 5
    print(f"Adding {a} and {b}: {perform_operation('add', a, b)}")
    print(f"Subtracting {b} from {a}: {perform_operation('subtract', a, b)}")
    print(f"Multiplying {a} and {b}: {perform_operation('multiply', a, b)}")

    # Read saved results
    print("Saved Addition Result:", read_result("add"))
    print("Saved Subtraction Result:", read_result("subtract"))
    print("Saved Multiplication Result:", read_result("multiply"))
