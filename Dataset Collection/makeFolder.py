import os
import numpy as np

DATA_PATH = os.getcwd()
# ---------------------setting up folders---------------------------------##


# Path for exported data, numpy arrays


# Actions that we try to detect
actions = np.array(['who', 'what', 'when', 'where', 'why',
                   'how', 'hello', 'phone', 'i', 'you', 'your', 'my'])

# Thirty videos worth of data
# no_sequences = 10

# Videos are going to be 30 frames in length
# sequence_length = 30

for action in actions:
    try:
        os.makedirs(os.path.join(
            DATA_PATH, "ACTIONS", action))
        os.makedirs(os.path.join(
            DATA_PATH, "ACTIONS", action, action+"_label"))
    except:
        pass
# for action in actions:
#     for sequence in range(no_sequences):
#         try:
#             os.makedirs(os.path.join(
#                 DATA_PATH, "ACTIONS", action, str(sequence)))
#         except:
#             pass


# ---------------------setting up folders---------------------------------##
