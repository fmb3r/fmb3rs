# def strcounter(s): #сложность O(n**2)
#     for sym in set(s):
#         counter = 0
#         for sub_sym in s:
#             if sym == sub_sym:
#                 counter += 1
#         print(sym, "-", counter)
#
# strcounter('asdvhgfa')

def strcounter2(s):
    syms_counter = {}
    for sym in s:
        syms_counter[sym] = syms_counter.get(sym, 0) + 1
    for sym, count in syms_counter.items():
        print(sym, '-', count)

strcounter2('qwwweeerrrtyyy')