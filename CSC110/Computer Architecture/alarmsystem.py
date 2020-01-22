# Evan Carnevale & Nick McCooey

import gates

def checkAlarmA1(sensors):
    if sensors[1]==1 and sensors[2]==1 and sensors[3] == 1:
        return True
    else:
        return False

def checkAlarmA0(sensors):
    if sensors[4]==1 or (sensors[0]==1 and sensors[1]==1):
        return True
    return False

def checkAlarmA2(sensors):
    if sensors[4]==1 and (sensors[5]==1 or sensors[6]==1):
        return True
    if sensors[4]==0 and (sensors[5]==1 and sensors[6]==1)
        return True
    return False
