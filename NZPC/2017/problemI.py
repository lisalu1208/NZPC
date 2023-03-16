"""
The Airport at NZPC headquarters is small by international standards, but the number of flights is
steadily increasing and has reached the point at which computer help with air traffic control is
needed. You have been asked to write part of the control algorithm. The airport is responsible for
aircraft in its immediate vicinity, and in particular for managing landing paths. Here is a diagram of
the airport environment.

The environment is a large circular area centred about 5 km south of the runway. Incoming aircraft
fly directly toward the centre from distant places (incoming from easterly and westerly directions –
never flying due north or south). When they reach the edge of the control circle they must be given
a ‘landing slot’ on the landing path. Incoming aircraft will all be travelling at a fixed speed of 400
km/hour. Imagine the landing path as a huge invisible ‘conveyor belt’ in the sky, extending south
from the control area centre. At midnight each day the conveyor belt starts with slot 0 at the centre,
and slots 1, 2, … each spaced 30 seconds of flying time apart to the south. The ‘conveyor’ moves
north at aircraft flying speed. The diagram above shows the conveyor belt at 1am in the morning –
with slot 120 just crossing the centre. When an aircraft is allocated its slot, it turns to fly so as to
exactly meet its ‘slot’ on the landing path, and then turns to align with the landing path and
proceeds to touch down shortly after crossing the centre. Usually there are several possible slots
available for an aircraft, the allocation rules just requiring that the aircraft must join its slot south of
the centre and inside the control circle. The diagram on the next page shows some possibilities.

Here an aircraft approaches with heading -50 degrees (+ve angle is clockwise from North). It arrives
at the edge of the (in this case 23 km radius) control circle at exactly 1am (just as slot 120 passes the
centre). The first slot it could meet is 127, and it would meet that slot at the point shown
approximately 3.5 minutes after arriving at the edge. Turning left at successively greater angles
would allow it to meet slots 128, 129, … through to 132 at the points shown. If it turned to meet slot
133, the meeting point would be outside the control circle and that would therefore not be allowed.

The algorithm for selecting landing slots processes the aircraft in the order in which their data is
received (which will be a non-decreasing time order). Each aircraft is allocated to the first slot it can
reach which has not yet been used for another aircraft. Note that the algorithm does not check to
see if flight paths intersect – another part of the system will do safety checks.

Input:

The algorithm for selecting landing slots processes the aircraft in the order in which their data is
received (which will be a non-decreasing time order). Each aircraft is allocated to the first slot it can
reach which has not yet been used for another aircraft. Note that the algorithm does not check to
see if flight paths intersect – another part of the system will do safety checks.

Output:

For each scenario your program should output one line with the text “Scenario” and the number of
the problem (counting from 1), followed by N lines, one for each aircraft (in the same order as given
in the input). For each aircraft you should output the slot number allocated to the plane, the
distance from the centre (in km) at which the plane meets the landing path, and the time at which
the aircraft will reach the centre of the control area (to commence final descent and landing).

Follow the format shown in the sample output. The distance and time values should be displayed
rounded with four decimals. Sample and test data has been chosen to avoid marginal rounding
values. You may assume that at least one landing slot will be available for each aircraft.
"""
