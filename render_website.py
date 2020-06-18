from livereload import Server
from jinja2 import Environment, FileSystemLoader, select_autoescape
import json, os
from more_itertools import chunked

def rebuild():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html'])
    )
    template = env.get_template('template.html')

    with open(os.path.join("static", "library.json"), "r", encoding='utf8') as file:
        all_books = json.load(file)
    os.makedirs("pages", exist_ok=True)
    books_groups = list(chunked(all_books, 100))

    pages_filenames = []
    for number, books_group in enumerate(books_groups):
        bisected_books_groups = list(chunked(books_group, 2))

        rendered_page = template.render(bisected_books_groups=bisected_books_groups,
                                        current_page_number=number + 1,
                                        pages_amount=len(books_groups))

        filename = f'index{number + 1}.html'
        with open(os.path.join("pages", filename), 'w', encoding="utf8") as file:
            file.write(rendered_page)
        pages_filenames.append(filename)
    print("Site rebuilded")

    for filename in os.listdir("pages"):
        if filename not in pages_filenames:
            os.remove(os.path.join("pages", filename))

rebuild()

server = Server()

server.watch("template.html", rebuild)

server.serve(root='.')