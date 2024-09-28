"""Functions for implementing the rules of the classic arcade game Pac-Man."""


def eat_ghost(power_pellet_active, touching_ghost):

    eat = power_pellet_active and touching_ghost
    return eat


def score(touching_power_pellet, touching_dot):

    scored = touching_power_pellet or touching_dot
    return scored


def lose(power_pellet_active, touching_ghost):

    losed = not power_pellet_active and touching_ghost
    return losed


def win(has_eaten_all_dots, power_pellet_active, touching_ghost):

    fin = has_eaten_all_dots
    losed = not power_pellet_active and touching_ghost
    won = fin and losed

    return won



#Print out the return value.
eat = eat_ghost(False, True)
score = score(False, True)
lose = lose(False, True)
win = win(False, True, False)

print( 'can you eat ghost?:', eat, 'can you score?:', score, 'did you loose?:', lose, 'did you win:', win)