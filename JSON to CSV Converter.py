# JSON to CSV Converter
import json
import csv
import os

if __name__ == '__main__':
    try:
        # Ask user for file names
        input_file = input("Enter JSON input file name (e.g., input.json): ").strip()
        output_file = input("Enter output CSV file name (e.g., output.csv): ").strip()

        # Check input file
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"Input file '{input_file}' not found")

        # Warn if output file exists
        if os.path.exists(output_file):
            choice = input(f"'{output_file}' already exists. Overwrite? (y/n): ").lower()
            if choice != 'y':
                print("Operation cancelled.")
                exit()

        # Read JSON
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Validate JSON structure
        if not isinstance(data, list) or len(data) == 0:
            raise ValueError("JSON must contain a non-empty list of objects")

        # Collect all possible headers (handles different keys in objects)
        headers = set()
        for item in data:
            headers.update(item.keys())
        headers = list(headers)

        # Write CSV (this creates the file if it doesn't exist)
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)

        print(f"Successfully converted '{input_file}' → '{output_file}'")

    except FileNotFoundError as e:
        print(f"{e}")
    except json.JSONDecodeError:
        print("Invalid JSON format.")
    except Exception as ex:
        print(f'Error: {str(ex)}')