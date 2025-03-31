import os

def search_string_in_py_files(folder_path, search_string):
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    try:
                        content = f.read()
                        if search_string in content:
                            print(f"Found in: {file_path}")
                    except Exception as e:
                        print(f"Could not read file {file_path}: {e}")

# Example usage
folder_path = r"C:\Users\20220806\AppData\Roaming\Blender Foundation\Blender\4.1\scripts\addons"  # Replace with your folder path
search_string = "mmr.import_vmd"     # Replace with the string you want to search
search_string_in_py_files(folder_path, search_string)