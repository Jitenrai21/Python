import time

startTime = time.time()
lastTime = startTime
lapNum = 1

print('Press ENTER to start the lap timer.\nPress CTRL+C to stop.')

try:
    while True:
        input()
        lapTime = round((time.time()-lastTime), 2)
        totalTime = round((time.time()-startTime), 2)

        print('The lap number is:',str(lapNum))
        print('The lap time is:',str(lapTime))
        print('Total time is:', str(totalTime))

        print('*'*20)

        lapNum += 1
        lastTime = time.time()
except KeyboardInterrupt:
    print('Done!')