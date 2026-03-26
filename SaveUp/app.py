from flask import Flask, request, jsonify
from database import create_table
from expense_manager import add_expense, get_expenses, get_total_expenses

app = Flask(__name__)

create_table()

@app.route("/")
def home():
    return "SaveUp API is running!"

@app.route("/add_expense", methods=["POST"])
def add():
    data = request.json
    add_expense(
        data["amount"],
        data["category"],
        data["date"],
        data.get("description", "")
    )
    return jsonify({"message": "Expense added successfully"}), 201

@app.route("/expenses", methods=["GET"])
def view():
    expenses = get_expenses()
    return jsonify(expenses)

@app.route("/total", methods=["GET"])
def total():
    total_value = get_total_expenses()
    return jsonify({"total_expenses": total_value})

if __name__ == "__main__":
    app.run(debug=True)