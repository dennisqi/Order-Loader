import os
import time
from helper import unzip
from orderloader import OrderLoader
from psqlqueries.inseration_queries import *
from psqlqueries.table_creation_queries import *


if __name__ == '__main__':
    # Create order loader with username, password and dbname
    # host = os.environ.get('PSQL_HOST')
    # username = os.environ.get('PSQL_USERNAME')
    # password = os.environ.get('PSQL_PASSWORS')
    # dbname = os.environ.get('PSQL_DBNAME')
    host = 'localhost'
    username = 'dennisq'
    password = ''
    dbname = 'postgres'
    order_loader = OrderLoader(host, username, password, dbname)

    # Create tables
    table_creation_queries = [
        user_table_creation_query,
        order_table_creation_query,
        product_table_creation_query,
        item_table_creation_query
    ]
    for table_creation_query in table_creation_queries:
        order_loader.create_table(table_creation_query)

    load_queries = [
        item_inseration_query, user_inseration_query,
        order_inseration_query, product_inseration_query]
    wanted_colss = []

    # # Write data into database
    zip_file = '../data/data.zip'
    directory_to_extract_to = '../data/'
    unzip(zip_file, directory_to_extract_to)
    for orders_file in order_loader.get_order_filenames_from_zip(zip_file):
        for order in order_loader.get_orders(directory_to_extract_to + orders_file):
            for load_query, wanted_cols in zip(load_queries, wanted_colss):
                order_loader.write_order_into_db(order, load_query, wanted_cols)

    order_loader.disconnect()
