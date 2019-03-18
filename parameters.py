HOW_MANY_ELEVATORS = 2

LIFETIME_OF_ELEVATOR= 25*365

SINGLE_ELEVATOR_PRICE = 30000

PROBABILITY_OF_FAILURE = 3.5/365

# In days
MINIMUM_REPAIR_TIME = 1
MAXIMUM_REPAIR_TIME = 5


# For new parts/fixing the old parts
MINIMUM_REPAIR_COST = 0
MAXIMUM_REPAIR_COST = 2000


# Just for calling the repair service and making them come around
REPAIR_COST_CONST = 120
REPAIR_COST_PER_DAY = 75 * 8

ANNUAL_CHECK_COST = 150

FULL_LIFETIME_ELEVATOR_PRICE = SINGLE_ELEVATOR_PRICE + ANNUAL_CHECK_COST * 25