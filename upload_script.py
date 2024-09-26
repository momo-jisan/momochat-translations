import csv
import mysql.connector
import os

def truncate_table(cursor, table_name):
  try:
    cursor.execute(f"SET FOREIGN_KEY_CHECKS = 0")
    cursor.execute(f"TRUNCATE TABLE {table_name}")
    cursor.execute(f"SET FOREIGN_KEY_CHECKS = 1")
    print(f"Table {table_name} truncated successfully.")
  except mysql.connector.Error as err:
    print(f"Error truncating table {table_name}: {err}")


def upload_csv_to_table(file_path, table_name):
  conn = mysql.connector.connect(
    host=os.getenv('MYSQL_HOST'),
    user=os.getenv('MYSQL_USER'),
    password=os.getenv('MYSQL_PASSWORD'),
    database=os.getenv('MYSQL_DB')
  )
  cursor = conn.cursor()

  # Open the CSV file
  with open(file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    columns = reader.fieldnames

    # Drop the existing table rows if they exist
    truncate_table(cursor, table_name)

    # Create a query dynamically based on the CSV columns and table name
    placeholders = ', '.join(['%s'] * len(columns))
    columns_str = ', '.join(columns)
    query = f"INSERT INTO {table_name} ({columns_str}) VALUES ({placeholders})"
    query += f" ON DUPLICATE KEY UPDATE " + ', '.join([f"{col} = VALUES({col})" for col in columns])

    for row in reader:
      values = tuple(None if row[col].strip() == '' else row[col] for col in columns)
      cursor.execute(query, values)

    conn.commit()
    cursor.close()
    conn.close()


def upload_all_tables():
  csv_dir = './momodb' #+ os.getenv('MYSQL_DB')
  for csv_file in os.listdir(csv_dir):
    if csv_file.endswith('.csv'):
      # Extract table name from CSV file name
      table_name = csv_file.replace('.csv', '')
      file_path = os.path.join(csv_dir, csv_file)
      print(f"Uploading data from {csv_file} to table {table_name}...")
      upload_csv_to_table(file_path, table_name)


if __name__ == '__main__':
  upload_all_tables()
