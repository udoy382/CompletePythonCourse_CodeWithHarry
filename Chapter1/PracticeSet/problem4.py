import os

def list_directory_contents(directory):
    try:
        # Get the list of files and directories in the specified directory
        contents = os.listdir(directory)
        
        # Print each item in the directory
        print(f"Contents of '{directory}':")
        for item in contents:
            print(item)
    
    except FileNotFoundError:
        print(f"Error: The directory '{directory}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied to access '{directory}'.")

if __name__ == "__main__":
    # Specify the directory you want to list
    directory_path = input("Enter the path of the directory to list: ")
    
    # Call the function to list contents
    list_directory_contents(directory_path)
