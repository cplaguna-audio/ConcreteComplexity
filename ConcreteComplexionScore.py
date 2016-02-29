from random import randint
from random import random
from random import seed

##############################
######### Utilities ##########
############################## 
def AddToArray(array, x):
  for idx in range(0, len(array)):
    array[idx] = array[idx] + x

def rotate(l,n):
    return l[n:] + l[:n]

def RandomNonUniform(dist):
  
  choice = random()
  # print choice
  cur_left = 0
  num_support = len(dist)
  for prob_idx in range(0, num_support):
    prob = dist[prob_idx]
    cur_right = cur_left + prob
    # print '[' + str(cur_left) + ',' + str(cur_right) + ']'
    if(cur_left <= choice and choice <= cur_right):
      return prob_idx
    cur_left = cur_right

  # If you didn't give a distribution that adds up to 1, you might not have 
  # chosen something yet. So just default to the most probable event.
  print 'Should have chosen something...'
  return dist.index(max(dist))
  
def GetShimonBounds():
  return [48, 88]

def IsOutOfRange(pitches):
  bounds = GetShimonBounds()
  for pitch in pitches:
    if(pitch < bounds[0]):
      return -1
    if(pitch > bounds[1]):
      return 1

  return 0

##############################
########## Rhythms ###########
############################## 
def PickMeasureRhythms(num_notes):
  if(num_notes == 1):
    choices = [[3], [-2, 1]]
    choice = RandomNonUniform([0.98, 0.02]);
    return choices[choice]
  if(num_notes == 2):
    choices = [[2, 1],
               [1, 2],
               [-1, 1, 1]]
    choice = RandomNonUniform([0.6, 0.38, 0.02]);
    return choices[choice]
  if(num_notes == 3):
    choices = [[1, 1, 1],
               [1.5, 0.5, 1],
               [2, 0.5, 0.5],
               [-1, 0.5, 0.5, 1]]          
    choice = RandomNonUniform([0.17, 0.45, 0.37, 0.01]);
    return choices[choice]
  if(num_notes == 4):
    choices = [[0.5, 0.5, 1, 1],
               [1, 0.5, 0.5, 1],
               [1, 1, 0.5, 0.5]]          
    choice = RandomNonUniform([0.45, 0.30, 0.15]);
    return choices[choice]
  if(num_notes == 5):
    choices = [[0.5, 0.5, 0.5, 0.5, 1],
               [1, 0.5, 0.5, 0.5, 0.5]]
    choice = RandomNonUniform([0.3, 0.7]);
    return choices[choice]
  if(num_notes == 6):
    choices = [[0.5, 0.5, 0.5, 0.5, 0.5, 0.5]]
    choice = RandomNonUniform([1]);
    return choices[choice]


##############################
########## Pitches ###########
############################## 
def GetScaleOffsets(scale):
  root = scale[0]
  mode = scale[1]

#  if(root == 'B' and mode == 'Min'):
#    offsets = [0, 2, 3, 5, 7, 9, 11]
#  elif(root == 'Bb' and mode == 'Min'):
#    offsets = [-1, 1, 2, 4, 6, 8, 10]
#  elif(root == 'A' and mode == 'Maj'):
#    offsets = [0, 2, 3, 5, 7, 9, 10]
#  elif(root == 'A' and mode == 'Dim'):
#    offsets =  [0, 1, 3, 4, 7, 8, 10]
#  elif(root == 'Ab' and mode == 'Maj'):
#    offsets =  [-1, 1, 2, 4, 6, 8, 9]
#  elif(root == 'D' and mode == 'Maj'):
#    offsets =  [0, 2, 3, 5, 7, 8, 10]
#  elif(root == 'Eb' and mode == 'Dim'):
#    offsets =  [-2, 1, 2, 4, 6, 7, 9]
#  elif(root == 'A' and mode == 'Min'):
#    offsets =  [0, 1, 3, 5, 7, 9, 10]
#  elif(root == 'F' and mode == 'Who'):
#    offsets =  [0, 1, 2, 4, 6, 8, 10]
#  elif(root == 'C' and mode == 'Maj'):
#    offsets =  [0, 1, 3, 5, 6, 8, 10]
#  elif(root == 'B' and mode == 'Maj'):
#    offsets =  [0, 2, 4, 5, 7, 9, 11]

  # Dorian.
  if(root == 'B' and mode == 'Min'):
    offsets = [0, 2, 3, 5, 7, 9, 10]

  # Dorian.
  elif(root == 'Bb' and mode == 'Min'):
    offsets = [-1, 1, 2, 4, 6, 8, 10]
  elif(root == 'A' and mode == 'Maj'):
    offsets = [0, 2, 3, 5, 7, 9, 10]
  elif(root == 'A' and mode == 'Dim'):
    offsets =  [0, 1, 3, 4, 7, 8, 10]

  # Sharp 11.
  elif(root == 'Ab' and mode == 'Maj'):
    offsets =  [-1, 1, 3, 4, 6, 8, 9]

  # Actually, dominant.
  elif(root == 'D' and mode == 'Maj'):
    offsets =  [0, 1, 3, 5, 7, 8, 10]
  elif(root == 'Eb' and mode == 'Dim'):
    offsets =  [-2, 1, 2, 4, 6, 7, 9]

  # Melodic minor.
  elif(root == 'A' and mode == 'Min'):
    offsets =  [0, 1, 3, 5, 7, 9, 10]
  elif(root == 'F' and mode == 'Who'):
    offsets =  [0, 1, 2, 4, 6, 8, 10]
  elif(root == 'C' and mode == 'Maj'):
    offsets =  [0, 1, 3, 5, 6, 8, 10]
  elif(root == 'B' and mode == 'Maj'):
    offsets =  [0, 2, 4, 5, 7, 9, 11]

  return offsets

def GetScaleRoot(scale):
  root = scale[0]
  mode = scale[1]
  if(root == 'B' and mode == 'Min'):
    return 0;
  elif(root == 'Bb' and mode == 'Min'):
    return 0;
  elif(root == 'A' and mode == 'Maj'):
    return 6;
  elif(root == 'A' and mode == 'Dim'):
    return 6;
  elif(root == 'Ab' and mode == 'Maj'):
    return 6;
  elif(root == 'D' and mode == 'Maj'):
    return 2;
  elif(root == 'Eb' and mode == 'Dim'):
    return 3;
  elif(root == 'A' and mode == 'Min'):
    return 6;
  elif(root == 'F' and mode == 'Who'):
    return 4;
  elif(root == 'C' and mode == 'Maj'):
    return 1;
  elif(root == 'B' and mode == 'Maj'):
    return 0;
  return -1;

def GetContourTypes():
  countours = ['straight', 'up', 'down', 'up_down', 'down_up']
  return countours

def GetSoloStyles():
  styles = ['arpeggio', 'continuous', 'jump']
  return styles

def RootDegreeToMidi(root_degree, scale):
  octave = root_degree / 7
  
  normalized_degree = root_degree - (octave * 7)
  
  scale_offsets = GetScaleOffsets(scale);
  cur_offset = scale_offsets[normalized_degree]

  normalized_midi = 71 + cur_offset
  root_midi = normalized_midi + (octave * 12)
  # print 'Root degree: ' + str(root_degree)
  # print 'Midi: ' + str(root_midi) + ', octave: ' + str(octave)
  return root_midi

def MidiToRootDegree(midi):
  # print 'Midi to root degree: ' + str(midi)
  offset = midi - 71

  octave = offset / 12
  offset = offset % 12

  if(offset < 2):
    root_degree = 0
  elif(offset < 4):
    root_degree = 1
  elif(offset < 5):
    root_degree = 2
  elif(offset < 7):
    root_degree = 3
  elif(offset < 9):
    root_degree = 4
  elif(offset < 11):
    root_degree = 5
  else:
    root_degree = 6

#  print 'octave: ' + str(octave)
 # print 'degree: ' + str(root_degree)

  root_degree = root_degree + (octave * 7)
  #print 'final: ' + str(root_degree)
  return root_degree

def ChooseClosestChordTone(root_degree, scale):
  choices = [0, 2, 4, 7]
  scale_root_degree = GetScaleRoot(scale)
  AddToArray(choices, scale_root_degree)

  while(root_degree > choices[-1]):
    AddToArray(choices, 7)

  while(root_degree < choices[0]):
    AddToArray(choices, -7)

  distances = [0, 0, 0, 0]
  for idx in range(0, 4):
    distances[idx] = abs(root_degree - choices[idx])

  choice_idx = distances.index(min(distances))

  cur_choice = choices[choice_idx]
  cur_choice_midi = RootDegreeToMidi(cur_choice, scale)
  bounds = GetShimonBounds()
  if(cur_choice_midi < bounds[0]):
    cur_choice = cur_choice + 7
  if(cur_choice_midi > bounds[1]):
    cur_choice = cur_choice - 7

  return cur_choice
  
def ChooseClosestSixOrNine(root_degree, scale):
  choices = [1, 5]
  scale_root_degree = GetScaleRoot(scale)
  AddToArray(choices, scale_root_degree)

  while(root_degree > choices[-1]):
    AddToArray(choices, 7)

  while(root_degree < choices[0]):
    AddToArray(choices, -7)

  distances = [0, 0]
  for idx in range(0, 2):
    distances[idx] = abs(root_degree - choices[idx])

  choice_idx = distances.index(min(distances))

  cur_choice = choices[choice_idx]
  cur_choice_midi = RootDegreeToMidi(cur_choice, scale)
  bounds = GetShimonBounds()
  if(cur_choice_midi < bounds[0]):
    cur_choice = cur_choice + 7
  if(cur_choice_midi > bounds[1]):
    cur_choice = cur_choice - 7

  return cur_choice

def ChooseClosestFiveSevenOrNine(root_degree, scale):
  choices = [4, 6, 8]
  scale_root_degree = GetScaleRoot(scale)
  AddToArray(choices, scale_root_degree)

  while(root_degree > choices[-1]):
    AddToArray(choices, 7)

  while(root_degree < choices[0]):
    AddToArray(choices, -7)

  distances = [0, 0]
  for idx in range(0, 2):
    distances[idx] = abs(root_degree - choices[idx])

  choice_idx = distances.index(min(distances))
  cur_choice = choices[choice_idx]
  cur_choice_midi = RootDegreeToMidi(cur_choice, scale)
  bounds = GetShimonBounds()
  if(cur_choice_midi < bounds[0]):
    cur_choice = cur_choice + 7
  if(cur_choice_midi > bounds[1]):
    cur_choice = cur_choice - 7


  return cur_choice


def PickFirstNote(prev_root_degree, rhythms, style, contour, scale):
  num_notes = len(rhythms)
  if(style == 'continuous' or 'jump'):
    first_note = ChooseClosestChordTone(prev_root_degree, scale)
  elif(style == 'arpeggio'):
    if(contour == 'down' and num_notes > 3):
      first_note = ChooseClosestFiveSevenOrNine(prev_root_degree, scale)
    else:
      first_note = ChooseClosestChordTone(prev_root_degree, scale)
  else:
    print 'Bad style from PickFirstNote'


  return first_note


def PickMeasurePitches(rhythms, scale, style, contour, previous_note):
  num_notes = len(rhythms)
  pitches = []

  prev_root_degree = MidiToRootDegree(previous_note)

  first_note_root_degree = PickFirstNote(prev_root_degree, rhythms, style, contour, scale)

  if(style == 'arpeggio'):
    root_degrees = ArpeggioMeasure(rhythms, first_note_root_degree, contour)
  elif(style == 'continuous'):
    root_degrees = ContinuousScalesMeasure(rhythms, first_note_root_degree, contour)
  elif(style == 'jump'):
    root_degrees = JumpMeasure(rhythms, first_note_root_degree, contour)
  else:
    print 'Bad Style (lol). ' + style

  for note_idx in range(0, num_notes):
    choice_root_degree = root_degrees[note_idx]
    choice_midi = RootDegreeToMidi(choice_root_degree, scale)
    pitches = pitches + [choice_midi]
  

  return pitches

def ArpeggioMeasure(rhythms, first_root_degree, contour):
  num_notes = len(rhythms)
  cur_degree = first_root_degree
  degrees = []

  deltas = []
  if(contour == 'up'):
    for note_idx in range(0, num_notes):
      deltas = deltas + [2]
  elif(contour == 'down'):
    for note_idx in range(0, num_notes):
      deltas = deltas + [-2]
  elif(contour == 'straight'):
    if(num_notes == 2):
      choice = randint(0, 1);
      if(choice == 0):
        deltas = [0, 2]
      else:
        deltas = [0, -2]

    elif(num_notes == 3):
      choice = randint(0, 3)
      if(choice == 0):
        deltas = [0, 2, -2]
      elif(choice == 1):
        deltas = [0, -2, 2]
      elif(choice == 2):
        deltas = [0, 0, -2]
      else:
        deltas = [0, 0, 2]

    elif(num_notes == 4):
      choice = randint(0, 2)
      if(choice == 0):
        deltas = [0, 2, 2, -2]
      elif(choice == 1):
        deltas = [0, 4, -2, -2]
      else:
        deltas = [0, 4, -2, 2]

    elif(num_notes == 5):
      choice = randint(0, 3)
      if(choice == 0):
        deltas = [0, 2, 2, -2, -2]
      elif(choice == 1):
        deltas = [0, 2, 2, -2, 2]
      elif(choice == 2):
        deltas = [0, 4, -2, -2, 2]
      else:
        deltas = [0, 4, -2, 2, -2]

    elif(num_notes == 6):
      choice = randint(0, 2)
      if(choice == 0):
        deltas = [0, 2, 2, -2, 2, -2]
      elif(choice == 1):
        deltas = [0, 2, 2, -2, -2, 2]
      elif(choice == 2):
        deltas = [0, 4, -2, 2, -2, 2]
      else:
        deltas = [0, 4, -2, 2, -4, 2]

    else:
      for note_idx in range(0, num_notes):
        cur_delta = 2;
        if(note_idx % 2 == 1):
          cur_delta = -2
        deltas = deltas + [cur_delta]

  elif(contour == 'up_down'):

    if(num_notes > 3):
      switch_idx = randint(1, num_notes - 1)
      for note_idx in range(0, num_notes):
        cur_delta = 2;
        if(note_idx > switch_idx):
          cur_delta = -2
        deltas = deltas + [cur_delta]
    else:
      for note_idx in range(0, num_notes):
        cur_delta = 2;
        if(note_idx > num_notes / 2):
          cur_delta = -2
        deltas = deltas + [cur_delta]
  elif(contour == 'down_up'):
    if(num_notes > 3):
      switch_idx = randint(1, num_notes - 1)
      for note_idx in range(0, num_notes):
        cur_delta = -2;
        if(note_idx > switch_idx):
          cur_delta = 2
        deltas = deltas + [cur_delta]
    else:
      for note_idx in range(0, num_notes):
        cur_delta = -2;
        if(note_idx > num_notes / 2):
          cur_delta = 2
        deltas = deltas + [cur_delta]

  deltas[0] = 0
  for note_idx in range(0, num_notes):
    if(rhythms[note_idx] > 0):
      cur_degree = cur_degree + deltas[note_idx]

    degrees = degrees + [cur_degree]
  return degrees

def ContinuousScalesMeasure(rhythms, first_root_degree, contour):
  num_notes = len(rhythms)
  cur_degree = first_root_degree
  degrees = []

  deltas = []
  if(contour == 'up'):
    for note_idx in range(0, num_notes):
      deltas = deltas + [1]
  elif(contour == 'down'):
    for note_idx in range(0, num_notes):
      deltas = deltas + [-1]
  elif(contour == 'straight'):
    for note_idx in range(0, num_notes):
      cur_delta = 1;
      if(note_idx % 2 == 1):
        cur_delta = -1
      deltas = deltas + [cur_delta]
  elif(contour == 'up_down'):
    for note_idx in range(0, num_notes):
      cur_delta = 1;
      if(note_idx > num_notes / 2):
        cur_delta = -1
      deltas = deltas + [cur_delta]
  elif(contour == 'down_up'):
    for note_idx in range(0, num_notes):
      cur_delta = -1;
      if(note_idx > num_notes / 2):
        cur_delta = 1
      deltas = deltas + [cur_delta]

  deltas[0] = 0
  for note_idx in range(0, num_notes):
    if(rhythms[note_idx] > 0):
      cur_degree = cur_degree + deltas[note_idx]
    degrees = degrees + [cur_degree]

  return degrees

def JumpMeasure(rhythms, first_root_degree, contour):
  num_notes = len(rhythms)
  cur_degree = first_root_degree
  degrees = []

  if(num_notes < 6):
    jump_idx = rhythms.index(max(rhythms)) + 1
    if(jump_idx >= num_notes):
      jump_idx = randint(0, num_notes - 1)
  else:
    jump_idx = randint(0,5)

  jump_amt = randint(2, 7)

  deltas = []
  if(contour == 'up'):
    for note_idx in range(0, num_notes):
      if(note_idx < jump_idx):
        deltas = deltas + [1]
      elif(note_idx == jump_idx):
        deltas = deltas + [jump_amt]
      else:
        deltas = deltas + [-1]
  elif(contour == 'up_down'):
    for note_idx in range(0, num_notes):
      if(note_idx < jump_idx):
        deltas = deltas + [-1]
      elif(note_idx == jump_idx):
        deltas = deltas + [jump_amt]
      else:
        deltas = deltas + [-1]

  elif(contour == 'down'):
    for note_idx in range(0, num_notes):
      if(note_idx < jump_idx):
        deltas = deltas + [-1]
      elif(note_idx == jump_idx):
        deltas = deltas + [-1 * jump_amt]
      else:
        deltas = deltas + [1]
  else:
    for note_idx in range(0, num_notes):
      if(note_idx < jump_idx):
        deltas = deltas + [1]
      elif(note_idx == jump_idx):
        deltas = deltas + [-1 * jump_amt]
      else:
        deltas = deltas + [1]

  deltas[0] = 0
  for note_idx in range(0, num_notes):
    if(rhythms[note_idx] > 0):
      cur_degree = cur_degree + deltas[note_idx]

    degrees = degrees + [cur_degree]
  return degrees

def PickContour(prev_pitch):
  bounds = GetShimonBounds()
  low_bound = bounds[0]
  high_bound = bounds[1]
  if(prev_pitch - low_bound < 5):
    return 'up'
  if(high_bound - prev_pitch < 5):
    return 'down'

  contours = GetContourTypes()
  contour_dist = [0.2, 0.25, 0.1, 0.25, 0.2]
  contour_choice = RandomNonUniform(contour_dist)
  return contours[contour_choice]

def PickStyle(cur_contour):
  # [arpeggio, continuous, jump]
  styles = GetSoloStyles()

  style_dist = []
  if(cur_contour == 'up' or cur_contour == 'down'):
    style_dist = [0.15, 0.6, 0.25]
  elif(cur_contour == 'up_down' or cur_contour == 'down_up'):
    style_dist = [0.2, 0.45, 0.35]
  else:
    style_dist = [0.25, 0.7, 0.15]

  style_choice = RandomNonUniform(style_dist)
  return styles[style_choice]

##############################
########### Score ############
############################## 
def ShimonTestScore():
  score = []
  score = score + ShimonPartBSolo(randint(60, 75), 0)
  last_note = score[-1][0]
  score = score + ShimonPartBSolo(last_note, 1)
  last_note = score[-1][0]
  score = score + ShimonPartBSolo(last_note, 2)

  score = score + ShimonPartC()
  score = score + ShimonPartD()

  return score

def ShimonFullScore():

  score = ShimonPartA(8) 

  score = score + ShimonPartBAccompaniment() + ShimonPartBAccompaniment()
  score = score + ShimonPartBSolo(randint(60, 75), 1)
  last_note = score[-1][0]
  score = score + ShimonPartBSolo(last_note, 2)

  score = score + ShimonPartC()
  score = score + ShimonPartD()

  return score

def ShimonPartA(num_times):
  low_measure = [[53, 126, 0.5],
                 [57, 126, 0.5],
                 [59, 126, 0.5], 
                 [63, 126, 0.5],
                 [61, 126, 1]]

  high_measure = [[74, 126, 0.5],
                 [66, 126, 0.5],
                 [70, 126, 0.5], 
                 [73, 126, 0.5],
                 [71, 126, 1]]

  measure = [[74, 53, 126, 0.5],
             [66, 57, 126, 0.5],
             [70, 59, 126, 0.5], 
             [73, 63, 126, 0.5],
             [71, 61, 126, 1]]
  score = []
  score = score + high_measure + [[0, 0, 3]] + low_measure + [[0, 0, 3]]
  score = score + high_measure + [[0, 0, 1]] + low_measure + [[0, 0, 1]]

  for i in range(0, num_times):
    score = score + measure
  return score

def ShimonPartBAccompaniment():

  score = [[59, 126, 1],
           [66, 74, 126, 1],
           [66, 74, 126, 1],

           [58, 126, 1],
           [65, 73, 126, 1],
           [65, 73, 126, 1],

           [57, 126, 1],
           [64, 73, 126, 1],
           [64, 73, 126, 1],

           [57, 126, 1],
           [63, 72, 126, 1],
           [63, 72, 126, 1],

           [56, 126, 1],
           [63, 72, 126, 1],
           [63, 72, 126, 1],

           [54, 126, 1],
           [62, 66, 126, 1],
           [62, 66, 126, 1],

           [51, 126, 1],
           [57, 66, 126, 1],
           [57, 66, 126, 1],

           [50, 126, 1],
           [57, 66, 126, 1],
           [57, 66, 126, 1],

           [57, 126, 1],
           [64, 72, 126, 1],
           [64, 72, 126, 1],

           [56, 126, 1],
           [64, 72, 126, 1],
           [64, 72, 126, 1],

           [54, 126, 1],
           [62, 69, 126, 1],
           [62, 69, 126, 1],

           [53, 126, 1],
           [61, 69, 126, 1],
           [61, 69, 126, 1],

           [60, 126, 1],
           [67, 71, 126, 1],
           [67, 71, 126, 1],

           [55, 126, 1],
           [67, 71, 126, 1],
           [67, 71, 126, 1],

           [59, 126, 1],
           [66, 70, 126, 1],
           [66, 70, 126, 1],

           [54, 126, 1],
           [66, 70, 126, 1],
           [66, 70, 126, 1],

           ]

  score = [[59, 126, 1],
           [54, 62, 126, 1],
           [54, 62, 126, 1],

           [58, 126, 1],
           [53, 61, 126, 1],
           [53, 61, 126, 1],

           [57, 126, 1],
           [52, 61, 126, 1],
           [52, 61, 126, 1],

           [57, 126, 1],
           [51, 60, 126, 1],
           [51, 60, 126, 1],

           [56, 126, 1],
           [51, 60, 126, 1],
           [51, 60, 126, 1],

           [54, 126, 1],
           [50, 54, 126, 1],
           [50, 54, 126, 1],

           [51, 126, 1],
           [57, 66, 126, 1],
           [57, 66, 126, 1],

           [50, 126, 1],
           [57, 66, 126, 1],
           [57, 66, 126, 1],

           [57, 126, 1],
           [52, 60, 126, 1],
           [52, 60, 126, 1],

           [56, 126, 1],
           [52, 60, 126, 1],
           [52, 60, 126, 1],

           [54, 126, 1],
           [50, 57, 126, 1],
           [50, 57, 126, 1],

           [53, 126, 1],
           [49, 57, 126, 1],
           [49, 57, 126, 1],

           [60, 126, 1],
           [55, 59, 126, 1],
           [55, 59, 126, 1],

           [55, 126, 1],
           [55, 59, 126, 1],
           [55, 59, 126, 1],

           [59, 126, 1],
           [54, 58, 126, 1],
           [54, 58, 126, 1],

           [54, 126, 1],
           [54, 58, 126, 1],
           [54, 58, 126, 1],

           ]
           
  return score

def ShimonPartBSolo(very_first_pitch, dist_choice):
  seed()
  score = []
  PROGRESSION = [['B', 'Min'],
                 ['Bb', 'Min'],
                 ['A', 'Maj'],
                 ['A', 'Dim'],
                 ['Ab', 'Maj'],
                 ['D', 'Maj'],
                 ['Eb', 'Dim'],
                 ['D', 'Maj'],
                 ['A', 'Min'],
                 ['A', 'Min'],
                 ['D', 'Maj'],
                 ['F', 'Who'],
                 ['C', 'Maj'],
                 ['C', 'Maj'],
                 ['B', 'Maj'],
                 ['B', 'Maj']]
  slow_dist = [0.1, 0.20, 0.4, 0.20, 0.1, 0.0]
  med_dist = [0.05, 0.10, 0.20, 0.3, 0.2, 0.15]
  fast_dist = [0.03, 0.05, 0.15, 0.22, 0.22, 0.33]

  if(dist_choice == 0):
    dist = slow_dist
  elif(dist_choice == 1):
    dist = med_dist
  elif(dist_choice == 2):
    dist = fast_dist

  previous_pitch = very_first_pitch;

  for measure_scale in PROGRESSION:
    num_notes = RandomNonUniform(dist) + 1
    rhythms = PickMeasureRhythms(num_notes)

    cur_contour = PickContour(previous_pitch)
    cur_style = PickStyle(cur_contour)

    pitches = PickMeasurePitches(rhythms, measure_scale, cur_style, cur_contour, previous_pitch)

    in_range = IsOutOfRange(pitches)
    while(in_range != 0):
      if(in_range == -1):
        cur_countour = 'up'
      if(in_range == 1):
        cur_countour = 'down'

      cur_style = PickStyle(cur_contour)
      pitches = PickMeasurePitches(rhythms, measure_scale, cur_style, cur_contour, previous_pitch)
      in_range = IsOutOfRange(pitches)
      print 'pitches: ' + str(pitches)

    num_notes_and_rests = len(rhythms)
    for note_idx in range(0, num_notes_and_rests):
      pitch = pitches[note_idx]
      rhythm = rhythms[note_idx]
      if(rhythm > 0):
        amplitude = 127
      else:
        amplitude = 0
        rhythm = rhythm * -1
      note = [pitch, amplitude, rhythm]
      score = score + [note]

    previous_pitch = pitches[-1]
  return score

def ShimonPartBPrecomposed():
  score = [[0, 0, 1],
         [74, 126, 0.5],
         [76, 126, 0.5],
         [78, 126, 1],

         [0, 0, 1],
         [73, 126, 0.5],
         [75, 126, 0.5],
         [77, 126, 1],

         [0, 0, 1],
         [73, 126, 0.5],
         [74, 126, 0.5],
         [76, 126, 0.5],
         [78, 126, 0.5],

         [80, 126, 1],
         [81, 126, 1],
         [83, 126, 1],

         [84, 126, 3],

         [81, 126, 3],

         [0, 0, 2],
         [81, 126, 1],

         [78, 126, 2.5],
         [76, 126, 0.5],

         [76, 126, 3],

         [74, 126, 3],

         [74, 126, 0.5],
         [72, 126, 0.5],
         [74, 126, 0.5],
         [76, 126, 0.5],  
         [74, 126, 0.5],
         [72, 126, 0.5],

         [73, 126, 3],

         [74, 126, 6],

         [75, 126, 6]]
  return score

def ShimonPartC():
   return [[59, 126, 1],
           [66, 75, 126, 1],
           [66, 75, 126, 1],

           [54, 126, 1],
           [66, 75, 126, 1],
           [66, 75, 126, 1],
           
           [55, 126, 1],
           [62, 71, 126, 1],
           [62, 71, 126, 1],

           [59, 126, 1],
           [62, 71, 126, 1],
           [62, 71, 126, 1],
           
           [50, 126, 1],
           [57, 66, 126, 1],
           [50, 126, 1],
           
           [51, 126, 1],
           [58, 66, 126, 2],

           [51, 126, 1],
           [58, 67, 126, 1],
           [51, 126, 1],
           
           [50, 126, 1],
           [57, 66, 126, 1],
           [54, 126, 1],

           [55, 126, 1],
           [62, 71, 126, 1],
           [62, 71, 126, 1],

           [62, 126, 1],
           [62, 71, 126, 1],
           [62, 71, 126, 1],

           [58, 126, 1],
           [67, 70, 126, 1],
           [67, 70, 126, 1],

           [63, 126, 1],
           [67, 70, 126, 1],
           [67, 70, 126, 1],

           [66, 126, 3],
           [66, 126, 1],
           [66, 126, 3],
           [66, 126, 1]
           ]

def ShimonPartD():
  score = [[59, 70, 126, 0.5],
         [71, 126, 0.5],
         [73, 126, 0.5],
         [74, 126, 0.5],
         [78, 126, 0.5],
         [76, 126, 0.5],

         [53, 69, 126, 0.5],
         [73, 126, 0.5],
         [77, 126, 0.5],
         [78, 126, 0.5],
         [80, 126, 1],

         [52, 81, 126, 1],
         [73, 126, 1],
         [71, 126, 1],

         [51, 126, 0.5],
         [72, 126, 0.5],
         [66, 126, 0.5],
         [70, 126, 0.5],
         [69, 126, 0.5],
         [67, 126, 0.5],

         [60, 66, 126, 0.5],
         [67, 126, 0.5],
         [69, 126, 0.5],
         [70, 126, 0.5],
         [74, 126, 0.5],
         [76, 126, 0.5],

         [58, 78, 126, 1],
         [74, 126, 1],
         [70, 126, 1],

         [60, 66, 126, 0.5],
         [67, 126, 0.5],
         [69, 126, 0.5],
         [70, 126, 0.5],
         [74, 126, 0.5],
         [76, 126, 0.5],

         [58, 78, 126, 1],
         [79, 126, 1],
         [78, 126, 1],

         [59, 70, 126, 0.5],
         [71, 126, 0.5],
         [73, 126, 0.5],
         [74, 126, 0.5],
         [78, 126, 0.5],
         [76, 126, 0.5],

         [53, 69, 126, 0.5],
         [73, 126, 0.5],
         [77, 126, 0.5],
         [78, 126, 0.5],
         [80, 126, 1],

         [52, 81, 126, 1],
         [73, 126, 1],
         [71, 126, 1],

         [51, 126, 0.5],
         [72, 126, 0.5],
         [66, 126, 0.5],
         [70, 126, 0.5],
         [69, 126, 0.5],
         [67, 126, 0.5],

         [60, 66, 126, 0.5],
         [67, 126, 0.5],
         [69, 126, 0.5],
         [70, 126, 0.5],
         [74, 126, 0.5],
         [76, 126, 0.5],

         [58, 78, 126, 1],
         [74, 126, 1],
         [70, 126, 1],

         [60, 66, 126, 0.5],
         [67, 126, 0.5],
         [69, 126, 0.5],
         [70, 126, 0.5],
         [74, 126, 0.5],
         [76, 126, 0.5],

         [58, 78, 126, 1],
         [54, 79, 126, 1],
         [78, 126, 1],

         [51, 126, 1],
         [79, 126, 1],
         [78, 126, 1],

         [54, 126, 1],
         [79, 126, 1],
         [78, 126, 1],

         [51, 70, 126, 1],
         [50, 70, 126, 2],

         [60, 126, 3],
         [60, 126, 3],

         [52, 126, 3],
         [52, 126, 3],

         [53, 126, 3],
         [53, 126, 3]

         ]

  return score
