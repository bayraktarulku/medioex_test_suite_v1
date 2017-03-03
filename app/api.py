from flask import Blueprint, jsonify, request
from subprocess import Popen, PIPE
from config import IO_BINARY_PATH
from functools import wraps
import os

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

    p = Popen([os.path.join(IO_BINARY_PATH, 'di_read'), str(pin)],
              stdout=PIPE, stderr=PIPE)
    output = p.communicate()[0]
    try:
        return jsonify({'status': 'OK',
                        'value': int(output)})
    except:
        return jsonify({'status': 'ERROR',
                        'message': output})


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
    p = Popen([os.path.join(IO_BINARY_PATH, 'do_write'), str(pin), str(val)],
              stdout=PIPE, stderr=PIPE)
    output = p.communicate()[0]
    if output:
        return jsonify({'status': 'ERROR',
                        'message': output})
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
    p = Popen([os.path.join(IO_BINARY_PATH, 'do_write'), str(pin), str(val)],
              stdout=PIPE, stderr=PIPE)
    output = p.communicate()[0]
    if output:
        return jsonify({'status': 'ERROR',
                        'message': output})
    return jsonify({'status': 'OK'})


@api.route('/ai', methods=['GET'])
@need_args('pin')
def ai():
    pin = int(request.args.get('pin'))
    if 1 > pin or pin > 4:
        return jsonify({
            'status': 'ERROR',
            'message': 'Analog input pins for MedIOEx must be in [1, 4]'})
    p = Popen([os.path.join(IO_BINARY_PATH, 'ai_read'), str(pin)],
              stdout=PIPE, stderr=PIPE)
    output = p.communicate()[0]
    try:
        return jsonify({'status': 'OK',
                        'value': int(output)})
    except:
        return jsonify({'status': 'ERROR',
                        'message': output})


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

    p = Popen([os.path.join(IO_BINARY_PATH, 'ao_write'), str(pin), str(val)],
              stdout=PIPE, stderr=PIPE)
    output = p.communicate()[0]
    if output:
        return jsonify({'status': 'ERROR',
                        'message': output})
    return jsonify({'status': 'OK'})
