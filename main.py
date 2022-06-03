from Simulation import Simulation

if __name__ == '__main__':
    print("Choose an action:")
    print("1) - Start simulation")
    print("2) - Load simulation")
    print("0) - Exit")
    simulation = Simulation()
    while True:
        choice = input("Enter a number:")
        try:
            get_choice_number = int(choice)
            if 0 > get_choice_number or get_choice_number > 2:
                print("Entered value " + str(get_choice_number) + " is incorrect")
                continue
        except ValueError:
            print("Entered value " + choice + " is not a number")
        else:
            break
    if get_choice_number == 2:
        simulation.load_from_file()
    simulation.simulate()
