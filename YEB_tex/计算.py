from settings import zonghe, zonghe_scope, once_scope, once


def math_scope_tex_once(yeb):
    yeb_1 = yeb / 12
    print(yeb_1)
    for i in range(len(once_scope)):
        if once_scope[i] >= yeb_1:
            return once[i]
    else:
        return once[len(once_scope)]  # 当大于80000 时候的情况


def once_tex(yeb):
    """
    :param yeb: 年终奖
    :return: 税额
    """
    tex, tf_num = math_scope_tex_once(yeb)  # tf_num 扣除数
    print("你的年终奖金为{0}， 扣除税率为{1}， 速算扣除数为{2}， 总计扣除税为{3}".format(yeb, tex, tf_num, yeb * tex - tf_num))
    return yeb * tex - tf_num


print(once_tex(12 * 80000.1))


def math_scope_tex_zonghe(math_tex_base):
    for i in range(len(zonghe_scope)):
        if zonghe_scope[i] >= math_tex_base:
            return zonghe[i]
    else:
        return zonghe[len(zonghe_scope)]  # 最后边界情况


def math_tex_base(yearly_salary, yeb, *args):
    year_tex_salary_base = yearly_salary - 60000  # 扣除基本减除费用 5000 起征点 * 12
    all_tex_salary = year_tex_salary_base + yeb
    if args:
        print(args)
        for i in args:
            all_tex_salary -= i
    print(all_tex_salary)
    return all_tex_salary


def zonghe_tex(yearly_salary, yeb, *args):
    """
    yearly_salary: 年薪
    yeb: 年终奖
    *args: 其他扣除费用 （社保、公积金等专项扣除）（专项附加扣除，房租+赡养老人项）
    :return: 税额
    """
    tex_base = math_tex_base(yearly_salary, yeb, *args)
    tex, tf_num = math_scope_tex_zonghe(tex_base)  # tf_num 速算扣除数
    print("你的年终奖税率基数为{0}， 扣除税率为{1}， 速算扣除数为{2}， 总计扣除税为{3}".format(tex_base, tex, tf_num, tex_base * tex - tf_num))
    return yeb * tex - tf_num


zonghe_tex(120000, 30000, 30000, 42000)
