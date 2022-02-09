def get_clean_file_names(
        file_names: list) -> list:
    clean_file_names = \
        []

    for file_name in file_names:
        clean_file_name = file_name.lower().strip().replace(" ", "_").replace("?", "").replace("-", "_"). \
            replace(r"/", "_").replace("\\", "_").replace("&", "").replace(")", "").replace(r"(", "").replace("$", "")

        clean_file_names.append(
            clean_file_name)

    return \
        clean_file_names
