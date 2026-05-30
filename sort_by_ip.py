from pathlib import Path

# Get the desktop path automatically
desktop = Path.home() / "Desktop"
input_file = desktop / "mixed_behavior_uba_logs.txt"
output_file = desktop / "mixed_behavior_uba_logs_sorted_by_ip.txt"

# Read the file
with open(input_file, 'r') as f:
    lines = f.readlines()

# Separate header from data
header = lines[0]
data_lines = lines[1:]

# Parse and sort data by IP address (third column)
parsed_data = []
for line in data_lines:
    parts = line.strip().split('\t')
    ip_address = parts[2]  # Third column (index 2)
    parsed_data.append((ip_address, line))

# Sort by IP address
parsed_data.sort(key=lambda x: x[0])

# Write sorted data to new file
with open(output_file, 'w') as f:
    f.write(header)
    for _, line in parsed_data:
        f.write(line)

print(f"Sorted data saved to {output_file}")
print(f"Total records: {len(parsed_data)}")
