import sqlalchemy

metadata = sqlalchemy.MetaData()

contacts_table = sqlalchemy.Table(
    "Contact",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(32)),
    sqlalchemy.Column("description", sqlalchemy.String(128)),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime()),
    sqlalchemy.Column("updated_at", sqlalchemy.DateTime()),
)
