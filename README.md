Reddit Comment Extractor

Reddit Comment Extractor is a Python script designed to fetch all comments (including nested ones) from a Reddit post and save them as a formatted text file. 
Additionally, it copies the comments to your clipboard for easy use. 

Features
	•	Extracts all comments, including replies (nested comments), from a Reddit post.
	•	Formats the extracted comments with instructions for summarization.
	•	Saves the comments to a .txt file in your system’s Downloads folder.
	•	Copies the formatted comments directly to your clipboard for convenience.
 Instruction for Mac

 Prerequisites
	1.	Python 3.7 or later: Make sure Python is installed on your system. 
	2.	Pip: Ensure pip is installed.

Create a folder and place the py file inside.
CD into that folder
pip install requests pyperclip
python red.py

Running this script it will ask you for the URL of the reddit post.
The script will extract all comments including nested, attach a promtp to the comments and cpy them to clipboard.
Then you can just simply paste in your LLM of choice and it will provide a detailed summary of the comments.
It also created a txt document with those comments in case of need.
