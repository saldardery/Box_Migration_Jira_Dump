import pandas as pd

# Read the CSV file
df = pd.read_csv('C:\\Users\\powerbi\\Box\\Incorta Backend\\Migration Jira Dump.csv')

# Add empty columns
df['Project key'] = ''
df['Project name'] = ''
df['Project type'] = ''
df['Project lead'] = ''
df['Project description'] = ''
df['Project url'] = ''
df['Custom field (GEO)'] = ''

# Save the modified DataFrame to a new CSV file
df.to_csv('C:\\Users\\powerbi\\Box\\Incorta Backend\\Migration Jira Dump.csv', index=False)
df.to_csv('C:\\Users\\powerbi\\Box\\SW Migrations\\Migration Jira Dump.csv', index=False)
