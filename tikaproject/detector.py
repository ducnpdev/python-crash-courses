import tika
from tika import detector
print(detector.from_file('rwservlet.pdf'))