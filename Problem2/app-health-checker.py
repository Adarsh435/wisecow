from collections import Counter

def analyze_log(log_file):
    # Variables to store analysis results
    num_successful_requests = 0
    status_codes = Counter()

    # Open the log file
    with open(log_file, 'r') as f:
        # Analyze each log line
        for line in f:
            # Split the log line into its components
            parts = line.strip().split(" - ")

            # Extract the status code from the log line
            status_code = int(parts[-1].split(":")[-1].strip())

            # Count the number of successful requests (status code 200)
            if status_code == 200:
                num_successful_requests += 1

            # Count the occurrences of each status code
            status_codes[status_code] += 1

    # Print summarized report
    print("Number of successful requests (Status code 200):", num_successful_requests)
    print("\nStatus codes:")
    for code, count in status_codes.items():
        print(f"Status code {code}: {count} occurrences")

# Example usage
if __name__ == "__main__":
    log_file = 'health-check.log'  # Replace 'your_log_file.log' with the path to your actual log file
    analyze_log(log_file)
