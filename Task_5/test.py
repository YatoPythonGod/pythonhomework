# def printer(*args):
#     print(args)
#
# lst_prog_lang = ['Python', 'Java', 'C', 'C++', 'C#', 'JavaScript', 'Go']
# range_num = list(range(1, len(lst_prog_lang) + 1))
#
# printer(lst_prog_lang, range_num)

def cash_func(func):
    def wrapper(*args, **kwargs):
        cash = {}
        if args in cash:
            return cash[args]
        else:
            cash[args] = func(args)
        return wrapper

    return cash_func


@cash_func
def multi(num):
    return num ** 10


print(multi(2222))
