import glob
import os
import requests
import zipfile
from io import BytesIO
from corpus.old_japanese.config import Config


config = Config()

def download_texts(url=config.data_url, text_dir=config.text_dir):
    print("Downloading texts...")
    r = requests.get(url)
    z = zipfile.ZipFile(BytesIO(r.content))
    z.extractall(text_dir)
    os.rename(text_dir + "shaped-text", text_dir + "doc_data")
    print("Done.")

if __name__ == "__main__":
    download_texts()