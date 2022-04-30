from flask import Flask
from conf import Conf
from constructs.inventory import Inventory
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
# from flask_login import LoginManager
app = Flask(__name__,instance_relative_config=True)
logs=[]
db = SQLAlchemy(app)
migrate = Migrate(app, db)

app.config.from_object(Conf)
os.makedirs(os.path.join(app.instance_path, 'img'), exist_ok=True)
os.makedirs(os.path.join(app.instance_path, 'doc'), exist_ok=True)
os.makedirs(os.path.join(app.instance_path, 'sound'), exist_ok=True)
os.makedirs(os.path.join(app.instance_path, 'code'), exist_ok=True)
os.makedirs(os.path.join(app.instance_path, 'misc'), exist_ok=True)


# from views import InventoryApi,InventoryItemApi
#
# app.add_url_rule("/api/inventory",view_func=InventoryApi.as_view("inventory_api"))
# app.add_url_rule("/api/inventory/<item_name>",view_func=InventoryItemApi.as_view("inventory_item_api"))
# login_manager=LoginManager()
# login_manager.init_app(app)

from app import routes
