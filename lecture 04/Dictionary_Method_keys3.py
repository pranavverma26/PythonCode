#      DICTIONARY METHODS

    # 1. Key  :-   Returns all keys.

info ={
    "key" : "value",
    "Name": "Pranav",
    "subjects" : {
        "phy" : 84,
        "maths" : 88,
    14 : ("a","b","c","d")
    }
}

print(info.keys())   # We did't get nested keys.  output = dict_keys(['key', 'Name', 'subjects'])

print(list(info.keys()))   # now after type casting output = ['key', 'Name', 'subjects']

print(len(list(info.keys())))   # output = 3

print(len(info))   # output = 3  # line 19 and 21 is for same value but written in diffrent type..


   

  