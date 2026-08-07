library={}
def add_book():
  status='Available'
  title=input('Enter the title of the book: ')
  if title in library:
    print(f'This book titled {title} is available')
  else:
    library[title]=status
    print('Book added successfully!')
def view_book():
  status='Available'
  for title,status in library.items():
    print(f'{title}: {status}')
def search_book():
  status='Available'
  title=input('Enter the title of the book: ')
  if title in library:
    print(f'{title}: {status}')
  else:
    print('Such book is not available!')
def borrow_book():
  status='Borrowed'
  title=input('Enter the title of the book you want to borrow: ')
  if title in library:
    library[title]=status
    print(f'You have successfully borrowed {title}!')
  else:
    print(f'The book titled {title} is not available')
def return_book():
  title=input('Enter the title of the book you want to return: ')
  if title in library:
    if library[title]=='Borrowed':
      library[title]='Available'
      print('Book returned successfully!')
    else:
      print('This book was not borrowed!')
  else:
    print('Such book is not available!')
    
def save():
  status='Available'
  with open('library_books.txt','w') as file:
    for title,status in library.items():
      file.write(f'{title}: {status}')
def main():
  while True:
    print('=== LIBRARY MANAGEMENT SYSTEM ===')
    print('1. Add Books')
    print('2. View all Books')
    print('3. Search for Book')
    print('4. Borrow a Book')
    print('5. Return a Book')
    print('6. Save Library Records')
    choice=input('Enter an option: ')
    if choice=='1':
      add_book()
    elif choice=='2':
      view_book()
    elif choice=='3':
      search_book()
    elif choice=='4':
      borrow_book()
    elif choice=='5':
      return_book()
    elif choice=='6':
      save()
    elif choice=='7':
      print('Thanks for using the library\nGoodbye!')
    else:
      print('Invalid Option!')
if __name__=='__main__':
  main()