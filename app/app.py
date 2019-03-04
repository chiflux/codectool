import urllib.parse
import base64
import binascii
from bottle import route, run, template, post, request, get, redirect, response, static_file

codecs = ["base64", "url", "hex"]

@get('/')
def index():
    mydict = request.query.decode()
    codec_name = None
    encoded = ''
    decoded = ''
    filename = ''
    if "codec" not in mydict: return getBase64()
    codec = mydict['codec']
    if "encoded" in mydict: encoded = mydict['encoded']
    if "decoded" in mydict: url_decoded = mydict['decoded']
    if codec == 'base64': codec_name = 'Base64'
    if codec == 'url': codec_name = 'URL'   
    if codec == 'hex': codec_name = 'HEX'   
    return template('form', codec=codec, codec_name=codec_name, encoded=encoded, decoded=decoded, filename=filename, codecs=codecs)

@get('/hex')
def getUrl():
    redirect('/?codec=hex')

@get('/url')
def getUrl():
    redirect('/?codec=url')

@get('/base64')
def getBase64():
    redirect('/?codec=base64')

@post('/hex')
def postUrl():    
    return postCodec("hex", request)

@post('/url')
def postUrl():    
    return postCodec("url", request)

@post('/base64')
def postBase64():
    return postCodec("base64", request)

def postCodec(codec, request):
    default_filename = codec + "_data"
    action = request.forms.get('action')
    codec = request.forms.get('codec')
    codec_name = request.forms.get('codec_name')
    filename = request.forms.get('filename')

    decoded = request.forms.get('decoded')
    if decoded==None: decoded=''
    encoded = request.forms.get('encoded')
    if encoded==None: encoded=''

    if action=='encode':
        data = request.files.data
        raw = None
        if data and data.file:
            raw = data.file.read() # This is dangerous for big files
            filename = data.filename
        else:
            raw = decoded.encode()
        if raw != None:
            if codec == "hex":
                encoded = binascii.hexlify(raw).upper()
            if codec == "base64":
                encoded = base64.b64encode(raw)
            if codec == "url":
                encoded = urllib.parse.quote_plus(raw.decode())
        return template('form', codec=codec, codec_name=codec_name, encoded=encoded, decoded=decoded, filename=filename, codecs=codecs)

    if action=='decode':
        if not filename: filename=default_filename
        response.content_type = 'application/octet-stream;'
        response.set_header('Content-Disposition', 'attachment; filename=' + filename)
        if codec == "hex":
            return binascii.unhexlify(encoded)
        if codec == "base64":
            return base64.b64decode(encoded)
        if codec == "url":
            return urllib.parse.unquote(encoded).encode()

    if action=='decode_text':
        if codec == "hex":
            decoded = binascii.unhexlify(encoded)
        if codec == "base64":
            decoded = base64.b64decode(encoded)
        if codec == "url":
            decoded =  urllib.parse.unquote(encoded)
        return template('form', codec=codec, codec_name=codec_name, encoded=encoded, decoded=decoded, filename=filename, codecs=codecs)

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='static')

run(host='0.0.0.0', port=8080)