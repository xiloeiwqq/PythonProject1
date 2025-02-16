import re


def mask_card_number(number: str) -> str:
    return number[:4] + " " + number[4:6] + "** **** " + number[-4:]


def mask_account_number(number: str) -> str:
    return "**" + number[-4:]


def mask_account_card(card_info: str) -> str:
    card_pattern = re.compile(r"(Visa|Maestro) (\d{16})")
    account_pattern = re.compile(r"(Счет) (\d{20})")

    card_match = card_pattern.match(card_info)
    if card_match:
        card_type, card_number = card_match.groups()
        return f"{card_type} {mask_card_number(card_number)}"

    account_match = account_pattern.match(card_info)
    if account_match:
        account_type, account_number = account_match.groups()
        return f"{account_type} {mask_account_number(account_number)}"

    return card_info


def get_date(date: str) -> str:
    date_form = f"{date[8:10] + '.' + date[5:7] + '.' + date[2:4]}"
    if "T" in date:
        date = date.split("T")[0]
    return date_form
