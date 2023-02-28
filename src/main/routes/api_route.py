from flask import Blueprint, jsonify, request
from src.main.composer import register_user_composer
from src.main.adapter import flask_adapter


api_routes_bp = Blueprint("api_routes", __name__)


@api_routes_bp.route("/test", methods=["POST"])
def testing():
    """Test."""
    return jsonify(
        {"Programmer": "Marcosls", "message": request.args.to_dict()}
    )


@api_routes_bp.route("/api/users", methods=["POST"])
def register_user():
    """register."""
    response = flask_adapter(request=request)

    msg = {"Type": "users", "id": response.body.id, "attr": response.body.name}

    return jsonify({"data": msg}), response.status_code
