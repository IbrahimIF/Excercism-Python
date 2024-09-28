"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):

    print ("dosen't work")
    total = temperature * neutrons_emitted
    print (total)
    if temperature < 800 and neutrons_emitted > 500 and total < 500000:
        return True
    else:
        return False


def reactor_efficiency(voltage, current, theoretical_max_power):

    generated_power = voltage * current
    efficiency = (generated_power/theoretical_max_power) * 100
    if efficiency >= 80:
        print ("green")
        return "green"
    elif efficiency < 80 and efficiency >= 60:
        print ("orange")
        return "orange"
    elif efficiency < 60 and efficiency >= 30:
        print ("red")
        return "red"
    elif efficiency < 30:
        print ("black")
        return "black"
    else:
        print ("try again")
        return False


def fail_safe(temperature, neutrons_produced_per_second, threshold):

    critical = temperature * neutrons_produced_per_second
    ninety = threshold * 0.9
    ten = threshold * 1.1
    if critical < ninety:
        return "LOW"
    elif critical <= ten:
        return "NORMAL"
    else:
        return "DANGER"
    


# to print out the return value.
balanced = is_criticality_balanced(800, 500)
efficiency = reactor_efficiency(10, 1000, 10000)
safe = fail_safe(10, 399, 10000 )

print( 'Is it critically balanced?:', balanced, 'Reactor Efficiency:', efficiency, 'failsafe:', safe)