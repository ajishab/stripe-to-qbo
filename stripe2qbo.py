import sys
import csv

def process_csv(input_file, output_file):
    with open(input_file, 'r') as file:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames

        # Select the desired columns
        columns_to_keep = ['created', 'gross', 'fee', 'description']
        selected_columns = [field for field in fieldnames if field in columns_to_keep]

        # Store the fee values for calculating the sum
        fees = []

        with open(output_file, 'w', newline='') as output:
            writer = csv.DictWriter(output, fieldnames=selected_columns + ['debited'])
            writer.writeheader()

            for row in reader:
                # Truncate 'created' column values to the first 10 characters
                row['created'] = row['created'][:10]

                # Perform modifications based on 'gross' values
                gross_value = float(row['gross'])
                debited_value = -gross_value if gross_value < 0 else 0
                row['debited'] = debited_value
                row['gross'] = 0 if gross_value < 0 else gross_value

                # Write the modified row to the output file
                writer.writerow({field: row[field] for field in selected_columns + ['debited']})

                # Store the fee value for sum calculation
                fees.append(float(row['fee']))

            # Calculate the sum of 'fee' column values
            fee_sum = sum(fees)

            # Write the final row with the specified values
            writer.writerow({
                'created': row['created'],
                'gross': 0,
                'fee': 0,
                'description': 'Monthly Payment Processing Fees',
                'debited': fee_sum
            })

# Check if the correct number of command-line arguments is provided
if len(sys.argv) != 3:
    print("Usage: python script.py input_file output_file")
else:
    # Get input and output filenames from command-line arguments
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    # Process the CSV file
    process_csv(input_filename, output_filename)
