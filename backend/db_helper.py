import mysql.connector
from contextlib import contextmanager
import logging
from logging_setup import setup_logger

logger = setup_logger('db_helper')
@contextmanager
def get_db_cursor(commit=False):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="2303",
        database="expense_manager"
    )

    cursor = connection.cursor(dictionary=True)
    yield cursor
    if commit:
        connection.commit()
    print("Closing cursor")
    cursor.close()
    connection.close()


def fetch_all_records():
    query = "SELECT * from expenses"

    with get_db_cursor() as cursor:
        cursor.execute(query)
        expenses = cursor.fetchall()
        for expense in expenses:
            print(expense)


def fetch_expenses_for_date(expense_date):
    logger.info(f"fetch_expenses_for_date called with {expense_date}")
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses WHERE expense_date = %s", (expense_date,))
        expenses = cursor.fetchall()
        for expense in expenses:
            print(expense)
    return expenses  # Ensure this line is here to return the data to the caller


def insert_expense(expense_date, amount, category, notes):
    logger.info(f"finsert_expense called with date:{expense_date}, amount:{amount}, category:{category}, notes:{notes}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute(
            "INSERT INTO expenses (expense_date, amount, category, notes) VALUES (%s, %s, %s, %s)",
            (expense_date, amount, category, notes)
        )


def delete_expenses_for_date(expense_date):
    logger.info(f"delete_expenses_for_date called with {expense_date}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("DELETE FROM expenses WHERE expense_date = %s", (expense_date,))

def fetch_expenses_summary(start_date, end_date):
    logger.info(f"fetch_expenses_summery called with start:{start_date}, end:{end_date}")
    with get_db_cursor() as cursor:
        cursor.execute(
            '''SELECT category, SUM(amount) as total 
               FROM expenses WHERE expense_date
               BETWEEN %s AND  %s
               GROUP BY category''',
               (start_date,end_date)
            )

        data = cursor.fetchall()
        return data

def fetch_expenses_by_month(month, year):
    logger.info(f"fetch_expenses_by_month called with month: {month}, year: {year}")
    with get_db_cursor() as cursor:
        cursor.execute(
            '''SELECT category, SUM(amount) as total 
               FROM expenses 
               WHERE EXTRACT(MONTH FROM expense_date) = %s 
               AND EXTRACT(YEAR FROM expense_date) = %s
               GROUP BY category''',
            (month, year)
        )

        data = cursor.fetchall()
        return data



if __name__ == "__main__":
    # fetch_all_records()
    # fetch_expenses_for_date("2024-08-01")
    # insert_expense("2024-08-20", 300, "Food", "Panipuri")
    # delete_expenses_for_date("2024-08-20")
    fetch_expenses_for_date("2024-08-20")

    summery = fetch_expenses_summary("2024-08-01","2024-08-05")
    for record in summery:
        print(record)