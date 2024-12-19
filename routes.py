from flask import Blueprint, request, jsonify
from models import books, members
from auth import is_authenticated
from library_utils import paginate

book_routes = Blueprint('book_routes', __name__)
member_routes = Blueprint('member_routes', __name__)

@book_routes.route('/', methods=['GET', 'POST'])
def manage_books():
    if request.method == 'POST':
        token = request.headers.get('Authorization')
        if not is_authenticated(token):
            return jsonify({'error': 'Unauthorized'}), 401

        book = request.json
        book['id'] = len(books) + 1
        books.append(book)
        return jsonify(book), 201

    search_title = request.args.get('title')
    search_author = request.args.get('author')
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 5))

    filtered_books = [book for book in books if
                      (not search_title or search_title.lower() in book['title'].lower()) and
                      (not search_author or search_author.lower() in book['author'].lower())]

    paginated_books, total = paginate(filtered_books, page, per_page)
    return jsonify({'books': paginated_books, 'total': total}), 200


@book_routes.route('/<int:book_id>', methods=['GET', 'PUT', 'DELETE'])
def manage_book_by_id(book_id):
    token = request.headers.get('Authorization')
    if request.method != 'GET' and not is_authenticated(token):
        return jsonify({'error': 'Unauthorized'}), 401

    book = next((book for book in books if book['id'] == book_id), None)
    if not book:
        return jsonify({'error': 'Book not found'}), 404

    if request.method == 'GET':
        return jsonify(book), 200
    elif request.method == 'PUT':
        updated_data = request.json
        book.update(updated_data)
        return jsonify(book), 200
    elif request.method == 'DELETE':
        books.remove(book)
        return '', 204


@member_routes.route('/', methods=['GET', 'POST'])
def manage_members():
    if request.method == 'POST':
        token = request.headers.get('Authorization')
        if not is_authenticated(token):
            return jsonify({'error': 'Unauthorized'}), 401

        member = request.json
        member['id'] = len(members) + 1
        members.append(member)
        return jsonify(member), 201

    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 5))
    paginated_members, total = paginate(members, page, per_page)
    return jsonify({'members': paginated_members, 'total': total}), 200


@member_routes.route('/<int:member_id>', methods=['GET', 'PUT', 'DELETE'])
def manage_member_by_id(member_id):
    token = request.headers.get('Authorization')
    if request.method != 'GET' and not is_authenticated(token):
        return jsonify({'error': 'Unauthorized'}), 401

    member = next((member for member in members if member['id'] == member_id), None)
    if not member:
        return jsonify({'error': 'Member not found'}), 404

    if request.method == 'GET':
        return jsonify(member), 200
    elif request.method == 'PUT':
        updated_data = request.json
        member.update(updated_data)
        return jsonify(member), 200
    elif request.method == 'DELETE':
        members.remove(member)
        return '', 204
