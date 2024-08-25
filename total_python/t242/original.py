# Generated by ChatGPT
import os
import shutil

# Define the file extensions for each category
categories = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx'],
    'Archives': ['.zip', '.rar', '.tar', '.gz', '.7z']
}


# Function to organize files into subfolders based on extensions
def organize_files(desktop_path):
    for category, extensions in categories.items():
        category_path = os.path.join(desktop_path, category)

        # Create the category folder if it doesn't exist
        if not os.path.exists(category_path):
            os.makedirs(category_path)

        # Move files to the appropriate category folder
        for item in os.listdir(desktop_path):
            item_path = os.path.join(desktop_path, item)

            if os.path.isfile(item_path):
                file_extension = os.path.splitext(item)[1].lower()
                if file_extension in extensions:
                    shutil.move(item_path, os.path.join(category_path, item))
                    print(f'Moved: {item} to {category}')


# Main function to run the script
def main():
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    print(desktop_path)
    organize_files(desktop_path)
    print('Files have been organized.')


if __name__ == '__main__':
    main()
