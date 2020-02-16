"""
For the given integer X print 1 if it's positive, -1 if it's negative, or 0 if it's equal
to zero.
Try to use the cascade if-elif-else for it.
"""

X = int(input('введите любое число '))
if X > 0:
    print(1)
elif X < 0:
    print(-1)
else:
    print (0)