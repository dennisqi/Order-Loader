import json
import zipfile
import psycopg2


class OrderLoader:

    def __init__(self, host, username, password, dbname):
        self.conn = psycopg2.connect(host=host, user=username, password=password, dbname=dbname)

    def get_order_filenames_from_zip(self, zip_file):
        """Yield all filenames in a zip file."""
        with zipfile.ZipFile(zip_file) as zip_file_obj:
            for filename in zip_file_obj.namelist():
                yield filename

    def get_orders(self, orders_file):
        """Yield all orders in a json file that contains orders."""
        with open(orders_file) as fin:
            for order in json.load(fin)['orders']:
                yield order

    def create_table(self, table_creation_query):
        """Create table using table_creation_query."""
        cur = self.conn.cursor()
        cur.execute(table_creation_query)
        self.conn.commit()
        cur.close()

    def write_order_into_db(self, order, load_query, wanted_cols):
        """
        Load the order in to Postgres database.

        Given a order in a dict format, load the the order info into the
        order table, load the user info into the user table.

        :param order: a dictionary containing order info
        :param load_query: PSQL query to load the data into certain table
        :param wanted_cols: a list of fileds that needed to be loaded
            into table, the fileds should corespond to the load_query
        """
        try:
            cur = self.conn.cursor()
            wanted_values = [order[key] for key in wanted_cols]
            cur.execute(load_query, wanted_values)
            cur.commit()
            cur.close()
        except Exception as e:
            raise e
            return False
        else:
            return True

    def disconnect(self):
        if self.conn:
            self.conn.close()
            return True
        return False
