class Config(object):
    def __init__(self):
        self.corpus_name = "old_japanese"
        # DATA configuration
        self.data_dir = "../data/"
        self.text_dir = "../data/old_japanese/"
        self.data_url = "https://github.com/taikis/koten-text/releases/download/1.0/shaped-text.zip"

        # SENTENCEPIECE configuration
        self.sp_prefix = "../data/tokenizer/old_japanese"
        self.vocab_size = 32000
        self.ctl_symbols = "[PAD],[CLS],[SEP],[MASK]"

        # Management
        self.raw_data_dir = "../data/old_japanese/raw_data"
        self.doc_data_dir = "../data/old_japanese/doc_data"