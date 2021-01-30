from sample_madlibs import whiskey,tango,foxtrot
import random

if __name__ == "__main__":
    m = random.choice([whiskey,tango,foxtrot])
    m.madlib()
    