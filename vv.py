word = "listen"
candidates = ["ilsent"]
fit_candidate = []
for candidate in candidates:
    if word != candidate:
        if sorted(candidate) == sorted(word):
            print(sorted(candidate))
        

    