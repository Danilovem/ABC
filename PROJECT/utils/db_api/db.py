import sqlite3

# r"C:\Users\Egor\PycharmProjects\Robert_the_helper\utils\db_api\questions.db"
class DataBase:
    def __init__(self, path_to_db=r"C:\Users\Egor\PycharmProjects\Robert_the_helper\utils\db_api\questions.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = tuple()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        cursor.execute(sql, parameters)
        data = None
        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()
        connection.close()
        return data

    def create_table_questions(self):
        sql = '''
        CREATE TABLE Questions (
        id INTEGER PRIMARY KEY,
        question TEXT NOT NULL,
        answer TEXT
        );  
        '''
        self.execute(sql, commit=True)

    def add_question(self, q: str, ans: str = None):
        if ans is None:
            ans = "Пока что ответа на данный вопрос нет, но скоро он появится!"
        sql = "INSERT INTO Questions (question, answer) VALUES (?, ?)"
        q = "<b>" + q + "</b>"
        parameters = (q, ans,)
        self.execute(sql, parameters, commit=True)

    def select_all_questions(self):
        sql = "SELECT * FROM Questions"
        return self.execute(sql, fetchall=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def select_question(self, id: int = None, q: str = None):
        if id:
            sql = "SELECT * FROM Questions WHERE id=?"
            return self.execute(sql, parameters=(id,), fetchone=True)
        if q:
            sql = "SELECT * FROM Questions WHERE question=?"
            return self.execute(sql, parameters=(q,), fetchone=True)

    def add_answer(self, ans, q):
        sql = "UPDATE Questions SET answer=? WHERE question=?"
        return self.execute(sql, parameters=(ans, q), commit=True)

    def delete_question(self, q: str = None, id: int = None):
        if q:
            sql = "DELETE FROM Questions WHERE question=?"
            return self.execute(sql, parameters=(q,), commit=True)
        if id:
            sql = "DELETE FROM Questions WHERE id=?"
            return self.execute(sql, parameters=(id,), commit=True)

    def delete_all(self):
        return self.execute("DELETE FROM Questions WHERE True", commit=True)

    def delete_table(self):
        return self.execute("DROP TABLE Questions", commit=True)


def logger(statement):
    print(f'''
-------------------------------------------
Executing:
{statement}

-------------------------------------------
''')
