import datetime
import winsound

def alarm(Timing):
    atime = str(datetime.datetime.now().strptime(Timing, "%I:%M %p"))
    atime = atime[11:-3]
    print(atime)

    realH = atime[:2]
    realH = int(realH)

    realmin = atime[3:5]
    realmin = int(realmin)

    print(f"Done alarm Set for {Timing}")

    while True:
        if realH==datetime.datetime.now().hour:
            if realmin==datetime.datetime.now().minute:
                print("Alarm is Running")
                winsound.PlaySound('time is running', winsound.SND_LOOP)
            elif realmin<datetime.datetime.now().minute:
                break

if __name__ == '__main__':
    alarm("3:46 PM")
