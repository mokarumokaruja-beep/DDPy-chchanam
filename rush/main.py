#!/usr/bin/env python3

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

STATUSES = {
    '1': 'Planned',
    '2': 'Reading',
    '3': 'Finished'
}


def pause():
    input('\nPress Enter to return to the menu...')


def cancel(value):
    return value == '/cancel'


def show_menu(menu):
    for number, name in menu.items():
        print(f'{number}: {name}')


def show_books(books):
    for number, (title, status) in enumerate(books.items(), 1):
        print(f'{number}. {title}: {status}')


def get_status():
    show_menu(STATUSES)
    choice = input('Select status (1-3) (/cancel to return): ').strip()

    if cancel(choice):
        return None
    elif choice in STATUSES:
        return STATUSES[choice]
    else:
        print('Invalid status choice.')
        return ''


def get_book(books, action):
    choice = input(f'Book number to {action} (/cancel to return): ').strip()

    if cancel(choice):
        return None
    elif choice.isdigit() and 1 <= int(choice) <= len(books):
        return list(books)[int(choice) - 1]
    else:
        print('Invalid book number.')
        return ''


def add(books):
    print('\n============ 1. Add new book ============\n')

    title = input('Book title (/cancel to return): ').strip()

    if cancel(title):
        return
    elif not title:
        print('Book title cannot be empty.')
    elif title in books:
        print('Book already exists.')
    else:
        status = get_status()

        if status is None:
            return
        elif not status:
            print('Please select a valid reading status.')
        else:
            books[title] = status
            print('Book added.')

    pause()


def view(books):
    print('\n============ 2. View all books ============\n')

    if not books:
        print('No books found.')
    else:
        show_books(books)

    pause()


def update(books):
    print('\n============ 3. Update reading status ============\n')

    if not books:
        print('No books found.')
        pause()
        return

    show_books(books)
    title = get_book(books, 'update')

    if title is None:
        return
    elif not title:
        pause()
        return

    status = get_status()

    if status is None:
        return
    elif not status:
        print('Please select a valid reading status.')
    else:
        books[title] = status
        print('Reading status updated.')

    pause()


def remove(books):
    print('\n============ 4. Remove book ============\n')

    if not books:
        print('No books found.')
        pause()
        return

    show_books(books)
    title = get_book(books, 'remove')

    if title is None:
        return
    elif not title:
        pause()
        return

    del books[title]
    print('Book removed.')
    pause()


def search(books):
    print('\n============ 5. Search books ============\n')

    keyword = input('Search book (/cancel to return): ').strip()

    if cancel(keyword):
        return

    found = False

    for number, (title, status) in enumerate(books.items(), 1):
        if keyword and keyword.lower() in title.lower():
            print(f'{number}. {title}: {status}')
            found = True

    if not found:
        print('No matching books found.')

    pause()


def summary(books):
    print('\n============ 6. Reading progress ============\n')

    print(f'Total books: {len(books)}')

    for status in STATUSES.values():
        count = 0

        for book_status in books.values():
            if book_status == status:
                count += 1

        print(f'{status}: {count}')

    pause()


def llm(records):
    print('\n============ 7. Reading summary by LLM ===========\n')

    client = OpenAI(
        base_url='https://integrate.api.nvidia.com/v1',
        api_key=os.getenv('NVIDIA_API_KEY')
    )

    while True:
        user_prompt = input('You (/cancel to return): ').strip()

        if isCancel(user_prompt):
            break

        if not user_prompt:
            print('Please enter a question.')
            continue

        response = client.responses.create(
            model='nvidia/nemotron-3.5-super-vl-120b-a12b',
            input=(
                f'Use only these reading records: {records}\n'
                f'User prompt: {user_prompt}'
            )
        )

        print('AI:', response.output_text)


def exit_program():
    goodbye_art = [
        r"     ██████╗  ██████╗  ██████╗ ██████╗",
        r"    ██╔════╝ ██╔═══██╗██╔═══██╗██╔══██╗",
        r"    ██║  ███╗██║   ██║██║   ██║██║  ██║",
        r"    ██║   ██║██║   ██║██║   ██║██║  ██║",
        r"    ╚██████╔╝╚██████╔╝╚██████╔╝██████╔╝",
        r"     ╚═════╝  ╚═════╝  ╚═════╝ ╚═════╝",
        r"           THANKS FOR READING!",
        r"            SEE YOU NEXT TIME!"
    ]

    for line in goodbye_art:
        print(line)


def main():
    books = {}

    header_art = [
        r"╔══════════════════════════════════════════╗",
        r"║                                          ║",
        r"║    ██████╗ ███████╗ █████╗ ██████╗       ║",
        r"║    ██╔══██╗██╔════╝██╔══██╗██╔══██╗      ║",
        r"║    ██████╔╝█████╗  ███████║██║  ██║      ║",
        r"║    ██╔══██║██╔══╝  ██╔══██║██║  ██║      ║",
        r"║    ██║  ██║███████╗██║  ██║██████╔╝      ║",
        r"║    ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝       ║",
        r"║          R E A D I N G   T R A C K E R   ║",
        r"║                                          ║",
        r"╚══════════════════════════════════════════╝"
    ]

    menu = {
        '1': 'Add new book',
        '2': 'View all books',
        '3': 'Update reading status',
        '4': 'Remove book',
        '5': 'Search books',
        '6': 'Summarize reading progress',
        '7': 'Reading summary by LLM',
        '8': 'Exit'
    }

    for line in header_art:
        print(line)

    while True:
        print('\n============ MENU ============\n')
        show_menu(menu)

        choice = input('\nSelect a menu: ').strip()

        if choice == '1':
            add(books)
        elif choice == '2':
            view(books)
        elif choice == '3':
            update(books)
        elif choice == '4':
            remove(books)
        elif choice == '5':
            search(books)
        elif choice == '6':
            summary(books)
        elif choice == '7':
            llm(books)
        elif choice == '8':
            exit_program()
            break
        else:
            print('Invalid menu choice.')


if __name__ == '__main__':
    main()
