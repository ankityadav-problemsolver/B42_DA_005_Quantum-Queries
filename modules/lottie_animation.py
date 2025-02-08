# load the animation file 
import json
def load_lottie_url(filepath):
    # filepath present locally in the system 
    with open(filepath,"r") as f:
        return json.load(f)
    
    