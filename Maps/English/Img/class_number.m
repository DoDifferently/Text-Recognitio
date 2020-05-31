function number = class_number(input)
% Returns the number of the class for a given input character
% For individual samples, the numbers are added according to the order in
% which they've been extracted.

char_vec = ['0':'9', 'A':'Z', 'a':'z'];
number = find(char_vec == input);
