import json
import os
def getlist():
    """
    return a generator for @/data.influencer.JSON
    """
    with open(f'{os.path.abspath("./")}/data/influencers.JSON') as json_file:
        raw_list=json.load(json_file)
        for business in raw_list:
            for influencer in  raw_list[business]:
                yield influencer