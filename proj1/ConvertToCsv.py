import pandas as pd
import os

# Get the current script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path for the .txt file (assuming the filename is known)
txt_filename = os.path.join(script_dir, "sachs.data.txt")

# Load the text file as a DataFrame
df = pd.read_csv(txt_filename, sep="\s+", header=None)

# Construct the path for the output CSV file (changing extension)
csv_filename = os.path.join(script_dir, "sachs_data.csv")

# Save the DataFrame to a CSV file
df.to_csv(csv_filename, index=False)

print(f"Data has been saved to {csv_filename}")
