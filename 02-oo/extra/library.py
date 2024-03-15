from libraryitem import Book, CD, Strip
from id_util import ID_UTIL


book = Book("De leeuw van Vlaanderen", "Hendrik Conscience",
            ID_UTIL.generate_id(), True, "Roman")
cd = CD("Master of Puppils", "Metallica", ID_UTIL.generate_id(), True, 8)
strip = Strip("De jacht op een voetbal", "Jef Nijns",
              ID_UTIL.generate_id(), True)
