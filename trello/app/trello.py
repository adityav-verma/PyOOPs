from app.constants import BoardPrivacy


class User(object):
    pass


class Trello:
    def create_board(self, name: str, privacy: BoardPrivacy) -> str: pass

    def update_board(self, id: str, name: str, privacy: BoardPrivacy) -> str: pass

    def show_board(self, id: str) -> dict: pass

    def add_members_to_board(self, id: str, user: User) -> str: pass

    def create_list(self, name: str, board_id: str) -> str: pass

    def show_list(self, id: str) -> dict: pass

    def create_card(self, name: str, description: str, list_id: str) -> str: pass

    def assign_user_to_card(self, id: str, user: User) -> str: pass

    def show_card(self, id: str) -> dict: pass

    def delete_board(self, id: str) -> None: pass

    def delete_list(self, id: str) -> None: pass

    def delete_card(self, id: str) -> None: pass

    def remove_members_from_board(self, id: str, user: User) -> None: pass

    def un_assign_user_from_card(self, id: str, user: User) -> None: pass
