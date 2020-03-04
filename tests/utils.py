from faker import Faker
from faker.providers import BaseProvider
from faker.providers.internet import ip_address, ip_network

fake = Faker('zh_CN')
fake.add_provider(ip_address)
fake.add_provider(ip_network)


# 要生成自定义数据请启用以下代码并进行相应修改

class CustomFakerProvider(BaseProvider):

    def methods(self):
        return {
                  "name": fake.name(),
                  "type": "true",
                  "uid": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                  "img_url": "string",
                  "is_authenticated": "true",
                  "contacts": [
                    {"mobile": fake.phone_number(),
                     "user_name": fake.user_name()
                    }
                  ],
                  "client_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                  "idcard": {
                    "id": "440923198604103767",
                    "front_url": fake.image_url(),
                    "back_url": "https://smartracing.oss-cn-hangzhou.aliyuncs.com/shared/images/idcard/full/15722634"
                  },
                  "isSubmit": "true",
                  "authenticate_time": "2020-02-29T17:55:20.833Z"
                }

    def market(self):
        return {
            "position": [120.123456, 30.123456]
        }


fake.add_provider(CustomFakerProvider)