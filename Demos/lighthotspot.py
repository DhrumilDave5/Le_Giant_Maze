def main() -> None:

    bruh_map = [["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
                ["X", ".", ".", ".", ".", ".", ".", ".", ".", "X"],
                ["X", ".", ".", ".", ".", ".", ".", ".", ".", "X"],
                ["X", ".", ".", ".", ".", ".", ".", ".", ".", "X"],
                ["X", ".", ".", ".", ".", ".", ".", ".", ".", "X"],
                ["X", ".", ".", ".", ".", ".", ".", ".", ".", "X"],
                ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"]
                ]

    position = (4, 4)
    range_ = 4

    bruh_map[position[1]][position[0]] = "O"
    past_lh = []
    present_lh = [position, ]
    future_lh = []

    for i in range(range_):

        count = 0

        for j in present_lh:

            top = (j[0], j[1] - 1)
            right = (j[0] + 1, j[1])
            bottom = (j[0], j[1] + 1)
            left = (j[0] - 1, j[1])
            top_mu = bruh_map[top[1]][top[0]]
            right_mu = bruh_map[right[1]][right[0]]
            bottom_mu = bruh_map[bottom[1]][bottom[0]]
            left_mu = bruh_map[left[1]][left[0]]

            print("-" * 100)
            print("Present_lh Index %s: %s in %s\n"
                  % (count, j, present_lh))
            print("Future Light Hotspots:\n" + str(future_lh))

            if top_mu == "." \
                    and (top not in past_lh + present_lh + future_lh):
                future_lh.append(top)
            if right_mu == "." \
                    and (right not in past_lh + present_lh + future_lh):
                future_lh.append(right)
            if bottom_mu == "." \
                    and (bottom not in past_lh + present_lh + future_lh):
                future_lh.append(bottom)
            if left_mu == "." \
                    and (left not in past_lh + present_lh + future_lh):
                future_lh.append(left)

            print("changed to\n" + str(future_lh))

            count += 1

        past_lh += present_lh
        present_lh.clear()
        present_lh += future_lh
        future_lh.clear()

        for k in present_lh:
            bruh_map[k[1]][k[0]] = "O"

        print("\n" + ("*" * 100))
        print("End of i = %d\n" % i)
        print("Past Light Hotspots: %s\nPresent Light Hotspots: %s"
              % (past_lh, present_lh))
        print("*" * 100)
        print("\nThe Maze at the end of i = %d\n" % i)
        for y in bruh_map:
            for z in y:
                print(z, end="")
            print()
        print("\n" + ("*" * 100))


if __name__ == "__main__":
    main()

'''

Algorithm Summary of the above code:

1)  The code starts with 3 lists 'past_lh', 'present_lh', 'future_lh',
    out of which past_lh and future_lh are blank and present_lh contains
    the initial lh
2)  The 'for i in range(range_)' loop is used to display upto range_ blocks
    away, the variable i here can be used in the actual function to show
    different shades of light (in reverse order)
3)  The 'for j in present_lh' loop is used to basically traverse through
    each present lh
4)  Two variables are created for each of the four 2D directions, which
    basically represent the up, down, right and left mu around j (present
    lh the loop is working on)
5)  It is checked for each of the 4 mu whether it is an empty one, and also
    if it is not already present in the three lh lists, if yes, then it
    becomes a future lh
6)  'for j in present_lh' loop ends
7)  All the elements of present_lh are added to past_lh, and present_lh is
    emptied
8)  All the elements of future_lh are added to present_lh (I did a bug in
    this process earlier, given below this algorithm) and future_lh is
    emptied
9)  The 'for k in present_lh' loop is actually supposed to be the loop
    where we display each k, but here for demonstration simplicity, those
    mu are edited in BRUH_MAP to 2, moreover this loop is placed inside the
    'for i in range(range_)' loop so that we can add different shades to mu
    at different distances from player
10) Finally bruh_map is displayed in 2D matrix form
11) 'for i in range(range_)' loop ends here

(The print statements in 'for i in' and 'for j in' loops are there to show
info about their each run)

The bug i did earlier in step 8 was that basically I was doing:

present_lh = future_lh
present_lh.clear()

thinking that I was sending items of future_lh to present_lh, whereas in
Python it actually means I am telling it to connect present_lh to the same
list as it is to future_lh (Forgot basics, Dumb me took a lot of time to
identify this, and that too with a fluke :P), so the correction I did was:

present_lh += future_lh
future_lh.clear()

future_lh is appended to present_lh since it would be emptied just in the
previous line of code

'''
