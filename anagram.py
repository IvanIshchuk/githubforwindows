word = "nose"
candidates = ["Eons", "ONES"]
fit_candidate = []
for candidate in candidates:
    if len(word) == len(candidate):
        word = word.lower()
        candidate_lower = candidate.lower()
        print(len(candidate_lower))
        if word != candidate_lower and sorted(word) == sorted(candidate_lower):
            fit_candidate.append(candidate)
print(fit_candidate)
            
                
