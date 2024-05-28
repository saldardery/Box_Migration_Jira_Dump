import subprocess

# Define the curl command parameters
url = "https://jira.eng.vmware.com/sr/jira.issueviews:searchrequest-csv-current-fields/185524/SearchRequest-185524.csv"
username = "saldardery"
password = "Deer@_91!Deer@_91!"
output_path = "C:\\Users\\powerbi\\Box\\Incorta Backend\\Migration Jira Dump.csv"

# Construct the curl command
curl_command = [
    "curl.exe",
    "-u",
    f"{username}:{password}",
    url,
    "-o",
    output_path,
    "-c -"
]

try:
    # Execute the curl command
    subprocess.run(curl_command, check=True)
    print("Download completed successfully.")
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")
