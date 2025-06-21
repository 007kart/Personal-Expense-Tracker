from database import create_connection

def add_expense(amount, category, date, note):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO expenses (amount, category, date, note)
        VALUES (?, ?, ?, ?)
    ''', (amount, category, date, note))
    conn.commit()
    conn.close()

def view_expenses():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM expenses')
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_expense(expense_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM expenses WHERE id = ?', (expense_id,))
    conn.commit()
    conn.close()
