def mirror(sen):
    sens = " "
    size = len(sens)
    for i in range(size//2):
        if sens[i] != sens[size-1-i]:
            return False
    return True

print(mirror("abcba"))
print(mirror("abcdba"))