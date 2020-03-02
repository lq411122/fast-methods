from fastapi import Query, APIRouter
from starlette.status import HTTP_200_OK

from ...utils import JSONResponse

from app.api.mongo.dataInDB import get_data_for_market
from app.models.body_model import market_parm
from app.models.response_model import market_response

router = APIRouter()


@router.post("/shop",
             response_model=market_response,
             status_code=HTTP_200_OK)
async def market(
        pos: market_parm,
        pag: int = Query(1, description="查询页码")
):
    data = get_data_for_market(position=pos.position, pag=pag)
    l = list(data)[0]
    shop_list = l["data"]

    shop = []
    for i in range(len(shop_list)):
        name = shop_list[i]["name"]
        dis = round(shop_list[i]['dis'] / 1000, 4)
        distance = str(dis) + "km"
        shop.append({name: distance})

    return JSONResponse({
        "result":  {
                "shop_list": shop,  # 查询页市场列表
                "current_page": pag}  # 当前页
    })