"""

Problem Statement

The objective is to design and implement an in-memory SQL-like database, which should support the following set of operations / functionality:

It should be possible to create or delete tables in a database.
A table definition comprises columns which have types. They can also have constraints
The supported column types are string and int.
The string type can have a maximum length of 20 characters.
The int type can have a minimum value of -1024 and a maximum value of 1024.
Support for mandatory fields (tagging a column as required)
It should be possible to insert records in a table.
It should be possible to print all records in a table.
It should be possible to filter and display records whose column values match a given value.



# Components

- Database
  - Table -> table interface
    - Columns (String, Integer, ... ) -> interface
      - type (ENUM)
      - value (ENUM)
      - contraints
            - ColumnType (STRING, INT)
              - contraints

OperationsL
Database
  - CRUD of Table
Table:
  - NO alter operations
  - insert operations
  - read or read with filter operations (optimisations if possible)
"""

from abc import ABC, abstractmethod


class ColumnTypeInterface(ABC):
    @abstractmethod
    def is_valid(self):
        pass

    # TOOD


class ContraintInteface(ABC):
    @abstractmethod
    def is_valid(self, column, table) -> bool: pass


class ColumnInterface(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def type(self) -> ColumnTypeInterface:
        pass

    @abstractmethod
    def is_valid(self, value, table):
        pass


class TableInterface(ABC):
    @property
    @abstractmethod
    def columns(self): pass

    @abstractmethod
    def insert(self, values): pass

    @abstractmethod
    def select(self, filters={}): pass


class DatabaseInterface(ABC):
    @abstractmethod
    def show_tables(self):
        pass

    @abstractmethod
    def create_table(self, name, columns): pass

    @abstractmethod
    def select(self, table_name, filters={}): pass


class StringColumnType(ColumnTypeInterface):
    def __init__(self, max_length=20):
        self._max_length = max_length

    def is_valid(self, value):
        return len(value) <= self._max_length


class IntegerColumnType(ColumnTypeInterface):
    def __init__(self, min_value=-1024, max_value=1024):
        self._min_value = min_value
        self._max_value = max_value

    def is_valid(self, value):
        if value < self._min_value:
            return False
        if value > self._max_value:
            return False
        return True


class Column(ColumnInterface):
    def __init__(self, name, column_type: ColumnTypeInterface):
        self._type = column_type()
        self._name = name

    @property
    def name(self):
        return self._name

    @property
    def type(self) -> ColumnTypeInterface:
        return self._type

    def is_valid(self, value, table):
        return self._type.is_valid(value)
        #  have some column level checks here


class Table(TableInterface):
    def __init__(self, name, columms):
        self._name = name
        self._columns, self._column_map = [], {}
        for column in columms:
            temp_column = Column(column['name'], column['type'])
            self._columns.append(temp_column)
            self._column_map[column['name']] = temp_column
        self._rows = []

    @property
    def columns(self):
        return self._columns

    def insert(self, values):
        temp_row = {}
        for name, value in values.items():
            if name not in self._column_map:
                raise Exception('Invalid column')
            column = self._column_map[name]
            is_valid = column.is_valid(value, self)
            if not is_valid:
                raise Exception('Column costraints failed')
            temp_row[name] = value
        self._rows.append(temp_row)

    def select(self, filters={}):
        # {'name': value, 'col_name': value}
        if not filters:
            return list(self._rows)
        temp_result = []
        # O(c*n)
        for row in self._rows:
            filtered = True
            for col_name, value in filters.items():
                if col_name not in self._column_map:
                    raise Exception('Invalid filter column')
                if row[col_name] != value:
                    filtered = False
            if filtered:
                temp_result.append(dict(row))
        # for col_name, value in filters.items():
        #     if col_name not in self._column_map:
        #         raise Exception('Invalid filter column')
        #     for row in self._rows:
        #         if row[col_name] == value:
        #             temp_result.append(dict(row))
        return temp_result


class Database(DatabaseInterface):
    def __init__(self, name):
        self._name = name
        self._tables = {}

    def show_tables(self):
        return dict(self._tables)

    def create_table(self, name, columns):
        table = Table(name, columns)
        self._tables[name] = table
        return table

    def select(self, table_name, filters={}):
        if table_name not in self._tables:
            raise Exception('Invalid table name')
        table = self._tables[table_name]
        return table.select(filters)


db = Database('test_db')
table = db.create_table('test_table', [{'name': 'string_col_1', 'type': StringColumnType},
                                       {'name': 'int_col_1', 'type': IntegerColumnType}])
print(table.columns)
print(table.columns[0].name, table.columns[0].type)
print(table.columns[1].name, table.columns[1].type)

table.insert({'string_col_1': 'hello', 'int_col_1': 1})
# print(table.select())

# table.insert({'string_col_1': 'hello', 'int_col_1': 90000})
# table.insert({'string_col_1': 'hellohellohellohellohellohellohellohellohellohello', 'int_col_1': 1})
table.insert({'string_col_1': 'world', 'int_col_1': 300})

print(table.select({'string_col_1': 'world', 'int_col_1': 1}))

"""
index =
int_col_1: {
    value1: [row1, row2],
    value2: [row1, row2]
}

- delete row with string- this
  data_store.delte(row) -> row
  data = {'col1': val1, 'col2': val2}

  # have to udpate the index for all values in the row
  iterate thorught values and update the idnex
  -


UniqueContarint(self, table, col):
index[col_name[value]] = [row]
"""
