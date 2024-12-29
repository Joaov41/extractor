import requests
import json
import os
import pyperclip

def extract_and_save_reddit_comments():
    while True:
        try:
            # Prompt the user to enter a URL
            url = input("Enter the Reddit post URL (or type 'exit' to quit): ").strip()
            if url.lower() == 'exit':
                print("Exiting the script.")
                break
            if not url.endswith(".json"):
                url += ".json"
            headers = {"User-agent": "Reddit Comment Extractor"}

            # Send HTTP request
            response = requests.get(url, headers=headers)
            data = response.json()

            # Function to recursively extract comments from Reddit thread
            def extract_comments(comments_array):
                result = []
                for c in comments_array:
                    if c["kind"] == "t1":
                        result.append(c["data"]["body"])
                        if c["data"].get("replies") and c["data"]["replies"]["data"]["children"]:
                            result.extend(extract_comments(c["data"]["replies"]["data"]["children"]))
                return result

            # Extract comments and join them into a single string
            extracted_comments = "\n\n".join(extract_comments(data[1]["data"]["children"]))

            # Add formatting and instructions to the comments
            formatted_comments = f"""You are the best content writer in the world! These are a reddit post comments.
Summarise the key themes and main points. Identify the top points or themes discussed in the comments, with examples for each. Include a brief overview of any major differing viewpoints if present. Think step by step.

<text>
{extracted_comments}
</text>"""

            # Save comments to a text file in the Downloads directory
            file_name = "comments.txt"
            file_path = os.path.expanduser("~/Downloads/" + file_name)
            with open(file_path, "w") as file:
                file.write(formatted_comments)

            # Inform the user
            print(f"Comments saved to: {file_path}\nComments also copied to clipboard.")

            # Copy the contents to clipboard using pyperclip
            pyperclip.copy(formatted_comments)

        except Exception as error:
            print(f"An error occurred: {error}")

# Execute the script
extract_and_save_reddit_comments()