

#  Module was created to speed up development process and don't write long SQL queries 


class Query():

    __CurrentQuery = ''

    def __init__(self, db : object) -> None: # Parametr is mysql, sqlite or postrgre
        try:
            self.db = db
            self.sql = self.db.cursor()
            # self.__subquery = SubQuery()
        except Exception as e:
            print(f"Unable to connect to database: {e}!") 
        else:
            print('Connected')


    # Function with executing of 
    def make(self, query) -> object:

        try:
            self.sql.execute(query)
        except:
            self.db.rollback()
        else:
            self.db.commit()
            return self
 

    # Main operations with DB
    def create(self, table : str, data : dict):

        try:
            keys = self.__commas(data.keys(), quotes=True) 
            values = self.__commas(data.values(), quotes=True) 

            print(f"INSERT INTO {table}({keys}) VALUES({values})")
            self.make(f"INSERT INTO {table}({keys}) VALUES({values});")
        except Exception as e:
            print(f'Unable to insert data: {e}')
        else:
            return 0


    def update(self, table : str, data : dict) -> object:
        
        try:
            values = self.__equality(data, condition = False)

            print(f"UPDATE {table} SET {values}")
            self.__CurrentQuery = f"UPDATE {table} SET {values}"
        except:
            print('Unable to update data')
        else:
            return self

    
    def select(self, table : str, fields : list) -> object:
        
        fields = self.__commas(fields)         
        self.__CurrentQuery = f"SELECT {fields} FROM {table}"
        return self


    def where(self, conditions : dict):
        if self.__CurrentQuery != '':
            conditions = self.__equality(conditions)
            self.__CurrentQuery += conditions
            print(self.__CurrentQuery)
            return self
        else:
            print('Cannt use where!')


    def first(self) -> tuple:
        return self.sql.fetchone()

    def get(self, limit : int = None) -> list:
        self.make(self.__CurrentQuery)
        if limit:
            return self.sql.fetchmany(limit)
        else:
            return self.sql.fetchall()




    # Helpers 
    def __equality(self, dictionary : dict, condition : bool = True) -> str:


        string = ' WHERE ' if condition is True else ''

        for key, field in enumerate(dictionary.keys()):

            # Check up if value is string or integer/decimal
            if type(dictionary[field]) is str:
                value = f'"{dictionary[field]}"'
            else:
                value = dictionary[field]

            c = '' if key == len(dictionary) - 1 or condition is False else ' AND '

            string += f"{field}={value}{c}"


        return string


    def __commas(self, arr : list, quotes : bool = False) -> str:

        string = ''
        if quotes is False:
            for key, value in enumerate(arr):
                if key == len(arr) - 1:
                    string += value
                else:
                    string += f'{value}, '
        else:
            for key, value in enumerate(arr):
                if key == len(arr) - 1:
                    string += f'"{value}"'
                else:
                    string += f'"{value}", '


        return string

