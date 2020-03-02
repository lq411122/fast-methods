import json
import re


from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from app.models.body_model import methods_parm

router = APIRouter()


# 转小驼峰
def to_xtf(str):
    res = re.match(r"[a-zA-Z]+_.+", str.group())

    if res:
        return re.sub(r"_\S", lambda x: x.group().replace("_", "").upper(), res.group())
    return str.group().replace("_", "")


# 转下画线
def to_xhx(str):
    res = re.match(r".*[a-z][A-Z].*", str.group())
    if res:
        return re.sub(r"([a-z])([A-Z])", lambda x: x.group(1) + "_" + x.group(2).lower(), res.group())
    ls = list(str.group())
    if (ls[1] == "i") and (ls[2] == "d") and (ls[3] == '"'):
        ls.insert(1, "_")
    return "".join(ls)


@router.post("/trans/{trans_name}")
def translation(
        trans_name: str,  # Path参数
        parm: methods_parm  # Request Body参数
):
    # 接收数据
    json_data = jsonable_encoder(parm)
    # json数据转字符串
    data = json.dumps(json_data)
    if trans_name == "to_xtf":
        t1 = re.sub(r"\w+\"\s*:", to_xtf, data)
    elif trans_name == "to_xhx":
        t1 = re.sub(r"\"[a-zA-Z0-9]+\"\s*:", to_xhx, data)

    result = json.loads(t1)
    return result


