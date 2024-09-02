from database.session import Base
from sqlalchemy import TIMESTAMP, Integer, DateTime, String, Boolean, text, Float, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True,
                                    nullable=False, unique=True)
    username: Mapped[str] = mapped_column(String(100),  nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=True, unique=True)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[DateTime] = mapped_column(TIMESTAMP(timezone=True), server_default=text(
        'CURRENT_TIMESTAMP'), nullable=False)
    updated_at: Mapped[DateTime] = mapped_column(TIMESTAMP(timezone=True), server_default=text(
        'CURRENT_TIMESTAMP'), onupdate=text('CURRENT_TIMESTAMP'), nullable=False)

    orders: Mapped[list["Order"]] = relationship(
        "Order", back_populates="user")
    cart_items: Mapped[list["CartItem"]] = relationship(
        "CartItem", back_populates="user")

    class Config:
        from_attributes = True


class Category(Base):
    __tablename__ = 'categories'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True,
                                    nullable=False, unique=True)
    category_name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=False)
    products: Mapped[list["Product"]] = relationship(
        "Product", back_populates="category")

    class Config:
        from_attributes = True


class CartItem(Base):
    __tablename__ = 'cart_items'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True,
                                    nullable=False, unique=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey(
        'users.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    product_id: Mapped[int] = mapped_column(Integer, ForeignKey(
        'products.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    created_at: Mapped[DateTime] = mapped_column(TIMESTAMP(timezone=True), server_default=text(
        'CURRENT_TIMESTAMP'), nullable=False)
    user: Mapped["User"] = relationship("User", back_populates="cart_items")

    class Config:
        from_attributes = True


class Product(Base):
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True,
                                    nullable=False, unique=True)
    product_name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=False)
    price: Mapped[Float] = mapped_column(Float, nullable=False)
    inventory_count: Mapped[int] = mapped_column(Integer, nullable=False)
    category_id: Mapped[int] = mapped_column(Integer, ForeignKey(
        'categories.id', ondelete='SET NULL', onupdate='CASCADE'))
    created_at: Mapped[DateTime] = mapped_column(TIMESTAMP(timezone=True), server_default=text(
        'CURRENT_TIMESTAMP'), nullable=False)
    updated_at: Mapped[DateTime] = mapped_column(TIMESTAMP(timezone=True), server_default=text(
        'CURRENT_TIMESTAMP'), onupdate=text('CURRENT_TIMESTAMP'), nullable=False)
    category: Mapped["Category"] = relationship(
        "Category", back_populates="products")

    class Config:
        from_attributes = True


class Order(Base):
    __tablename__ = 'orders'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True,
                                    nullable=False, unique=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey(
        'users.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    total_price: Mapped[Float] = mapped_column(Float)
    status: Mapped[Boolean] = mapped_column(
        Boolean, default=False, nullable=False)
    created_at: Mapped[DateTime] = mapped_column(TIMESTAMP(timezone=True), server_default=text(
        'CURRENT_TIMESTAMP'), nullable=False)
    updated_at: Mapped[DateTime] = mapped_column(TIMESTAMP(timezone=True), server_default=text(
        'CURRENT_TIMESTAMP'), onupdate=text('CURRENT_TIMESTAMP'), nullable=False)
    user: Mapped["User"] = relationship("User", back_populates="orders")
    items: Mapped[list["OrderItem"]] = relationship(
        "OrderItem", back_populates="order")

    class Config:
        from_attributes = True


class OrderItem(Base):
    __tablename__ = 'order_items'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True,
                                    nullable=False, unique=True)
    order_id: Mapped[int] = mapped_column(Integer, ForeignKey(
        'orders.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    product_id: Mapped[int] = mapped_column(Integer, ForeignKey(
        'products.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    price: Mapped[Float] = mapped_column(Float)
    order: Mapped["Order"] = relationship("Order", back_populates="items")

    class Config:
        from_attributes = True


class authenticated_user(Base):
    __tablename__ = "authenticated_users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=False,
                                    nullable=False, unique=True)

    class Config:
        from_attributes = True
