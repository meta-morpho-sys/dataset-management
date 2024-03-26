from data_clean_utility.anomalies_discovery import visualise_anomalies
from data_clean_utility.setup_working_dir import prepare_location
from data_clean_utility.print_duplicates import detect_non_standard_unit_nos, print_duplicates
from data_clean_utility.duplicates_merger import merge_duplicates


def main():
    path_to_csv, output_directory = prepare_location()

    # actual merging
    merge_duplicates(path_to_csv, output_directory)

    # Additional insight on rows like:
    # anomalies visualisation
    visualise_anomalies(path_to_csv, output_directory)
    detect_non_standard_unit_nos(path_to_csv, output_directory)

    # duplicates visualisation
    print_duplicates(path_to_csv, output_directory)




# Entry point of the program
if __name__ == "__main__":
    main()
