import sounddevice as sd
import matplotlib.pyplot as plt
from python_speech_features import mfcc
from scipy.cluster.vq import vq
from sklearn.cluster import KMeans
import numpy as np
from sklearn.metrics.cluster import (v_measure_score,completeness_score,homogeneity_score)


code=list()
f=open('dataset.txt','r')
for i in f.readlines():
    code.append(int(float(i)))
fc=16000
sd.default.samplerate=fc
duration=5 #sec
print 'Please speak'
myrecording=sd.rec(int(duration*fc),samplerate=fc,channels=1)
sd.wait()
mfcc_feat = mfcc(myrecording,fc)
kmeans=KMeans(n_clusters=10,random_state=0).fit(mfcc_feat)
codebook=kmeans.labels_
print codebook
vmeasurescore=v_measure_score(code,codebook)
completeness=completeness_score(code,codebook)
homogeneity=homogeneity_score(code,codebook)


print vmeasurescore,completeness,homogeneity
'''if score>0.5:
    print 'Hello, Harsha'
else:
    print 'I dont know who you are'
    print 'What is your name?'
    name=raw_input()
    np.savetxt(name+'dataset.txt',codebook)
'''

plt.figure()
plt.plot(myrecording)
plt.show()
