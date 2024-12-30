class Knight:
    """
    The knight moves multiple squares each move.
    It either moves up or down one square vertically and over two squares horizontally OR up or down two squares vertically and over one square horizontally.
    This movement can be remembered as an "L-shape" because it looks like a capital "L".
    """

    # The order of the moves significantly impacts the efficiency of solutions
    MOVES = [
        (2, 1),  # One square up and two squares right
        (1, 2),  # Two squares up and one square right
        (-1, 2),  # Two squares up and one square left
        (-2, 1),  # One square up and two squares left
        (-2, -1),  # One square down and two squares left
        (-1, -2),  # Two squares down and one square left
        (1, -2),  # Two squares down and one square right
        (2, -1)  # One square down and two squares right
    ]
