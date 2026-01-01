def filter_by_state(list_state: list[dict], state: str = "EXECUTED") -> list[dict]:
    filter_lists = []
    for el in list_state:
        if el["state"] == state:
            filter_lists.append(el)

    return filter_lists
