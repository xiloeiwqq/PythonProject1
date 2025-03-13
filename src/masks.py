import logging
import os

if not os.path.exists('logs'):
    os.makedirs('logs')

logger = logging.getLogger('masks')
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('logs/masks.log', mode='w')
file_handler.setLevel(logging.DEBUG)

file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)

logger.addHandler(file_handler)

def get_mask_card_number(card_number: str) -> str:
    """маскировка номера карты"""
    card_str = str(card_number)
    masked_card = f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"
    logger.info(f"Маскированный номер карты: {masked_card}")
    return masked_card



def get_mask_account(account_number: str) -> str:
    """маскировка номера счета"""
    account_str = str(account_number)
    masked_account = f"**{account_str[-4:]}"
    logger.info(f"Маскированный номер счета: {masked_account}")
    return masked_account


print(get_mask_account('36172638712'))
print(get_mask_card_number('2737193628281631'))
