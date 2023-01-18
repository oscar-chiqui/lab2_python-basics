# Part 2: Author class - no duplicate books

# Initialize with name and an empty book list

class Author:
    def __init__(self, name): 

        self.name = name
        self.books = []

# Print error message if book already published under the Author's name.

    def publish(self, book):
        if book in self.books: 
            
            print(f'"{""}" is already published under this author. This Book has already been selected:')

            for book in self.books:
                print(book)

                print('Please try again with a book title that is not already in this list.')

 # Add to book if book not already in list.
        else:
            self.books.append(book)
    
    def __str__ (self):

        book_list = ', '.join(self.books) 

        return(f'Author: {self.name}; Books: {book_list}')

def main():

# name3 from author

    name3 = Author('Sara Smith')
    name3.publish('Always Happy')

    print(name3)

# the book given has the same name as a book currently in the books list.

    name3.publish('Always Happy')

if __name__ == '__main__':
    main()