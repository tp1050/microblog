from flask import Flask, make_response, jsonify, request, redirect, url_for
from flask.views import MethodView
from app import inventory

class InventoryApi(MethodView):
    """ /api/inventory """

    def get(self):
        """ Return the entire inventory collection """
        return make_response(jsonify(inventory), 200)

    def delete(self):
        """ Delete the entire inventory collection """
        inventory.clear()
        print(inventory)
        return make_response(jsonify({}), 200)


class InventoryItemApi(MethodView):
    """ /api/inventory/<item_name> """

    error = {
        "itemNotFound": {
            "errorCode": "itemNotFound",
            "errorMessage": "Item not found"
        },
        "itemAlreadyExists": {
            "errorCode": "itemAlreadyExists",
            "errorMessage": "Could not create item. Item already exists"
        }
    }

    def get(self, item_name):
        """ Get an item """
        if not inventory.get(item_name, None):
            return make_response(jsonify(self.error["itemNotFound"]), 400)
        return make_response(jsonify(inventory[item_name]), 200)

    def post(self, item_name):
        print('poooooooooost')
        print(request.data)
        body = request.get_json()
        print(23232)
        print("dsdsdss"+body)
        print(23232)

        """ Create an item """
        if inventory.get(item_name, None):
            return make_response(jsonify(self.error["itemAlreadyExists"]), 400)
        body = request.get_json()
        print(body)
        inventory[item_name] = {"description": body.get("description", None), "qty": body.get("qty", None)}
        return make_response(jsonify(inventory[item_name]))

    def put(self, item_name):
        """ Update/replace an item """
        body = request.get_json()
        inventory[item_name] = {"description": body.get("description", None), "qty": body.get("qty", None)}
        return make_response(jsonify(inventory[item_name]))

    def patch(self, item_name):
        """ Update/modify an item """
        if not inventory.get(item_name, None):
            return make_response(jsonify(self.error["itemNotFound"]), 400)
        body = request.get_json()
        inventory[item_name].update({"description": body.get("description", None), "qty": body.get("qty", None)})
        return make_response(jsonify(inventory[item_name]))

    def delete(self, item_name):
        """ Delete an item """
        if not inventory.get(item_name, None):
            return make_response(jsonify(self.error["itemNotFound"]), 400)
        del inventory[item_name]
        return make_response(jsonify({}), 200)
