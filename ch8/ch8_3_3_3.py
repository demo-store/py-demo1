def get_formatter_name(first_name, last_name, middle_name = ''):
    """获取整洁的名称"""
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()


musician = get_formatter_name("jimi", "hendrix")
print(musician)

musician = get_formatter_name('john', 'hooker', 'lee')
print(musician)
