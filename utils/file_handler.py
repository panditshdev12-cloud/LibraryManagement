import csv
import os


class FileHandler:
    """Handles CSV file operations."""

    @staticmethod
    def save_data(filename, data, headers):
        try:
            with open(filename, "w", newline="") as file:
                writer = csv.DictWriter(
                    file,
                    fieldnames=headers
                )

                writer.writeheader()
                writer.writerows(data)

        except IOError as error:
            print(f"Error saving file: {error}")

    @staticmethod
    def load_data(filename):
        data = []

        try:
            if not os.path.exists(filename):
                return data

            with open(filename, "r", newline="") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    data.append(row)

        except IOError as error:
            print(f"Error loading file: {error}")

        return data

    @staticmethod
    def create_file(filename, headers):
        if not os.path.exists(filename):
            try:
                with open(filename, "w", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow(headers)

            except IOError as error:
                print(f"Error creating file: {error}")