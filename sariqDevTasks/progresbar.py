from progressbar import ProgressBar
import time

pbar = ProgressBar(maxval=100)
pbar.start()

for i in range(1,101):
    pbar.update(i)
    time.sleep(0.5)

pbar.finish()