import OSC

UDP_IP = "127.0.0.1"
UDP_PORT = 5000

# "128.16.127.104"
SHIMON_UDP_IP = "143.215.110.56" # "38.110.16.157"
SHIMON_UDP_PORT = 51973

c = OSC.OSCClient()
c.connect((UDP_IP, UDP_PORT)) 

oscmsg = OSC.OSCMessage()
oscmsg.setAddress("/mididata")
oscmsg.append(60)
oscmsg.append(126)
c.send(oscmsg)
