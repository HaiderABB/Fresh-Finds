from sqlalchemy import func, text
from sqlalchemy.orm import Session


def register_user(user_data, db: Session):

    # sql_command = text("""
    #     SELECT register_user(:username, :email, :password);
    # """)

    # db.execute(sql_command, {
    #     'username': user_data.username,
    #     'email': user_data.email,
    #     'password': user_data.password_hash
    # })

    # Commit the transaction to ensure the changes are saved
    db.commit()


def validate_user(user_email, db: Session) -> bool:
    sql_command = text("""SELECT validate_user(:email)""")
    result = db.execute(sql_command, {'email': user_email})
    db.commit()
    return result.scalar()
