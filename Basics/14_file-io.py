s = "Ayush is a gamer"

#Write

# with open("ayush.txt", "w") as f:
#     f.write(s)

fp = open("ayush.txt", "w")
fp.write(s)
fp.close()