

male = True
tall = False

if male and tall:
    print("You are not tall")
elif male and not(tall):
    print("You are a short male.")
elif not(male) and tall:
    print("You are not a male but are tall.")
else:
    print("You are either not a male or not tall or both.")
