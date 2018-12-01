# !/usr/bin/env python
# coding:utf-8

import numpy as np
import matplotlib.pyplot as plt

px = np.arange(0.001,1.0,0.001)
log0 = -np.log(px)
log1 = -(1-px)*np.log(px)
log2 = -np.power((1-px),2)*np.log(px)

plt.figure(1,[8,6])
plt.plot(px,log0,label="$\gamma$ = 0")
plt.plot(px,log1,label="$\gamma$ = 1")
plt.plot(px,log2,label="$\gamma$ = 2")

plt.xlabel("probability of ground truth class")
plt.ylabel("loss")

plt.xlim(0,1)
plt.ylim(0,5)

plt.annotate("$CE(p_t) = -log(p_t)$",[0.2,3])
plt.annotate("$FL(p_t) = -(1-p_t)^{\gamma}log(p_t)$",[0.2,2.75])

plt.legend()
plt.show()