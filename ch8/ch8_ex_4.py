def show_magicians(magicians):
    """显示名称"""

    for name in magicians:
        print("" + name.title())


def make_great(magicians):
    """修改名称"""
    u_magicians = []
    i = 0
    for name in magicians:
        u_magicians.append('the Great ' + name)
        i += 1

    return u_magicians


magicians = ["MA", "MB"]
print("first show magicians ")
show_magicians(magicians)

print("update magicians ")
u_magicians = make_great(magicians[:])

print("second show magicians ")
show_magicians(magicians)

print("show update magicians")
show_magicians(u_magicians)
