from flask import Blueprint, jsonify, request
from functools import wraps
from app.controllers import (do_di_init, ai_init, ao_init, temp_init,
                             do_write, di_read, ao_write, ai_read, temp_read)

api = Blueprint('api', __name__, url_prefix='/api')


class need_args(object):
    def __init__(self, *args, **kwargs):
        super(need_args, self).__init__()
        self.args = args
        self.kwargs = kwargs

    def __call__(self, f):
        @wraps(f)
        def wrapped():
            for arg in self.args:
                if arg not in request.args:
                    return jsonify({'status': 'ERROR',
                                    'message': '{} needed'.format(arg)})
            return f()
        return wrapped


@api.route('/di', methods=['GET'])
@need_args('pin')
def di():
    pin = int(request.args.get('pin'))
    if 1 > pin or pin > 16:
        return jsonify({
            'status': 'ERROR',
            'message': 'Digital input pins for MedIOEx must be in [1, 16]'})

    do_di_init()
    result = di_read(pin)
    return jsonify({'status': 'OK',
                    'value': result})


@api.route('/do', methods=['GET'])
@need_args('pin', 'val')
def do():
    pin = int(request.args.get('pin'))
    val = int(request.args.get('val'))
    if 1 > pin or pin > 12:
        return jsonify({
            'status': 'ERROR',
            'message': 'Digital output pins for MedIOEx must be in [1, 12]'})
    elif val not in (0, 1):
        return jsonify({'status': 'ERROR',
                        'message': 'Digital outputs only accept 0 or 1.'})
    do_di_init()
    do_write(pin, val)
    return jsonify({'status': 'OK'})


@api.route('/ro', methods=['GET'])
@need_args('pin', 'val')
def ro():
    pin = int(request.args.get('pin'))
    val = int(request.args.get('val'))
    if 13 > pin or pin > 16:
        return jsonify({
            'status': 'ERROR',
            'message': 'Relay pins for MedIOEx must be in [13, 16]'})
    elif val not in (0, 1):
        return jsonify({'status': 'ERROR',
                        'message': 'Relay outputs only accept 0 or 1.'})

    do_di_init()
    do_write(pin, val)
    return jsonify({'status': 'OK'})


@api.route('/ai', methods=['GET'])
@need_args('pin')
def ai():
    pin = int(request.args.get('pin'))
    if 1 > pin or pin > 4:
        return jsonify({
            'status': 'ERROR',
            'message': 'Analog input pins for MedIOEx must be in [1, 4]'})

    ai_init()
    result = ai_read(pin)

    return jsonify({'status': 'OK',
                    'value': result})


@api.route('/ao', methods=['GET'])
@need_args('pin', 'val')
def ao():
    pin = int(request.args.get('pin'))
    val = int(request.args.get('val'))
    if 1 > pin or pin > 4:
        return jsonify({
            'status': 'ERROR',
            'message': 'Analog output pins for MedIOEx must be in [1, 4]'})
    elif 0 > val or val > 4095:
        return jsonify({
            'status': 'ERROR',
            'message': 'Analog outputs accept between 0 and 4095.'})

    ao_init()
    ao_write(pin, val)
    return jsonify({'status': 'OK'})


@api.route('/temperature', methods=['GET'])
def get_temperature():
    temp_init()
    result = temp_read(1)
    return jsonify({'status': 'OK', 'value': result})


@api.route('/close', methods=['GET'])
def close():
    ao_init()
    for pin in range(1, 5):
        ao_write(pin, 0)

    do_di_init()
    for pin in range(1, 16):
        do_write(pin, 0)

    return jsonify({'status': 'OK'})
