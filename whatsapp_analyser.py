import matplotlib.pyplot as plt
from collections import Counter
import numpy as np
with open ("WhatsApp Chat with School frnds.txt","r", encoding="utf-8") as f:
    data = f.readlines()
    names = []

    for line in data:
        if "-" in line and ":" in line:
            try:
                name = line.split("-")[1].split(":")[0].strip() 
                names.append(name)
            except:
                continue
    count = Counter(names)
    print(count)
    names = list(count.keys())
    messages = list(count.values())

    plt.bar(names, messages, color ='#003f5c')
    plt.xlabel("People")
    plt.ylabel("Number of Messages")
    plt.title("WhatsApp Chat Analysis")

    plt.show()
