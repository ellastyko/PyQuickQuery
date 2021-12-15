
import sqlite3
"""
    Module was created to speed up development process and don't write long SQL queries 
"""


class Query:

    dialect : str
    dialects = ['default', 'sqlite3', 'mysql', 'postgre3'] 


    def __init__(self, database : object, dialect : str = 'default') -> None: # Parametr is mysql, sqlite or postrgre
        """
            database - object of ...

            type - sort of database like mysql, sqlite3, postgre3, etc.
        """
        try:
            self.db = database
            
            if dialect not in self.dialects:
                raise "Invalid dialect" # Make raise error
            self.dialect = dialect
            self.sql = self.db.cursor()
            self.db.row_factory = sqlite3.Row
        except Exception as e:
            print(f"Unable to connect to database: {e}!") 
        else:
            print('Connected')


    def make(self, query : str) -> object:
        """
            Execute SQL query
        """
        try:
            self.sql.execute(query)
        except Exception as e:
            print(f'Unable to execute query: {e}')
            self.db.rollback()
            raise Exception       
        else:
            self.db.commit()
            return self.sql 


    def create(self, table : str, data : dict) -> tuple:
        """
            Create row in special table

        """
        try:
            keys = ', '.join(self.__quotes(key) for key in data.keys())
            values = ', '.join(self.__quotes(value) for value in data.values())

            self.make(f"INSERT INTO {table}({keys}) VALUES({values})")
        except:
            print(f'Unable to insert data!')
        else:       
            self.make(f'SELECT * FROM {table} WHERE id={self.sql.lastrowid}')
            return self.sql.fetchone()


    def update(self, table : str, data : dict, where : dict = None) -> object:
        
        try:

            values = ', '.join (f"{key}={self.__quotes(value)}" for key, value in data.items())
            clauses = self.__build_clause(where)

            self.make(  f"UPDATE {table} SET " + values + clauses  )
        except:
            print('Unable to update data')
        else:
            self.make( f"SELECT * FROM {table} " + clauses )

            updated_data = self.sql.fetchall()

            if len(updated_data) > 1:
                return updated_data
            elif len(updated_data) == 1:
                return updated_data[0]

    
    def select(self, table : str, columns : list = '*', where : dict = None, order_by : dict = ['id', 'ASC']) -> list:
        """
            Select rows from special table

            :table - name of table in str format
            :columns - list of necessary columns (all columns by default)
            :
        """
        if type(columns) is list:
            columns = ', '.join(columns)

        clauses = self.__build_clause(where)
        order_by = self.__build_order_by(order_by)

        self.make( f"SELECT {columns} FROM " + table + clauses + order_by )

        return self.get 


    def delete(self, table : str, where : dict) -> None:

        self.make(f"DELETE FROM " + table + self.__build_clause(where))


    def get(self, limit : int = None) -> list:
        """
            Returns rows after select  

            :limit - number of rows
        """

        if limit is None:
            return self.sql.fetchall()
        elif type(limit) is int and limit > 0:
            return self.sql.fetchone() if limit == 1 else self.sql.fetchmany(limit)
        else:
            print('Invalid parametr')


    def __build_order_by(self, order_by):
        return " ORDER BY " + ' '.join(order_by)


    def __build_clause(self, where) -> str: # Returns 
        """
            Build WHERE clause  `WHERE clause AND clause` format
        """
        if where is not None:
            return ' WHERE ' + ' AND '.join(self.__key_value(where))
        else:
            return ''


    def __key_value(self, data : dict) -> list:
        """
            Present dict in   `key=value,` format
        """
        return [f"{key}={self.__quotes(value)}" for key, value in data.items()]


    def __quotes(self, field):

        if type(field) is not str:
            return field
         
        if self.dialect == 'mysql':
            return f"`{field}`" 
        else:
            return f"'{field}'"

    def __injection_checkup(self, query):
        """
            Check correction of SQL query :: in progress
        """
        pass

