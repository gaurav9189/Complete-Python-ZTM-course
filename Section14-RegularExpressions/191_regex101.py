import re
txt = '''
Let's create a sea of comments.
These comments will leave a sea of emotions
These emotions will wash away the sea of struggle
Struggle makes you stronger!
Stronger you are, wealthier you are!!
'''

email = 'someth_in_g@yahoo.co.in'


pattern1 = re.compile(r"[a-zA-Z][s][$\s]")
pattern2 = re.compile(r"([a-zA-Z]).([$!])")
# Creating a pattern object for an email validation
pattern3 = re.compile(
    r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+")
p1 = pattern1.search(string=txt)
p2 = pattern2.search(txt)
p3 = pattern3.search(email)
print(p1.group())
print(p2.group(2))
# using group method on the match object for email pattern. The pattern is using 2 groups as seen in the o/p
print(p3.groups())
