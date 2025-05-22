from mymodule import greeting # can import specific file this way which doesnt call any other defined functions

greeting("Diwas")

from mymodule import sum,diff

result1=sum(1,2)
print(result1)
result2=diff(3,2)
print(result2)

from mymodule import mul as m #can name function after importing 
result3=m(3,2)
print(result3)


#alternate way
import mymodule #it will run the whole file this way
mymodule.greeting("Diwas")

import mymodule as m #can name file
m.greeting("Diwas")
