from pydlt import DltFileReader

# Read DLT messages from file
for msg in DltFileReader("sample.dlt"):
    # Print overview of each DLT message
    print(msg)
