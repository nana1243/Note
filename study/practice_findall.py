import re

a = ["hennie", "nnie"]
b = "**nnie"

test = re.sub("\*", "[a-z0-9]", b)  # noqa :W605
print(test)
search_result1 = re.findall(test, a[0])
search_result2 = re.findall(test, a[1])

print(search_result1)
print(search_result2)
