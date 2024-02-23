import os
import shutil
import msvcrt

# Get the current directory
current_dir = os.getcwd()

# Create the output folder
output_folder = os.path.join(current_dir, 'output')
os.makedirs(output_folder, exist_ok=True)

# Ask how many copies are needed
while True:
    copies = input("How many copies do you need? ")
    if copies.isdigit() and int(copies) > 0:
        copies = int(copies)
        break
    else:
        print("Please enter a valid number.")


# Iterate over the files in the current directory
for filename in os.listdir(current_dir):
    if os.path.isfile(filename) and not filename.startswith('renamer'):
        # Print the filename with the message
        print("Processing file: ", filename)
        
        # Get the file extension
        file_extension = os.path.splitext(filename)[1]

        # Create 1000 copies of the file
        for i in range(1, copies):
            # Generate the new filename
            
            new_filename = f"{os.path.splitext(filename)[0]}-{str(i).zfill(4)}{file_extension}"

            # Copy the file to the output folder
            shutil.copy2(filename, os.path.join(output_folder, new_filename))

            # Print the message with the copied file number
            print("Copied: ", i)

print("All files have been copied successfully!")
print("Press any key to close...")
msvcrt.getch()
