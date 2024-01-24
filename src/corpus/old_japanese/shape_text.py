# coding=utf-8
# Copyright 2021 rinna Co., Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from tqdm import tqdm

from corpus.old_japanese.config import Config

config = Config()
N_LINES_PER_FILE = 1e3

def detect_utf(book_data_path):
    with open(f"{book_data_path}", "rb") as text_file:
        bom = text_file.read(3)
        if bom != b'\xef\xbb\xbf':
            return "utf-8"
        else:
            return "utf-8-sig"


def split_file(book_data_path):
    white_data = []
    # detect utf-8 bom
    encode = detect_utf(book_data_path)

    with open(f"{book_data_path}", "r", encoding=encode) as text_file:
            blank_line = False
            first_line = True
            for line in text_file:
                #  # delete 〓 <- this
                line = line.replace("〓", "")

                if first_line and line == "\n":
                    continue
                else:
                    first_line = False

                if line == "\n":
                    continue
                
                white_data.append(line)
    with open(f"{book_data_path}", "w", encoding="utf-8") as text_file:
        text_file.write("".join(white_data))

if __name__ == "__main__":
    doc_dir = config.doc_data_dir

    for book_name in os.listdir(doc_dir):
        print(book_name)
        book_data_path = f"{doc_dir}/{book_name}"
        split_file(book_data_path)

