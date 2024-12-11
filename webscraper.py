import os
import requests
from bs4 import BeautifulSoup

print("Hello World")


def scrape_images(url, folder_name):
    """Scrapes images from a given URL and saves them to a folder."""
    # Create the folder if it doesn't exist
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Send a GET request to the URL
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for bad status codes

    # Parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all the image tags
    img_tags = soup.find_all("img")

    imgs = []

    # Download each image
    for img_tag in img_tags:
        img_url = img_tag.get("src")
        if img_url and img_url.startswith("http"):  # Check if the URL is valid
            img_name = os.path.basename(img_url)
            img_path = os.path.join(folder_name, img_name)

            # Send a GET request to the image URL
            img_response = requests.get(img_url)
            img_response.raise_for_status()

            # Save the image to the folder
            with open(img_path, "wb") as f:
                f.write(img_response.content)

            # print(f"Downloaded: {img_url}")

            imgs.append(img_url)

    return imgs
