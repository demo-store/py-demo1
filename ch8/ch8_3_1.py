def get_formatted_name(first_name, last_name):
    """返回完整的名字"""
    full_name = first_name + ' ' + last_name
    return full_name.title()


musician = get_formatted_name('Jimi', 'hendrix')
print(musician)
