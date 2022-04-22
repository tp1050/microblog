from flask import Flask
from conf import Conf
from constructs.inventory import Inventory
# from flask_login import LoginManager
app = Flask(__name__,)
logs=[]


app.config.from_object(Conf)
# from views import InventoryApi,InventoryItemApi
#
# app.add_url_rule("/api/inventory",view_func=InventoryApi.as_view("inventory_api"))
# app.add_url_rule("/api/inventory/<item_name>",view_func=InventoryItemApi.as_view("inventory_item_api"))
# login_manager=LoginManager()
# login_manager.init_app(app)

from app import routes
