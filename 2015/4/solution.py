"""--- Day 4: The Ideal Stocking Stuffer ---
Santa needs help mining some AdventCoins (very similar to bitcoins) to use as
gifts for all the economically forward-thinking little girls and boys.

To do this, he needs to find MD5 hashes which, in hexadecimal, start with at
least five zeroes. The input to the MD5 hash is some secret key (your puzzle
input, given below) followed by a number in decimal. To mine AdventCoins, you
must find Santa the lowest positive number (no leading zeroes: 1, 2, 3, ...)
that produces such a hash.

For example:

If your secret key is abcdef, the answer is 609043, because the MD5 hash of
abcdef609043 starts with five zeroes (000001dbbfa...), and it is the lowest
such number to do so.
If your secret key is pqrstuv, the lowest number it combines with to make an
MD5 hash starting with five zeroes is 1048970; that is, the MD5 hash of
pqrstuv1048970 looks like 000006136ef....
Your puzzle answer was 346386.

--- Part Two ---
Now find one that starts with six zeroes.

Your puzzle answer was 9958218.

Both parts of this puzzle are complete! They provide two gold stars: **
"""

import os
from hashlib import md5


def lowest_hash_complement(data, zeros):
    md5_hash = data
    i = 0
    string = "0" * zeros
    while md5_hash[:zeros] != string:
        i += 1
        new_data = data + str(i)
        md5_hash = md5(new_data.encode()).hexdigest()
    return i


if __name__ == "__main__":
    base_path = os.path.dirname(__file__)
    input_path = os.path.join(base_path, "input")
    with open(input_path, "r") as input_file:
        instructions = input_file.read()

    print(lowest_hash_complement(data=instructions, zeros=5))
    print(lowest_hash_complement(data=instructions, zeros=6))
