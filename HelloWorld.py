from sda_ex_oop_1_mz.cat import Cat


def cat_creator() -> list:
    cats = []
    cat1 = Cat("Panda")
    cat2 = Cat("Filemon")
    cats.append(cat1)
    cats.append(cat2)
    return cats


def main():
    # cat = Cat("Mruczek")
    # print(cat.make_sound())
    cats = cat_creator()
    for cat in cats:
        print(cat.make_sound())
        cat.eat_mouse()


if __name__ == "__main__":
    main()
