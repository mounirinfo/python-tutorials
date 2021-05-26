import librosa
#import IPython.display as ipd
import matplotlib.pyplot as plt
#ipd.Audio('Enregistrement.wav')
data,sampling_rate=librosa.load('Enregistrement.wav')
print(sampling_rate)
plt.figure(figsize=(12,4))
librosa.display.waveplot(data, sr=sampling_rate)
