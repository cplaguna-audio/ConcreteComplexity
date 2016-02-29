import OSC
import time
import ConcreteComplexionScore

def sendScore(score, connection):
  print "Sending score."
  for note in score:
    sendNote(note, connection)
    note_time = float(note[-1]) * seconds_per_beat;
    time.sleep(note_time)

def sendNote(note, connection):
  # If single note.
  if(len(note) == 3):
    oscmsg = OSC.OSCMessage()
    oscmsg.setAddress("/mididata")
    oscmsg.append(note[0])
    oscmsg.append(note[1])
    connection.send(oscmsg)
  # If chord.
  elif(len(note) == 4):
    oscmsg = OSC.OSCMessage()
    oscmsg.setAddress("/mididata")
    oscmsg.append(note[0])
    oscmsg.append(note[2])
    connection.send(oscmsg)

    oscmsg = OSC.OSCMessage()
    oscmsg.setAddress("/mididata")
    oscmsg.append(note[1])
    oscmsg.append(note[2])
    connection.send(oscmsg)
  else:
    print 'Bad note.'

UDP_IP = "127.0.0.1"
UDP_PORT = 5000
ETHERNET_IP = "169.254.251.148"
ETHERNET_PORT = 51973
SHIMON_UDP_IP = "143.215.110.56"
SHIMON_UDP_PORT = 51973
SCORE = ConcreteComplexionScore.ShimonFullScore()
TEST_SCORE = ConcreteComplexionScore.ShimonTestScore()
TRUE_SHIMON = False

ETHERNET = True

BPM = 135.0;

seconds_per_beat = 60.0 / BPM;

c = OSC.OSCClient()

c.connect((ETHERNET_IP, ETHERNET_PORT)) 


while(True):
  print("Type spacebar to send score. Type x to exit.")
  user_input = raw_input();
  if(user_input == " "):
    sendScore(SCORE, c)
  elif(user_input == "x"):
    break;


