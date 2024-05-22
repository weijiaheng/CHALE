import json
import numpy as np
import pandas as pd

###########  Step 1: Load synthetic hallucinated dataset  ###########
    # follow ./synthetic_halu_data_simplified.ipynb
    # with open('../hallucinated_ans.json', 'r') as f:
with open('hallucinated_ans_final_filtered.json', 'r') as f:
    loaded_hallucinated_ans = json.load(f)
    
# The dataset includes following keys
print(loaded_hallucinated_ans.keys())
