


from src.message_formatter.message_formatter import PyarBhara_deco, funny_deco

@funny_deco
def prnt_message(message):
    return message

print(prnt_message("Hello World"))


@PyarBhara_deco
def prant_massage(message):
    return message

print(prant_massage("kesy ho tum"))


