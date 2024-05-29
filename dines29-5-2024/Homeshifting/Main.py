# import Shiftingitems.Books
# obj=Shiftingitems.Books.ABC()
# obj.Bookstype()
# import Shiftingitems.Cloths.Jeans
# Shiftingitems.Cloths.Jeans.display()

       #Another way -->

# from Shiftingitems import Books
# Books.Bookstype()

# from Shiftingitems.Footwears import Flats,Shoes
# Flats.displayflats()
# Shoes.displayshoes()

# from Shiftingitems.Footwears.Flats import *
# displayflats()
# Shoes.displayshoes()

     #calling all functions

from Shiftingitems.Footwears import *
Flats.displayflats()
Shoes.displayshoes()