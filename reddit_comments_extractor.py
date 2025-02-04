import requests
import os
import pyperclip
from pync import Notifier

def fetch_more_comments(more_node, link_id):
    """
    Fetch additional comments using Reddit's morechildren API endpoint.
    """
    children_ids = ",".join(more_node["data"]["children"])
    api_url = f"https://www.reddit.com/api/morechildren.json?api_type=json&link_id={link_id}&children={children_ids}"
    headers = {"User-agent": "Reddit Comment Extractor"}
    try:
        response = requests.get(api_url, headers=headers)
        json_data = response.json()
        if (
            "json" in json_data and 
            "data" in json_data["json"] and 
            "things" in json_data["json"]["data"]
        ):
            return json_data["json"]["data"]["things"]
        return []
    except Exception as error:
        print(f"Error fetching more comments: {error}")
        return []

def extract_comments(comments_array, link_id):
    """
    Recursively extracts comments from the provided array, including nested replies
    and fetching additional comments from 'more' objects.
    """
    result = []
    for c in comments_array:
        if c["kind"] == "t1":
            if "body" in c["data"]:
                result.append(c["data"]["body"])
            replies = c["data"].get("replies")
            if replies and isinstance(replies, dict):
                children = replies.get("data", {}).get("children", [])
                result.extend(extract_comments(children, link_id))
        elif c["kind"] == "more":
            more_comments = fetch_more_comments(c, link_id)
            result.extend(extract_comments(more_comments, link_id))
    return result

def extract_and_save_reddit_comments():
    while True:
        try:
            url = input("Enter the Reddit post URL (or type 'exit' to quit): ").strip()
            if url.lower() == 'exit':
                print("Exiting the script.")
                break
            if not url.endswith(".json"):
                url += ".json"
            headers = {"User-agent": "Reddit Comment Extractor"}
            response = requests.get(url, headers=headers)
            data = response.json()

            # Determine the thread's link_id from the submission data
            try:
                link_id = data[0]["data"]["children"][0]["data"]["name"]
            except Exception:
                print("Could not determine the thread link ID. Is this a valid Reddit post?")
                continue

            # Extract all comments, including nested and "more" comments
            comments_data = data[1]["data"]["children"]
            extracted_comments_list = extract_comments(comments_data, link_id)
            extracted_comments = "\n\n".join(extracted_comments_list)

            # Add formatting and instructions to the comments
            formatted_comments = f"""You are the best content writer in the world! These are a reddit post comments.
Summarise the key themes and main points. Identify the top points or themes discussed in the comments, with examples for each. Include a brief overview of any major differing viewpoints if present. Think step by step.

<text>
{extracted_comments}
</text>"""

            # Save comments to a text file in the Downloads directory
            file_name = "comments.txt"
            file_path = os.path.expanduser("~/Downloads/" + file_name)
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(formatted_comments)

            # Copy the contents to the clipboard using pyperclip
            pyperclip.copy(formatted_comments)

            print(f"Comments saved to: {file_path}\nComments also copied to clipboard.")

            # Display a desktop notification with the count of extracted comments
            num_comments = len(extracted_comments_list)
            Notifier.notify(f"{num_comments} comments extracted.", title="Reddit Comments Extractor")

        except Exception as error:
            print(f"An error occurred: {error}")

if __name__ == "__main__":
    extract_and_save_reddit_comments()