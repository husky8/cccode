import numpy as np

def getWilsonScore(pos, total, p_z=2.):
    """
    威尔逊得分计算函数
    参考：https://en.wikipedia.org/wiki/Binomial_proportion_confidence_interval
    :param pos: 正例数
    :param total: 总数
    :param p_z: 正太分布的分位数
    :return: 威尔逊得分
    """
    pos_rat = pos * 1. / total * 1.  # 正例比率
    score = (pos_rat + (np.square(p_z) / (2. * total))
             - ((p_z / (2. * total)) * np.sqrt(4. * total * (1. - pos_rat) * pos_rat + np.square(p_z)))) / \
            (1. + np.square(p_z) / total)
    return score
if __name__ == '__main__':
    print(getWilsonScore(4,5))


