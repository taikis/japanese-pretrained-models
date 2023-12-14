
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

### 3 Train BERT model

```bash
CUDA_VISIBLE_DEVICES=0 python -m task.pretrain_roberta.train \
    --n_gpus 1 \
    --save_model True \
    --enable_log True \
    --model_size base \
    --model_config_filepath model/roberta-ja-base-config.json \
    --batch_size 32 \
    --eval_batch_size 32 \
    --n_training_steps 3000000 \
    --n_accum_steps 16 \
    --init_lr 0.0006
```