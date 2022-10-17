from Menu import Menu
from UserInterface import UserInterface
from MenuRepository import MenuRepository
from Order import Order


def test_get_total_price():
    # Arrange
    menu_repository = MenuRepository()
    user_interface = UserInterface(menu_repository)
    menu1 = Menu(1, "Test 1", 10.50)
    order = Order(1,1)

    # Act
    menu_repository.set_menu_item(menu1)    

    # Assert
    assert user_interface.get_total_price(order) == 10.5
    assert type(user_interface.get_total_price(order)) == float



def test_get_user_input(monkeypatch):
    # Arrange
    menu_repository = MenuRepository()
    user_interface = UserInterface(menu_repository)
    menu1 = Menu(1, "Test 1", 10.50)
    monkeypatch.setattr('builtins.input', lambda _: "1 1")


    # Act
    menu_repository.set_menu_item(menu1)    
    order = user_interface.get_user_input()

    # Assert
    assert user_interface.get_user_input().code == 1
    assert user_interface.get_total_price(order) == 10.5


