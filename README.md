Reddit Comments Extractor

# Reddit Comments Extractor

## Overview
This Python script extracts comments from a Reddit post, including nested replies and additional comments from 'more' objects, using Reddit's API. The extracted comments are formatted and saved to a text file in the Downloads directory, copied to the clipboard, and a desktop notification is displayed with the total count of extracted comments.

## Features
- Extracts all comments, including nested replies and 'more' comments.
- Formats the comments with instructions for summarization.
- Saves the extracted comments to a text file in the `Downloads` directory.
- Copies the formatted comments to the clipboard.
- Sends a macOS desktop notification with the total number of extracted comments.

## Installation
### Prerequisites
Ensure you have Python installed, and install the required dependencies:

```sh
pip install requests pyperclip pync
```

## Usage
1. Run the script:

```sh
python reddit_comments_extractor.py
```

2. Enter the Reddit post URL when prompted.
3. The script will extract and process the comments.
4. The formatted comments will be:
   - Saved as `comments.txt` in the `~/Downloads/` directory.
   - Copied to the clipboard.
   - A notification will be displayed showing the number of extracted comments.
5. Type `exit` to quit the script.

## Example Output
When providing a Reddit URL, the script extracts the comments and saves them in the following format:

```
You are the best content writer in the world! These are a reddit post comments.
Summarise the key themes and main points. Identify the top points or themes discussed in the comments, with examples for each. Include a brief overview of any major differing viewpoints if present. Think step by step.

<text>
[Extracted Comments Here]
</text>
```

## Known Issues & Limitations
- The script does not authenticate with Reddit, so it might be subject to rate limits.

## License
This project is licensed under the MIT License.

## Contributions
Pull requests and improvements are welcome! Feel free to fork the repository and submit changes.

