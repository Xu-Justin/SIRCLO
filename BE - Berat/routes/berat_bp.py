from flask import Blueprint

from controllers import BeratController

berat_bp = Blueprint('berat_bp', __name__)

berat_bp.route('/index', methods=['GET'])(BeratController.index)

berat_bp.route('/show/<tgl>', methods=['GET'])(BeratController.show)

berat_bp.route('/add', methods=['GET'])(BeratController.add_form)
berat_bp.route('/add', methods=['POST'])(BeratController.add)

berat_bp.route('/update/<tgl>', methods=['GET'])(BeratController.update_form)
berat_bp.route('/update/<tgl>', methods=['POST'])(BeratController.update)

berat_bp.route('/delete', methods=['POST'])(BeratController.delete)