def get_human_age(cat_age: int, dog_age: int) -> list:
"    cat_human = 0

    if cat_age >= 15:
        cat_human += 1
        cat_age -= 15

        if cat_age >= 9:
            cat_human += 1
            cat_age -= 9
        cat_human += (cat_age // 4)

    dog_human = 0

    if dog_age >= 15:
        dog_human += 1
        dog_age -= 15

        if dog_age >= 9:
            dog_human += 1
            dog_age -= 9
        dog_human += (dog_age // 5)

    return [cat_human, dog_human]
"