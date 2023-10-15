import cloudscraper
import time
import winsound

# List of URLs you want to check
urls = [

    "https://in.bookmyshow.com/buytickets/my-cinemas-redcarpet-kariyad/cinema-kryd-MYCR-MT/20231019",
]

# Text to search for on the webpages
search_text = "Leo"

# Initialize a cloudscraper session
scraper = cloudscraper.create_scraper()

while True:
    for url in urls:
        # Send an HTTP GET request to the website
        response = scraper.get(url)

        # Check if the response status code is 200 (OK)
        if response.status_code == 200:
            # Check if the search text is present in the webpage's content
            if search_text in response.text:
                print(f"Text '{search_text}' found on {url}")
                winsound.Beep(500, 1000)  # Beep
                time.sleep(1)  # Pause for 1 second
                winsound.Beep(500, 1000)  # Beep
                time.sleep(1)  # Pause for 1 second
                winsound.Beep(500, 1000)  # Beep
                winsound.Beep(500, 1000)  # Beep
                time.sleep(1)  # Pause for 1 second
                winsound.Beep(500, 1000)  # Beep
                time.sleep(1)  # Pause for 1 second
                winsound.Beep(500, 1000)  # Beep
                exit()  # Exit the script when text is found
            else:
                print(f"Text '{search_text}' not found on {url}")
        else:
            print(f"Failed to retrieve the webpage at {url}. Status code: {response.status_code}")

    # Wait for 30 seconds before checking again
    time.sleep(60)
