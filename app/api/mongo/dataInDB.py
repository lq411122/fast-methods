from typing import List
from config.testing import db_client, per_page


def get_data_for_market(
        position: List[float] = None,
        pag: int = None):

    total = db_client.test.shop_list.find({"position": {"$nearSphere": position}}).count()

    # 判断输入的页码是否符合
    normal_page = total // per_page  # 每页够十条数据的页数
    total_page = normal_page + 1  # 总页数
    last_page = total % per_page  # 最后一页市场个数

    if 0 < pag <= normal_page:
        pages = per_page
    elif pag == total_page:
        pages = last_page
    else:
        return "请输入正确的页码"

    data = db_client.test.shop_list.aggregate([
        {"$geoNear": {"near": position,
                      "distanceField": "dis",
                      "includeLocs": "loc",
                      "spherical": True,
                      "distanceMultiplier": 6378137,
                      "maxDistance": 100000000 / 6378137}},
        {"$sort": {"dis": -1}},
        {"$skip": per_page * (pag - 1)},
        {"$limit": pages},
        {"$project": {
            "tmp": {
                "name": '$name',
                "position": '$position',
                "dis": "$dis",
                "loc": '$loc'
            }}},
        {"$group": {"_id": "null", "total": {"$sum": 1}, "data": {"$push": '$tmp'}}}

    ])

    return data