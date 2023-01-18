""""
Oscar Chiqui | ITEC 2905-80  Capstone.

An author has a name, and a list of books published
"""

print("Part 1: Author class \n")

# Create a class
# __init__ method

class Author:
    def __init__(self,name):

        self.name = name
        self.books = []

    def publish(self, book):
        self.books.append(book)

#Add a __str__ method that returns a String with the author's name, 
# and the names of all of their book's titles.

    def __str__(self):

        book_list = ', '.join(self.books) or 'No published books'

        return(f'Author: {self.name}.Books: {book_list}')

# Write a main function to test your class, create some example authors, 
# and publish some examples books. 

def main():
    name1 = Author('Anahi Martinez')
    name1.publish('Dream in 2023')
    name1.publish('The dark Novel')

    print(name1)

    name2 = Author('Erick Ten Hang ')
    print(name2)

    name3 = Author('Sara Smith')
    name3.publish('1:Past and Glory Vol:1')
    name3.publish('2: Always Happy')
    name3.publish('3: Variety')

    print(name3)

    name2.publish('My first Book by Erik Ten Hang : Paradise City')

    print(name2)

if __name__ == '__main__':
    main()