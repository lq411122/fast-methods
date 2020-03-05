from typing import List

from fastapi import HTTPException

from ..api.utils import per_page
from utils.mongodb import collection


def get_data_for_market(
        position: List[float] = None,
        pag: int = None):

    total = collection.find({"position": {"$nearSphere": position}}).count()

    # 判断输入的页码是否符合
    normal_page = total // per_page  # 每页够十条数据的页数
    total_page = normal_page if total % per_page == 0 else normal_page + 1
    last_page = total % per_page  # 最后一页市场个数

    if 0 < pag <= normal_page:
        pages = per_page
    elif pag == total_page:
        pages = last_page
    else:
        raise HTTPException(status_code=200, detail="查询页无数据")

    data = collection.aggregate([
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