import os
import fnmatch

def modify_file_name(path, new_word):
    if(os.path.exists(path)):
        new_file_name = os.path.join(os.path.dirname(path), new_word)
        os.rename(path, new_file_name)
        return new_file_name

def modify_file_content(path, suffix, old_text, new_text):
    if(os.path.exists(path)):
        if path.endswith(suffix):
            with open(path, 'r') as f:
                content = f.read()
            if old_text in content:
                content = content.replace(old_text, new_text)
                with open(path, 'w') as f:
                    f.write(content)
    else:
        print(f"content file path no exists")


def rename_folders(start_dir):
    for foldername in os.listdir(start_dir):
        #print(f"foldername is {foldername}")
        folderpath = os.path.join(start_dir, foldername)
        #print(f"folderpath is {folderpath}")
        if os.path.isdir(folderpath):
            # modify dirs name if it is dir in regression
            rename_folders(folderpath)
            # modify current dir name
            newname = foldername.replace(old_word, new_word)
            #print(f"newname is {newname}")
            os.rename(folderpath, os.path.join(start_dir, newname))

if __name__ == '__main__':
    # Input old_word and find match content
    old_word = input('Please input old word: ')
    new_word = input('Please input new word: ')
    suffix   = input('Please input suffix: ')
    start_dir = os.getcwd()
    matching_files = []
    matching_dirs = []

    #Rename folders in regression
    rename_folders(start_dir)

    #Iteration modify file content and file name
    for root, dirs, files in os.walk(start_dir):
        for f in files:
            if fnmatch.fnmatch(f, '*' + old_word + '*'):
                matching_files.append(os.path.join(root, f))
    for f in matching_files:
        file_name = os.path.basename(f)
        old_text_list = os.path.splitext(file_name)
        old_text = str(old_text_list[0])
        new_text = new_word
        new_file_content = modify_file_content(f, suffix, old_word, new_text)
        new_file_path = modify_file_name(f, file_name.replace(old_word, new_word ))