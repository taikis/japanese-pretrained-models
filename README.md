
# old-japanese-pretrained-models 

This is a fork of https://github.com/rinnakk/japanese-pretrained-models

[train-sentencepiece.py](./src/old_japanese/train_sentencepiece.py) is from https://github.com/yoheikikuta/bert-japanese  
Copylight (c) 2020 @yoheikikuta  
Apache-2.0 license

## Usage

### 1 Download text data

```bash
python -m corpus.old_japanese.download_shaped_text
```

### 2 Train SentencePiece model

```bash
python -m corpus.old_japanese.train_sentencepiece
```

### 3 