

"""
    Module was created to speed up development process and don't write long SQL queries 
"""


class Query:

    
    __query = ''
    dialect = 'default'
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
        except Exception as e:
            print(f"Unable to connect to database: {e}!") 
        else:
            print('Connected')


    def make(self, query) -> object:

        try:
            self.sql.execute(query)
        except Exception as e:
            print(f'Unable to execute query: {e}')
            self.db.rollback()
            raise Exception       
        else:
            self.db.commit()
            return self


    def create(self, table : str, data : dict) -> tuple:

        try:
            keys = ', '.join(f"{self.__quotes(key)}" for key in data.keys())
            values = ', '.join(f"{self.__quotes(value)}" for value in data.values())

            self.make(f"INSERT INTO {table}({keys}) VALUES({values})")
        except:
            print(f'Unable to insert data!')
        else:       
            self.make(f'SELECT * FROM {table} WHERE id={self.sql.lastrowid}')
            return self.sql.fetchone()


    def update(self, table : str, data : dict) -> object:
        
        # TODO Пофиксить апдейт

        try:
            values = self.__equality(data, condition = False)

            self.__query = f"UPDATE {table} SET {values}"
        except:
            print('Unable to update data')
        else:
            return self 

    
    def select(self, table : str, fields : list = '*', where : dict = None, order_by : dict = ['id', 'ASC']) -> list:
        
        if type(fields) is list:
            fields = ', '.join(fields)

        self.__query = f"SELECT {fields} FROM {table}{self.__build_clause(where)}{self.__build_order_by(order_by)}"
        print(self.__query)
        return self.get 


    def delete(self, table : str, where : dict) -> None:

        self.__query = f"DELETE FROM {table}{self.__build_clause(where)}"
        self.make(self.__query)


    def get(self, limit : int = None) -> list:
        """
            limit of rows
        """
        self.make(self.__query)

        if limit is None:
            return self.sql.fetchall()
        elif type(limit) is int and limit > 0:
            return self.sql.fetchone() if limit == 1 else self.sql.fetchmany(limit)
        else:
            print('Invalid get func')


    def __build_order_by(self, order_by):
        return " ORDER BY " + ' '.join(order_by)

    def __build_clause(self, where):
        if where is not None:
            clause = ' WHERE ' + ' AND '.join(f"{key}={self.__quotes(value)}" for key, value in where.items())
            return clause
        else:
            return ''

    def __quotes(self, field):

        if type(field) is not str:
            return field
         
        if self.dialect == 'mysql':
            return f"`{field}`" 
        else:
            return f"'{field}'"

