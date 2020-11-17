import peewee

db = peewee.SqliteDatabase('score.db')

class BaseModel(peewee.Model):
    class Meta:
        database = db

class Score(BaseModel):
    id = peewee.IntegerField(unique=True, index=True, primary_key=True)
    score = peewee.IntegerField(null=False)

if __name__ == '__main__':
    try:
        Score.create_table()
        print("Tabela de Score criada")
    except peewee.OperationalError:
        print("Tabela Score existente")