from typing import Optional
from espnet2.bin.tts_inference import Text2Speech
from espnet2.utils.types import str_or_none


class TTSModel(object):
    """
    Wrapper for Text2Speech Model
    """
    model: Text2Speech

    def __call__(self, text: str):
        # load sholud be called before
        return self.model(text)

    async def load(self, model_path, device):
        self.model = await load_model(model_path=model_path, device=device)


async def load_model(model_path: Optional[str], device: str = 'cpu') -> Text2Speech:
    if model_path is None:
        model = Text2Speech.from_pretrained(
            model_tag="imdanboy/kss_tts_train_jets_raw_phn_null_g2pk_train.total_count.ave",
            vocoder_tag=str_or_none("none"),
            device=device
        )
    else:
        model = Text2Speech.from_pretrained(
            model_file=model_path,
            vocoder_tag=str_or_none("none"),
            device=device
        )
    return model