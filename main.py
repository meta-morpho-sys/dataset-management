from anomalies_discovery import visualise_anomalies
from setup_working_dir import prepare_location
from print_duplicates import print_multiples
from duplicates_merger import print_merges


def main():
    path_to_csv, output_directory = prepare_location()

    visualise_anomalies(path_to_csv, output_directory)
    print_multiples(path_to_csv, output_directory)
    print_merges(path_to_csv, output_directory)


# Entry point of the program
if __name__ == "__main__":
    main()
