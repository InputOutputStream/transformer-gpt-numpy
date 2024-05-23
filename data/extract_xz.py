import os
import lzma
from tqdm import tqdm

def xz_files_in_dir(directory):
    files = []
    for filename in os.listdir(directory):
        if (filename.endswith(".xz") or filename.endswith(".lzma")) and os.path.isfile(os.path.join(directory, filename)):
            files.append(filename)
    return files

folder_path = "/home/father/Desktop/hgpt"
output_file_train = "train_split.txt"
output_file_val = "val_split.txt"
# output_file = "output{}.txt"
vocab_file = "vocab.txt"
# split_files = int(input("Howmany files would you like to split this into: "))

files = xz_files_in_dir(folder_path)
total_files = len(files)
split_index = int(total_files * 0.9)


files_train = files[:split_index]
files_val = files[split_index:]

# max_count = total_files // split_files if split_files != 0 else total_files

vocab = set()

with open(output_file_train, 'w', encoding="utf-8") as outfile:
    for count, filename in enumerate(tqdm(files_train, total=len(files_train))):
        file_path = os.path.join(folder_path, filename)
        print("train file : ", filename)
        with lzma.open(file_path, 'rt', encoding="utf-8") as infile:
            text = infile.read()
            outfile.write(text)
            character = set(text)
            vocab.update(character)
with open(output_file_val, 'w', encoding="utf-8") as outfile:
    for filename in tqdm(files_val, total=len(files_val)):
        file_path = os.path.join(folder_path, filename)
        print("val file : ", filename)
        with lzma.open(file_path, 'rt', encoding='utf-8') as infile:
            text = infile.read()
            outfile.write(text)
            characters = set(text)
            vocab.update(characters)
            
with open(vocab_file, 'w', encoding="utf-8") as vfile:
    for char in vocab:
        vfile.write(char + '\n')
