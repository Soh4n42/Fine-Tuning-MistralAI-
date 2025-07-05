import json


with open('train.json', 'a') as f:
    with open('sports_headlines.txt','r') as f1:
        for lines in f1:
            line = lines.strip()
            if line:
                json.dump({"prompt": "Generate a sports news headline.", "response": lines}, f)
                f.write("\n")