import hid
import time
import keyboard
from threading import Timer
 
VENDOR_ID = 0x07CA
PRODUCT_ID = 0x9850
 
# Max time between taps to count as part of same gesture (seconds)
TAP_THRESHOLD = 0.5
 
class TapDetector:
    def __init__(self, threshold=TAP_THRESHOLD):
        self.threshold = threshold
        self.count = 0
        self.timer = None
 
    def tap(self):
        self.count += 1
        if self.timer:
            self.timer.cancel()
 
        self.timer = Timer(self.threshold, self._handle_taps)
        self.timer.start()
 
    def _handle_taps(self):
        if self.count == 1:
            print("🎵 Single tap → Play/Pause")
            keyboard.send("play/pause media")
        elif self.count == 2:
            print("⏭️  Double tap → Next Track")
            keyboard.send("next track")
        elif self.count == 3:
            print("⏮️  Triple tap → Previous Track")
            keyboard.send("previous track")
        else:
            print(f"🤷 {self.count} taps — no action mapped.")
        self.count = 0
        self.timer = None
 
def main():
    dev = hid.device()
    dev.open(VENDOR_ID, PRODUCT_ID)
    dev.set_nonblocking(1)
    print("Press the button (1x=play, 2x=next, 3x=prev). Ctrl+C to quit.\n")
 
    detector = TapDetector()
    last_state = None
 
    try:
        while True:
            report = dev.read(8)
            if report:
                state = report[1]
                if state != last_state:
                    if state == 1:
                        detector.tap()
                    last_state = state
            time.sleep(0.01)
    except KeyboardInterrupt:
        print("\nExiting.")
    finally:
        dev.close()
 
if __name__ == "__main__":
    main()
 
