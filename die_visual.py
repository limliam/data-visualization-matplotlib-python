from random import randint
import plotly.express as px

class Die:
    """ A class representing a single die. """

    def __init__(self, num_sides=6):
        """ Assume a six-sided die. """
        self.num_sides = num_sides

    def roll(self):
        """ Return a random value between 1 and number of sides. """
        return randint(1, self.num_sides)
    
die = Die()

# create two D6 dice.
die_1 = Die()
#die_2 = Die()
die_2 = Die(10)

# make some rolls, and store results in a list.
results = []
for roll_num in range(50_000):
    # result = die.roll()
    result = die_1.roll() + die_2.roll()     
    results.append(result)
# print(results)

# analyze the results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
#poss_results = range(1, die.num_sides+1) # 1-6
poss_results = range(1, max_result+1) 

for value in poss_results:
    frequency = results.count(value) # the number of occurence for each side
    frequencies.append(frequency)
# print(frequencies)

# visualize the results
# show() method of plotly.express renders the resulting chart
# as an HTML file and open in a new browser tab.

# title = 'Results of Rolling One D6 1,000 Times'
title = 'Results of Rolling D6 and D10 50,000 Times'

labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)   
fig.update_layout(xaxis_dtick=1) # distance of tick mark by 1 

# display the result in web browser
fig.show() 
# or save the result in html file
# fig.write_html('dice_vidual_d6d10.html')

