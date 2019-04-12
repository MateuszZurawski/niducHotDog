import argparse
import parameters
import simulator
from numpy import arange
from tqdm import tqdm

possible_parameters = [item for item in dir(parameters) if not item.startswith("__") and not "COLORS" in item and not "LIFETIME_OF_ELEVATOR" in item]

parser = argparse.ArgumentParser(description='Elevator Simulator *disco music*.')

parser.add_argument('--parameter', type=str, required=True, choices=possible_parameters)

parser.add_argument('--range', type=float, nargs=3, metavar=('from', 'to', 'step'), required=True,
                    help='Range of values in which the parameter will change')


args = parser.parse_args()

simulator = simulator.Simulator()

parameter_to_change = args.parameter
from_value = args.range[0]
to_value = args.range[1]
step = args.range[2]

filename = 'results/' + parameter_to_change + '.csv'
output_file = open(filename, 'w')

print('# Simulating...')
for value in tqdm( arange(from_value, to_value, step)):
    setattr(parameters, parameter_to_change, value)

    output_file.write( str(simulator.average_uptime(100) ) + '\n' )
    #print(getattr(parameters, args.parameter))
    #simulation.run()   


print(f'# Saved to {filename}...')