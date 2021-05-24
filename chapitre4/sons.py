import librosa.display
import IPython.display as ipd
import matplotlib.pyplot as plt
ipd.audio('Enregistrement.wav')
data,sampling_rate=librosa.load('nregistrement.wav')
print(sampling_rate)
plt.figure(figsize=(12.4))
librosa.display.waveplot(data, sr=sampling_rate)
