import os

# Get all markdown files in the current directory
markdown_files = [f for f in os.listdir(".") if f.endswith(".md") and f != "Index.md"]

# Sort the files
markdown_files.sort()

# Create the index file
with open("Index.md", "w") as index_file:
    index_file.write("# Index\n\n")
    for f in markdown_files:
        # Replace spaces with %20 for URL encoding
        url_encoded_f = f.replace(" ", "%20")
        index_file.write(f"- [{f}]({url_encoded_f})\n")

