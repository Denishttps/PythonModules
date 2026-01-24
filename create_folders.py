import pathlib

def create_folders(path_to_main_folder, subfolder_names):
    """
    Create folders for the given list of folder paths.

    Parameters:
    subfolder_names (list of str): List of folder paths to create.
    """
    for path in subfolder_names:
        pathlib.Path(path_to_main_folder, path).mkdir(parents=True, exist_ok=True)


if __name__ == "__main__":
    main_folder = input("Enter the path to the main folder: ")
    subfolders = [f"ex{i}" for i in range(int(input("Enter the number of subfolders to create: ")))]
    create_folders(main_folder, subfolders)