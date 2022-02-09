from dataframe_services.dataframe_to_csv_exporter import export_concatenated_dataframe_data
from file_folder_services.path_generator import get_folder_path
from dataframe_services.dataframe_from_csv_generator import generate_dictionary_of_dataframes_from_csv_folder
from dataframe_services.dataframe_merger import left_merge_dataframe
from dataframe_services.dataframe_information_generator import generate_dataframe_information

def orchestrate_olympic_analysis():
    folder_path = get_folder_path(
        title_message='input_folder')

    dictionary_of_dataframes = \
        generate_dictionary_of_dataframes_from_csv_folder(
            folder_path=folder_path)

    athletes_dataframe = \
        left_merge_dataframe(
            dictionary_of_dataframes=dictionary_of_dataframes)

    generate_dataframe_information(
        dataframe=athletes_dataframe)

    export_concatenated_dataframe_data(
        dataframe=athletes_dataframe,
        file_name='athletes_dataframe')
    return \
        athletes_dataframe
