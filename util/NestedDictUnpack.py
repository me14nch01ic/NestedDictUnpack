def unpack(data: dict, parent_key: str = None):

    items: dict = {}

    for key, value in data.items():
        new_key = f'{parent_key}_{key}' if parent_key else key
        if isinstance(value, dict):
            items.update(unpack(value, new_key))
        else:
            items[new_key] = value

    return items