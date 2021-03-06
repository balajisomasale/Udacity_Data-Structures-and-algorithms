import os

def find_files(suffix, path=None):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    
    if path == None:
        return "No path specified"

    # Creating a list inorder to store the paths to return
    list_of_paths = []

    # Listing files and directories in this current path
    current_dir = os.listdir(path)
    
    # Iteration through files and directories
    for item in current_dir:
        new_path = os.path.join(path,item)

        if new_path.endswith(suffix):
                list_of_paths.append(new_path)

        else:
            if os.path.isdir(new_path):
                list_of_paths.extend(find_files(suffix, new_path))

    return list_of_paths



def file_list(list):
    if len(list) > 0:
        return list
    else:      
        return "No files found with suffix"



path = './testdir'

suffix_c = ".c"
print(file_list(find_files(suffix_c,path)))  # Should return list with 4 file paths

suffix_f = ".f"
print(file_list(find_files(suffix_f,path)))  # Should return "no files found with suffix"

print(file_list(find_files(suffix_f,)))  # Should return "No path specified"


#Resubmitting the work : Adding more test cases 

suffix_h=".h"
print(file_list(find_files(suffix_h,path)))   #checking for .h files 

suffix_empty=""
print(file_list(find_files(suffix_empty,path)))   #checking for the Empty files which has NO EXTENSTION
#we will get output as files which are actually the sb folders with NO EXTENSION => Satisfied 