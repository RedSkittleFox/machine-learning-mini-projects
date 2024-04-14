import os

for filename in os.listdir("./../"):
    if(filename[0].isdigit()):
        for notebook in os.listdir(f"./../{filename}"):
            if notebook.endswith(".ipynb"):
                print(f"{notebook}\n")
                os.system(f"jupyter nbconvert --to markdown \"./../{filename}/{notebook}\" --output=readme.md")
                break
