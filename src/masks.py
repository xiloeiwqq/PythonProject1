def get_mask_card_number(card_number: str) -> str:
    """маскировка номера карты"""
    card_str = str(card_number)
    masked_card = f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"
    return masked_card


def get_mask_account(account_number: str) -> str:
    """маскировка номера счета"""
    account_str = str(account_number)
    masked_account = f"**{account_str[-4:]}"
    return masked_account
