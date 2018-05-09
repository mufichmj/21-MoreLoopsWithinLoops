"""
This project demonstrates NESTED LOOPS (i.e., loops within loops)
in the context of TWO-DIMENSIONAL GRAPHICS.

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Mariah Mufich.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to test them. """
    run_test_draw_upside_down_wall()


def run_test_draw_upside_down_wall():
    """ Tests the    draw_upside_down_wall    function. """
    # Tests 1 and 2 are ALREADY DONE (here).
    window = rg.RoseWindow(550, 300, 'Upside-down wall, Tests 1 and 2')

    rectangle = rg.Rectangle(rg.Point(125, 230), rg.Point(155, 250))
    draw_upside_down_wall(rectangle, 8, window)

    rectangle = rg.Rectangle(rg.Point(375, 175), rg.Point(425, 225))
    draw_upside_down_wall(rectangle, 4, window)

    window.close_on_mouse_click()


def draw_upside_down_wall(rectangle, n, window):
    """
    See   MoreWalls.pdf   in this project for pictures that may
    help you better understand the following specification:

    Draws an "upside-down wall" on the given window, where:
      -- The BOTTOM of the wall is a single "brick"
            that is the given rg.Rectangle.
      -- There are n rows in the wall.
      -- Each row is a row of "bricks" that are the same size
            as the given rg.Rectangle.
      -- Each row has one more brick than the row below it.
      -- Each row is centered on the bottom row.

    Preconditions:
      :type rectangle: rg.Rectangle
      :type n: int
      :type window: rg.RoseWindow
    and n is nonnegative.
    """
    # ------------------------------------------------------------------
    # TODO: 2. Implement and test this function.
    #     Some tests are already written for you (above).
    # ------------------------------------------------------------------
    orig_c1x = rectangle.corner_1.x
    orig_c1y = rectangle.corner_1.y
    orig_c2x = rectangle.corner_2.x
    orig_c2y = rectangle.corner_2.y

    c1x = orig_c1x
    c1y = orig_c1y
    c2x = orig_c2x
    c2y = orig_c2y
    height = rectangle.get_height()
    width = rectangle.get_width()

    c1 = rg.Point(c1x, c1y)
    c2 = rg.Point(c2x, c2y)


    for k in range(n):
        for j in range(k + 1):
            new_rect = rg.Rectangle(c1, c2)
            new_rect.attach_to(window)
            window.render(.1)

            c1x = c1x + width
            c2x = c2x + width
        c1x = orig_c1x - (k + 1) * (width) * (0.5)
        c2x = orig_c2x - (k + 1) * (width) * (0.5)
        c1y = orig_c1y - height
        c2y = orig_c2y - height

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
