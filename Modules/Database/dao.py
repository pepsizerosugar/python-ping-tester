import sqlite3

from Modules.Database.DataClass.transfer import Transfer


# Assign data to transfer class
def assign_data(data):
    Transfer.server_list = data


class dao:
    def __init__(self, dbname):
        self.dbname = dbname
        self.conn = sqlite3.connect(self.dbname)
        self.cursor = self.conn.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.commit()
            self.conn.close()

    # Create table
    def create_table(self, table_name):
        if self.table_exists(table_name):
            return False
        else:
            self.execute(
                f"CREATE TABLE {table_name} (server_name TEXT, server_region TEXT, server_ip TEXT)")
            return True

    def table_exists(self, table_name):
        self.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'")
        return self.cursor.fetchone() is not None

    # Insert data
    def insert_data(self, table_name, values):
        try:
            self.execute(
                f"INSERT INTO {table_name} (server_name, server_region, server_ip) VALUES {values}")
            return True
        except sqlite3.IntegrityError:
            return False

    # Select data
    def select_data(self, table_name):
        try:
            self.execute(f"SELECT * FROM {table_name}")
            assign_data(self.cursor.fetchall())
            return Transfer.server_list
        except sqlite3.OperationalError:
            return False

    def select_data_by_server_name(self, table_name, server_name):
        try:
            self.execute(f"SELECT * FROM {table_name} WHERE server_name = '{server_name}'")
            assign_data(self.cursor.fetchall())
            return Transfer.server_list
        except sqlite3.OperationalError:
            return False

    def select_data_by_server_region(self, table_name, server_region):
        try:
            self.execute(f"SELECT * FROM {table_name} WHERE server_region = '{server_region}'")
            assign_data(self.cursor.fetchall())
            return Transfer.server_list
        except sqlite3.OperationalError:
            return False

    def select_data_by_server_ip(self, table_name, server_ip):
        try:
            self.execute(f"SELECT * FROM {table_name} WHERE server_ip = '{server_ip}'")
            assign_data(self.cursor.fetchall())
            return Transfer.server_list
        except sqlite3.OperationalError:
            return False

    # Update data
    def update_data(self, table_name, values):
        """
        Update data in table
        :param table_name: table name
        :param values: values to update (values[0] = column name, values[1] = existing value, values[2] = new value)
        :return: True if success, False if not
        """
        try:
            self.execute(
                f"UPDATE {table_name} SET {values[0]} = {values[1]} WHERE {values[0]} = {values[2]}")
            return True
        except sqlite3.OperationalError:
            return False

    # Delete data
    def delete_data(self, table_name, values):
        """
        Delete data from table
        :param table_name: table name
        :param values: values to delete (values[0] = column name, values[1] = value to delete)
        :return: True if success, False if not
        """
        try:
            self.execute(
                f"DELETE FROM {table_name} WHERE {values[0]} = {values[1]}")
            return True
        except sqlite3.OperationalError:
            return False

    # Delete table
    def delete_table(self, table_name):
        """
        Delete table
        :param table_name: table name
        :return: True if success, False if not
        """
        try:
            self.execute(f"DROP TABLE {table_name}")
            return True
        except sqlite3.OperationalError:
            return False

    # Delete all data
    def delete_all_data(self, table_name):
        """
        Delete all data from table
        :param table_name: table name
        :return: True if success, False if not
        """
        try:
            self.execute(f"DELETE FROM {table_name}")
            return True
        except sqlite3.OperationalError:
            return False

    # Delete all tables
    def delete_all_tables(self):
        """
        Delete all tables
        :return: True if success, False if not
        """
        try:
            self.execute(f"SELECT name FROM sqlite_master WHERE type='table'")
            tables = self.cursor.fetchall()
            for table in tables:
                self.cursor.execute(f"DROP TABLE {table}")
            return True
        except sqlite3.OperationalError:
            return False

    # Delete all data and tables
    def delete_all(self, table_name):
        """
        Delete all data and tables
        :param table_name: table name
        :return: True if success, False if not
        """
        if self.delete_all_data(table_name) & self.delete_all_tables():
            return True
        else:
            return False

    # execute sql
    def execute(self, sql):
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except sqlite3.OperationalError as e:
            print(e)
