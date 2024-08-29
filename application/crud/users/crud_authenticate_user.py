from sqlalchemy import func, text
from sqlalchemy.orm import Session
from utils.password_hash import verify_password_bcrypt


def crud_authenticate_user(user_data, db: Session) -> int:
    sql_command = text("""
        SELECT authenticate_user(:username, :email, :password);
    """)

    user_id = db.execute(sql_command, {
        'email': user_data.email,
        'password': user_data.password_hash
    }).scalar()
    db.commit()
    return user_id


def validate_user_status(user_email, db: Session) -> bool:
    sql_command = text("""SELECT validate_user_status(:email);""")
    status = db.execute(sql_command, {
        'email': user_email
    }).scalar()
    db.commit()
    return status


def verify_user_password(user_password, user_email, db: Session) -> bool:
    sql_command = text("""SELECT get_user_password(:email);""")
    stored_password = db.execute(sql_command, {
        'email': user_email
    }).scalar()
    db.commit()
    isTrue = verify_password_bcrypt(stored_password, user_password)
    return isTrue
