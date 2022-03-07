# -*- coding: UTF-8 -*-

import numpy
import random

# A list of the emoji we want to randomize.
emojilist =  '👩‍💻','👩🏻‍💻','👩🏽‍💻','👩🏼‍💻','👩🏾‍💻','👩🏿‍💻','👨‍💻','👨🏻‍💻','👨🏼‍💻','👨🏽‍💻','👨🏾‍💻','👨🏿‍💻'

# Repeat it X number of times (I'm using 10 here as an example).
repeated = numpy.repeat(emojilist, 10)

# Randomize the list (in place).
random.shuffle(repeated)

# Join the elements together with nothing in between, and print it out.
# It's easy to pipe the output to a file using ">".
print ''.join(repeated[1])