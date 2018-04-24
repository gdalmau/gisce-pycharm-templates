# -*- encoding: utf-8 -*-
from collections import namedtuple
from erppeek import Client
from csv import reader
from tqdm import tqdm

import click


HEADERS = [
    'column1',
    'column2',
    'column3',
]

Row = namedtuple('CSVRow', field_names=HEADERS)


def count_lines(filepath):
    with open(filepath, 'r') as file_to_read:
        return len(file_to_read.readlines())


def parse_line(connection, row):
    pass
    

def import_from_csv(connection, filepath, separator=';'):
    total = count_lines(filepath)
    with open(filepath, 'r') as csvfile:
        csvreader = reader(csvfile, separator=separator)
        for vals in tqdm(csvreader, desc='Reading CSV', total=total):
            row = Row(vals)
            parse_line(connection, row)


@click.command()
@click.option('-h', '--host',
              help='Host to connect to via ERP Peek',
              type=str, default='http://localhost', show_default=True)
@click.option('-p', '--port',
              help='Port to connect via ERP Peek',
              type=int, default=8069, show_default=True)
@click.option('-d', '--database',
              help='Database to connect to the ERP',
              type=str, default='test_123456789', show_default=True)
@click.option('-u', '--user',
              help='User to connect to the ERP',
              type=str, default='admin', show_default=True)
@click.option('-p', '--password',
              help='Password to connect to the ERP',
              type=str)
@click.option('-s', '--separator',
              help='Separator for the CSV file',
              type=str, default=';', show_default=True)
@click.argument('filepath',
                type=str)
def import_file(host, port, database, user, password, separator, filepath):
    server_url = '{host}:{port}'.format(**locals())
    c = Client(server=server_url, db=database, user=user, password=password)
    import_from_csv(c, filepath, separator=separator)


if __name__ == '__main__':
    import_file()
