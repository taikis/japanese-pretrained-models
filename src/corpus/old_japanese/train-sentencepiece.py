#!/usr/bin/env python3

# From https://github.com/yoheikikuta/bert-japanese
# Copylight (c) 2020 @yoheikikuta
# Apache-2.0 license

import configparser
import glob
import os
import sentencepiece as sp
from corpus.old_japanese.config import Config

config = Config()


TEXTDIR = config.text_dir
PREFIX = config.sp_prefix
VOCABSIZE = config.vocab_size
CTLSYMBOLS = config.ctl_symbols


def _get_text_file(text_dir=TEXTDIR):
    file_list = glob.glob(f'{text_dir}/*.txt')
    files = ",".join(file_list)
    return files


def train(prefix=PREFIX, vocab_size=VOCABSIZE, ctl_symbols=CTLSYMBOLS):
    files = _get_text_file()
    command = f'--input={files} --model_prefix={prefix} --vocab_size={vocab_size} --control_symbols={ctl_symbols}'
    sp.SentencePieceTrainer.Train(command)


def main():
    train()


if __name__ == "__main__":
    main()
