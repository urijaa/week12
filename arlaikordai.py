from flask import Flask, jsonify, request
from flask_cors import CORS,cross_origin

app = Flask(__name__)


CORS(app)

books = [{"id":1,"title":"Book1", "author":"me"},{"id":2,"title":"Book2", "author":"me"},{"id":3,"title":"Book3", "author":"me"}]



@app.route("/")
def Greet():
    return "<p>Hello world</p>"

@app.route("/books", methods=["GET"])
@cross_origin()
def get_all_books():
    return jsonify({"books":books})

@app.route("/books/<int:book_id>", methods=["GET"])
@cross_origin()
def get_books(book_id):
    book = next((b for b in books if b["id"]==book_id), None)
    if book:
        return jsonify(book)
    else:
        return jsonify({"error":"Book not found"}), 404

@app.route("/books", methods=["POST"])
@cross_origin()
def create():
    data = request.get_json()
    new_books={
        "id": len(books)+1,
        "title": data["title"],
        "author": data["author"]
    }
    books.append(new_books)
    return jsonify(new_books), 201

@app.route("/books/<int:book_id>", methods=["DELETE"])
@cross_origin()
def delete_books(book_id):
    global books 
    books = [b for b in books if b["id"]!=book_id]
    return jsonify({"message":"book was Deleted"})

@app.route("/books/<int:book_id>", methods=["PUT"])
@cross_origin()
def update_books(book_id):
    book = next((b for b in books if b["id"]!=book_id), None)
    if book: 
        data = request.get_json()
        book.update(data)
        return jsonify(book), 200
    else:
        return jsonify({"message":"Book not found"}), 404

if __name__ == "__main__":
    app.run(host="127.0.0.1", port="5000" ,debug=True)