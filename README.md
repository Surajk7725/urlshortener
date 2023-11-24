# URL Shortener

This Python script provides a simple GUI-based URL shortening tool using the tkinter library for the graphical user interface, pyperclip for copying to the clipboard, and pyshorteners for shortening URLs.

## Getting Started

### Prerequisites

Make sure you have the required libraries installed. You can install them using the following:

- **pip install pyperclip pyshorteners**

### Running the Application

Run the script (python url.py) in a Python environment. The GUI window will appear, allowing you to shorten URLs.

## Using the URL Shortener
Enter the URL you want to shorten in the provided text entry.
Click on the "Generate Short URL" button.
The shortened URL will be displayed in the second text entry.
Click on the "Copy Short URL" button to copy the shortened URL to your clipboard.

## GUI Elements
- **URL Entry:** Text entry for the user to input the long URL that needs to be shortened.
- **Generate Short URL Button:** Initiates the URL shortening process.
- **Short URL Entry:** Displays the shortened URL after it has been generated.
- **Copy Short URL Button:** Copies the shortened URL to the clipboard.

## Customization
The script currently uses the TinyURL shortening service. You can explore other services provided by pyshorteners and modify the script accordingly.

- **Line:** url_short = pyshorteners.Shortener().tinyurl.short(urladdress)

## Dependencies
1)pyperclip: Used to interact with the clipboard for copying the shortened URL.

2)pyshorteners: A library that provides a convenient interface to various URL shortening services.



