import requests
import torch
import webscraper
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-large"
).to("cuda")

url = "https://www.google.com/search?q=pot+boiling+over&sca_esv=abe1209c8be175c1&udm=2&biw=1440&bih=785&sxsrf=ADLYWIJfdM_fRDnTcg4bAkrVzGkpEeDzbw%3A1729525428153&ei=tHYWZ4T6CP3f5NoP1ceqkAQ&ved=0ahUKEwiEpJmm6J-JAxX9L1kFHdWjCkIQ4dUDCBA&uact=5&oq=pot+boiling+over&gs_lp=Egxnd3Mtd2l6LXNlcnAiEHBvdCBib2lsaW5nIG92ZXIyBRAAGIAEMgUQABiABDIFEAAYgAQyBBAAGB4yBBAAGB4yBBAAGB4yBBAAGB4yBBAAGB4yBhAAGAUYHjIGEAAYBRgeSMIhUJwFWMEgcAN4AJABAJgBigGgAeIKqgEEMTMuNLgBA8gBAPgBAZgCEqACuArCAg0QABiABBixAxhDGIoFwgIIEAAYgAQYsQPCAgYQABgHGB7CAgoQABiABBhDGIoFwgIEECMYJ8ICCxAAGIAEGLEDGIMBwgIQEAAYgAQYsQMYQxiDARiKBcICBxAAGIAEGArCAgoQABiABBixAxgKmAMAiAYBkgcEMTQuNKAHjVQ&sclient=gws-wiz-serp"  # Replace with the desired website URL
folder_name = "boiling_pot_images"

img_urls = webscraper.scrape_images(url, folder_name)


def reader(img_urls):
    descriptions = []
    for img_url in img_urls:
        pic = []
        raw_image = Image.open(requests.get(img_urls[0], stream=True).raw).convert(
            "RGB"
        )

        # conditional image captioning
        text = "a photography of"
        inputs = processor(raw_image, text, return_tensors="pt").to("cuda")

        out = model.generate(**inputs)
        pic.append(processor.decode(out[0], skip_special_tokens=True))

        # unconditional image captioning
        inputs = processor(raw_image, return_tensors="pt").to("cuda")

        out = model.generate(**inputs)
        pic.append(processor.decode(out[0], skip_special_tokens=True))
        descriptions.append(pic)
    return descriptions


print(reader(img_urls))
