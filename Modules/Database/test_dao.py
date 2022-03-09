import unittest

from Modules.Database.dao import dao


class TestDAO(unittest.TestCase):
    def setUp(self):
        self.database = "test_database"
        self.table = "test_table"
        self.server = "localhost"
        self.region = "us-east-1"
        self.ip = "0.0.0.0"
        self.dao = dao(self.database)

    def test_create_database(self):
        import os
        self.assertTrue(os.path.exists(self.database))

    def test_create_table(self):
        self.dao.create_table(self.table)
        self.assertTrue(self.dao.table_exists(self.table))

    def test_insert_data(self):
        values = (self.server, self.region, self.ip)
        self.dao.create_table("test_insert_data")
        if self.dao.insert_data("test_insert_data", values):
            self.assertTrue(self.dao.select_data("test_insert_data"), [(self.server, self.region, self.ip)])
        else:
            self.assertFalse(self)

    def test_select_data(self):
        values = (self.server, self.region, self.ip)
        self.dao.create_table("test_select_data")
        if self.dao.insert_data("test_select_data", values):
            self.assertEqual(self.dao.select_data("test_select_data"), [(self.server, self.region, self.ip)])
        else:
            self.assertFalse(self)
