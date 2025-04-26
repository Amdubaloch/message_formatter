def funny_deco(func):
    def wrapper(message):
        border = " 🦧 🗣️" * (len(message) //2)
        return f"{border}\n 🤓 {message} 🥱\n {border}"
    return wrapper


def PyarBhara_deco(func):
    def wrapper(message):
        return f"💓💨💃 {message} 💓💨💃"
    return wrapper
