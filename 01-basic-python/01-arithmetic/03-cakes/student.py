def cakes(eggs, butter, flour):
    eggs = eggs // 5
    butter = butter // 240
    flour = flour // 250
    return min(eggs, butter, flour)
