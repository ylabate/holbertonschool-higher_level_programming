#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    for count in range(x):

        try:
            print("{:d}".format(my_list[count]), end='')
            i += 1
        except (ValueError, TypeError):
            continue
    print()
    return (i)


if __name__ == "__main__":
    # Test 1: Liste avec seulement des entiers
    print("=== Test 1: Entiers seulement ===")
    my_list = [1, 2, 3, 4, 5]
    nb_print = safe_print_list_integers(my_list, 2)
    print("nb_print: {:d}".format(nb_print))
    
    # Test 2: Liste avec types mixtes
    print("\n=== Test 2: Types mixtes ===")
    my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
    nb_print = safe_print_list_integers(my_list, len(my_list))
    print("nb_print: {:d}".format(nb_print))
    
    # Test 3: x plus grand que la longueur (doit lever exception)
    print("\n=== Test 3: x > longueur (exception attendue) ===")
    try:
        nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
        print("nb_print: {:d}".format(nb_print))
    except IndexError as e:
        print("Exception IndexError attrapée: {}".format(e))
    
    # Test 4: Liste vide
    print("\n=== Test 4: Liste vide ===")
    my_list = []
    nb_print = safe_print_list_integers(my_list, 0)
    print("nb_print: {:d}".format(nb_print))
    
    # Test 5: Avec des booléens (doivent être ignorés)
    print("\n=== Test 5: Avec booléens ===")
    my_list = [1, True, 2, False, 3]
    nb_print = safe_print_list_integers(my_list, 5)
    print("nb_print: {:d}".format(nb_print))
    
    # Test 6: Entiers négatifs et zéro
    print("\n=== Test 6: Entiers négatifs et zéro ===")
    my_list = [-5, 0, -1, 10, -100]
    nb_print = safe_print_list_integers(my_list, 5)
    print("nb_print: {:d}".format(nb_print))
    
    # Test 7: Tous les éléments ne sont pas des entiers
    print("\n=== Test 7: Aucun entier ===")
    my_list = ["a", "b", "c", 3.14, None]
    nb_print = safe_print_list_integers(my_list, 5)
    print("nb_print: {:d}".format(nb_print))
    
    # Test 8: Types variés avec floats, None, dict
    print("\n=== Test 8: Types très variés ===")
    my_list = [1, 2, 3.5, "Hello", None, 4, {"key": "value"}, 5]
    nb_print = safe_print_list_integers(my_list, 8)
    print("nb_print: {:d}".format(nb_print))
    
    # Test 9: x = 0
    print("\n=== Test 9: x = 0 ===")
    my_list = [1, 2, 3]
    nb_print = safe_print_list_integers(my_list, 0)
    print("nb_print: {:d}".format(nb_print))
    
    # Test 10: Grands entiers
    print("\n=== Test 10: Grands entiers ===")
    my_list = [999999, -999999, 0, 12345]
    nb_print = safe_print_list_integers(my_list, 4)
    print("nb_print: {:d}".format(nb_print))
