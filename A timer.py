import time

def wait(scds):
      time.sleep(scds)

running = True
minutes = 0
seconds = 0

while running:
      try:
            minutes = int(input("Please enter the minutes: "))
      except ValueError:
            print("Please print an appropiate value for minutes.")
            wait(1)
            print("Make sure it is between 0 and 10, inclusive.")
            print()
            wait(1)
      else:
            if not (0 <= minutes <= 10):
                  print("Please enter a number between 0 and 10, inclusive.")
                  print()
                  wait(1)
            else:
                  running = False


running = True

while running:
      try:
            seconds = int(input("Please enter the seconds: "))
      except ValueError:
            print("Please print an appropiate value for minutes.")
            wait(1)
            print("Make sure it is between 0 and 10, inclusive.")
            print()
            wait(1)
      else:
            if not (0 <= minutes <= 59):
                  print("Please enter a number between 0 and 59, inclusive.")
                  print()
                  wait(1)
            else:
                  running = False


while minutes > 0 or seconds > 0:
      if seconds == 0:
            minutes -= 1
            seconds = 59
      else:
            seconds -= 1

      displaySeconds = ""

      if seconds < 10:
            displaySeconds = "0" + str(seconds)
      else:
            displaySeconds = str(seconds)
            
      print(str(minutes)+":"+displaySeconds)
            
      wait(1)

