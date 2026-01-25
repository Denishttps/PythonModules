import pathlib


def create_folders(path_to_main_folder, subfolder_names):
    for path in subfolder_names:
        pathlib.Path(path_to_main_folder, path).mkdir(
            parents=True, exist_ok=True
        )


if __name__ == "__main__":
    main_folder = input("Enter the path to the main folder: ")
    count = int(input("Enter the number of subfolders to create: "))
    subfolders = [f"ex{i}" for i in range(count)]
    create_folders(main_folder, subfolders)
