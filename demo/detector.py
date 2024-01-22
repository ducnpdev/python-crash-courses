import tika
tika.initVM()
from tika import parser
from tika import detector

filePath = "hdss_oldold.pdf"
# filePath = "rwservlet.pdf"
parsed = parser.from_file(filePath)
print(parsed["content"])

print()
print()
print()


# filePath1 = "hdss_cn01signedcn01signed.pdf"
# # filePath = "rwservlet.pdf"
# parsed1 = parser.from_file(filePath1)
# print(parsed1["metadata"])


# print()
# print()

# filePath2 = "hdss_oldold.pdf"
# # filePath = "rwservlet.pdf"
# parsed2 = parser.from_file(filePath2)
# print(parsed2["metadata"])

# print(detector.from_file('rwservlet.pdf'))