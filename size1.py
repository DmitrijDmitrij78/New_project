import os

def format_size(size):
    if size >= 1024 * 1024:
        return f"{size / (1024 * 1024):.1f} МБ"
    elif size >= 1024:
        return f"{size / 1024:.1f} КБ"
    else:
        return f"{size} Б"

directory_path = os.getcwd()
files_with_sizes = []

for filename in os.listdir(directory_path):
    if os.path.isfile(os.path.join(directory_path, filename)):
        size = os.path.getsize(os.path.join(directory_path, filename))
        files_with_sizes.append((filename, size))

files_with_sizes.sort(key=lambda x: x[1], reverse=True)

print("Список файлов:")
for i, (filename, size) in enumerate(files_with_sizes, start=1):  
   print(f"{i}. {filename} - {format_size(size)}")
