from database import create_connection


def add_expense(amount, category, date, description):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO expenses (amount, category, date, description)
    VALUES (?, ?, ?, ?)
    """, (amount, category, date, description))

    conn.commit()
    conn.close()


def get_expenses():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()

    conn.close()
    return rows


def get_total_expenses():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(amount) FROM expenses")
    total = cursor.fetchone()[0]

    conn.close()
    return total