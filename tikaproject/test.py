import tika 
tika.initVM()
from tika import parser


parsed = parser.from_file('rwservlet.pdf')


# print(parsed["metadata"])
print(parsed["content"])