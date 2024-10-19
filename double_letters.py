def double_letters(word):
    if len(word) < 1:
        return False
    prev_letter = ""
    current_letter = ""
    returningValue = ""
    for letter in word:
        prev_letter = current_letter
        current_letter = letter
        if prev_letter == current_letter:
            returningValue = True
            break
        else:
            returningValue = False
    return returningValue