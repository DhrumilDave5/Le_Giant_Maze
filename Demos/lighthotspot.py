BRUH_MAP = [["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
            ["X", ".", ".", ".", ".", ".", ".", ".", ".", "X"],
            ["X", ".", ".", ".", ".", ".", ".", ".", ".", "X"],
            ["X", ".", ".", ".", ".", ".", ".", ".", ".", "X"],
            ["X", ".", ".", ".", ".", ".", ".", ".", ".", "X"],
            ["X", ".", ".", ".", ".", ".", ".", ".", ".", "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"]
            ]

POSITION = (4, 4)
RANGE = 4

BRUH_MAP[POSITION[1]][POSITION[0]] = "O"
PAST_LH = []
PRESENT_LH = [POSITION, ]
FUTURE_LH = []

for i in range(RANGE):

    COUNT = 0

    for j in PRESENT_LH:

        TOP = (j[0], j[1] - 1)
        RIGHT = (j[0] + 1, j[1])
        BOTTOM = (j[0], j[1] + 1)
        LEFT = (j[0] - 1, j[1])
        TOP_MU = BRUH_MAP[TOP[1]][TOP[0]]
        RIGHT_MU = BRUH_MAP[RIGHT[1]][RIGHT[0]]
        BOTTOM_MU = BRUH_MAP[BOTTOM[1]][BOTTOM[0]]
        LEFT_MU = BRUH_MAP[LEFT[1]][LEFT[0]]

        print("-" * 100)
        print("Present_lh Index %s: %s in %s\n" % (COUNT, j, PRESENT_LH))
        print("Future Light Hotspots:\n" + str(FUTURE_LH))

        if TOP_MU == "." and (TOP not in PAST_LH + PRESENT_LH + FUTURE_LH):
            FUTURE_LH.append(TOP)
        if RIGHT_MU == "." and (RIGHT not in PAST_LH + PRESENT_LH + FUTURE_LH):
            FUTURE_LH.append(RIGHT)
        if BOTTOM_MU == "." and (BOTTOM not in PAST_LH + PRESENT_LH + FUTURE_LH):
            FUTURE_LH.append(BOTTOM)
        if LEFT_MU == "." and (LEFT not in PAST_LH + PRESENT_LH + FUTURE_LH):
            FUTURE_LH.append(LEFT)

        print("changed to\n" + str(FUTURE_LH))

        COUNT += 1

    PAST_LH += PRESENT_LH
    PRESENT_LH.clear()
    PRESENT_LH += FUTURE_LH
    FUTURE_LH.clear()

    for k in PRESENT_LH:
        BRUH_MAP[k[1]][k[0]] = "O"

    print("\n" + ("*" * 100))
    print("End of i = %d\n" % i)
    print("Past Light Hotspots: %s\nPresent Light Hotspots: %s" % (PAST_LH, PRESENT_LH))
    print("*" * 100)
    print("\nThe Maze at the end of i = %d\n" % i)
    for y in BRUH_MAP:
        for z in y:
            print(z, end="")
        print()
    print("\n" + ("*" * 100))

'''

Algorithm Summary of the above code:

1)  The code starts with 3 lists 'PAST_LH', 'PRESENT_LH', 'FUTURE_LH', out of which PAST_LH and FUTURE_LH are blank and
    PRESENT_LH contains the initial lh
2)  The 'for i in range(RANGE)' loop is used to display upto RANGE blocks away, the variable i here can be used in the
    actual function to show different shades of light (in reverse order)
3)  The 'for j in PRESENT_LH' loop is used to basically traverse through each present lh
4)  Two variables are created for each of the four 2D directions, which basically represent the up, down, right and left
    mu around j (present lh python is working on)
5)  It is checked for each of the 4 mu whether it is an empty one, and also if it is not already present in the three lh
    lists, if yes, then it becomes a future lh
6)  'for j in PRESENT_LH' loop ends
7)  All the elements of PRESENT_LH are added to PAST_LH, and PRESENT_LH is emptied
8)  All the elements of FUTURE_LH are added to PRESENT_LH (I did a bug in this process earlier, given below this
    algorithm) and FUTURE_LH is emptied
9)  The 'for k in PRESENT_LH' loop is actually supposed to be the loop where we display each k, but here for
    demonstration simplicity, those mu are edited in BRUH_MAP to 2, moreover this loop is placed inside the 'for i in
    range(RANGE)' loop so that we can add different shades to mu at different distances from player
10) Finally BRUH_MAP is displayed in 2D matrix form
11) 'for i in range(RANGE)' loop ends here

(The print statements in 'for i in' and 'for j in' loops are there to show info about their each run)

The bug i did earlier in step 8 was that basically I was doing:

PRESENT_LH = FUTURE_LH
FUTURE_LH.clear()

thinking that I was sending items of FUTURE_LH to PRESENT_LH, whereas in Python it actually means I am telling it to
connect PRESENT_LH to the same list as it is to FUTURE_LH (Forgot basics, Dumb me took a lot of time to identify this,
and that too with a fluke :P), so the correction I did was:

PRESENT_LH += FUTURE_LH
FUTURE_LH.clear()

FUTURE_LH is appended to PRESENT_LH since it would be emptied just in the previous line of code

'''
