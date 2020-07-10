import logging
import requests
import argparse
import pprint

# Weblink to access
BOOK = "https://www.anapioficeandfire.com/api/books"

def main():
    
    # Register logging information
    logging.basicConfig(filename='icefire.log', format='%(levelname)s:%(asctime)s%(message)s', datefmt = '%m/%d/%Y %I:%M:%S %p', level=logging.INFO)

    try:
        logging.info('Scripting started')
        icefire = requests.get(BOOK + "/" + args.bookno)
       
        # Generating an error
        print(10/0)

        # Pretty print the json response
        pprint.pprint(icefire.json())
    
        # Write response code to log
        logging.info("API Response Code - " + str(icefire))
    
    except Exception as err:
        logging.critical(err)

    finally:
        logging.info("Program ended")


if __name__ == '__main__':
    
    # Give a book No when this program is executed
    parser = argparse.ArgumentParser()
    parser.add_argument('--bookno', help='Enter the book number (integer) to look up.')
    args = parser.parse_args()
    main()
