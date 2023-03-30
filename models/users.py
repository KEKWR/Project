from sqlalchemy import text,sql,Boolean,DateTime,MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey, JSON
from sqlalchemy.dialects.postgresql import UUID


metadata = MetaData()

roles = Table(
    "roles",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("permissions", JSON),
)

users_table = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String(40), unique=True, index=True),
    Column("name", String(100)),
    Column("hashed_password", String()),
    Column(
        "is_active",
        Boolean(),
        server_default=sql.expression.true(),
        nullable=False,
    ),
    Column('role_id',Integer, ForeignKey("roles.id")),
)


tokens_table = Table(
    "tokens",
    metadata,
    Column("id", Integer, primary_key=True),
    Column(
        "token",
        UUID(as_uuid=False),
        server_default=text("uuid_generate_v4()"),
        unique=True,
        nullable=False,
        index=True,
    ),
    Column("expires", DateTime()),
    Column("user_id", ForeignKey("users.id")),
)