import io
import numpy as np
import wave
import whisper
from xoxxox.shared import Custom

#---------------------------------------------------------------------------

class SttPrc():

  def __init__(self, config="xoxxox/config_sttwsp_000", **dicprm):
    diccnf = Custom.update(config, dicprm)
    self.nmodel = whisper.load_model(diccnf["nmodel"])
    self.lngtgt = diccnf["lngtgt"]

  def infere(self, datwav):
    dicres = self.nmodel.transcribe(self.cnvnpy(datwav), language=self.lngtgt)
    return dicres["text"]

  def cnvnpy(self, datwav):
    with io.BytesIO(datwav) as b:
      with wave.open(b, "rb") as f:
        n = f.getnframes()
        r = f.readframes(n)
        datnpy = np.frombuffer(r, dtype=np.int16).copy()
        datnpy = (datnpy / 32768.0).astype(np.float32)
        if f.getnchannels() == 2:
          datnpy = datnpy.reshape(-1, 2).mean(axis=1)
    return datnpy
