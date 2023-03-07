import re

txt = '''
This is a random statement.
And this is a random line.
We are both randomly exisitng along lines of parallel universes!!
Is'nt that a randomly amazing statement?!
'''
# re findall is a method which returns a list of occurences
print(re.findall(pattern='random', string=txt))
# splitting the string on the basis of pattern
print(re.split(pattern='\sa', string=txt))
# A matched object is returned with a search method
matched = re.search(pattern='random', string=txt)
# A match object has it's own methods, such as span which returns a tuple of index where pattern was found
print(matched.span())
print(matched.start())
print(matched.end())
print(matched.group())

# A Compile method returns a pattern object. It too has similar methods such as find, findall etc
pattern = re.compile('This is a random statement')
print(
    f'This is the pattern obj findall method: {pattern.findall(string=txt)}')
print(
    f'This is the pattern obj search method: {pattern.search(string=txt)}')
print(
    f'This is the pattern obj fullmatch method: {pattern.fullmatch(string=txt)}')
print(f'This is the pattern obj match method: {pattern.match(txt)}')
