def get_files_from_dir(dirpath):
    """
    Get all files from a directory path.

    Params
    ------
    dirpath: string
        The path of directory.

    Returns
    -------
    array-like
        The list containing all filenames.
    """
    return [f for f in listdir(dirpath) if isfile(join(dirpath, f))]
