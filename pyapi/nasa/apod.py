#!/usr/bin/env python3
import urllib.request
import json

NASAAPI = "https://api.nasa.gov/planetary/apod?"

def main():
    with open("/home/student/nasa/nasa.creds") as mycreds:
        nasacreds = mycreds.read()

    # Remove any extra new line feeds
    nasacreds = "api_key=" + nasacreds.strip("\n")

    # Call the webservice with our key
    apodurlobj = urllib.request.urlopen(NASAAPI + nasacreds)

    # Read the file-like object
    apodread = apodurlobj.read()

    # Decode JSON to Python data structure
    apod = json.loads(apodread.decode("utf-8"))

    # Display our Pythonic data
    print("\n\nConverted Python data")
    print(apod)

    print()
    print(apod["title"] + "\n")
    print(apod["date"] + "\n")
    print(apod["explanation"] + "\n")
    print(apod["url"])

    ## Uncomment the code below if running in a GUI
    ## and you want to open the URL in a browser
    ## use Firefox to open the HTTPS URL
    ## input("\nPress Enter to open NASA Picture of the Day in Firefox")
    ## webbrowser.open(decodeapod["url"])

if __name__ == "__main__":
    main()
