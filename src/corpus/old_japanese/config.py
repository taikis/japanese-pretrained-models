class Config(object):
    def __init__(self):
        # DATA configuration
        self.data_dir = "../data/"
        self.text_dir = "../data/old_japanese/"

        # SENTENCEPIECE configuration
        self.sp_prefix = "../data/tokenizer/old_japanese"
        self.vocab_size = 32000
        self.ctl_symbols = "[PAD],[CLS],[SEP],[MASK]"
