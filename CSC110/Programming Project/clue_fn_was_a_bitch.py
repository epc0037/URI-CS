#Best Version so far
def generateClueList(random_color_list, guess):
    Clue_List = []
    for i in range(len(guess)):
        if guess[i] == random_color_list[i] and 2 not in Clue_List:
            Clue_List += [2]
            random_color_list[i] == 'MATCH'
            if guess[i] != random_color_list[i] and guess[i] in random_color_list:
                Clue_List += [1]
    return Clue_List



# Natalie Spatharakis
def generateClueList(random_color_list, guess):

    #new list for writing clues
    Clue_List = []
    # temp list to alter color list without changing it
    temp_list = [-1,-1,-1,-1]
    # loop through length of list...
    for i in range(len(random_color_list)):
        # add each to temp
        temp_list[i] = random_color_list[i]
        print(temp_list[i])
    # looping through color list...
    for i in range(len(random_color_list)):
        
        for j in range((len(random_color_list))):
            # if the guess is anywhere in color list...
            print(guess[i],"compared to ",temp_list[j])
            if guess[i] ==  temp_list[j]:
                # if they are in the same position..
                if i == j and 2 not in Clue_List:
                    # add a 2 to the clue list
                    Clue_List += [2]
                    # don't match this one again
                    temp_list[j] = '-1'
                    print(guess[i],temp_list[j])
                # if not the same position..
                if i != j and 1 not in Clue_List:
                    # add 1
                    Clue_List += [1]
                    print(guess[i],temp_list[j])
                    
    return Clue_List






#Original
def generateClueList(random_color_list, guess):
    Clue_List = []
    i = 0
    while (i < 4):
        if guess[i] in random_color_list and guess[i] == random_color_list[i] and 2 not in Clue_List :
            Clue_List += [2]
        i +=1
    i = 0
    while (i < 4):
        if guess[i] in random_color_list and guess[i] != random_color_list[i] and 1 not in Clue_List:
            Clue_List += [1]
        i = i + 1
    return Clue_List
