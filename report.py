from database import create_connection
from tabulate import tabulate

def monthly_summary():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT substr(date, 1, 7) as month, SUM(amount)
        FROM expenses
        GROUP BY month
        ORDER BY month
    ''')
    data = cursor.fetchall()
    conn.close()
    print(tabulate(data, headers=["Month", "Total Spent"], tablefmt="psql"))

def category_summary():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT category, SUM(amount)
        FROM expenses
        GROUP BY category
    ''')
    data = cursor.fetchall()
    conn.close()
    print(tabulate(data, headers=["Category", "Total Spent"], tablefmt="psql"))
