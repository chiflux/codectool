<!DOCTYPE html>
<html lang="en">
<head>
    <link rel="stylesheet" href="/static/chiflux.css" type="text/css">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>URL Encoder / Decoder</title>

    <style>
    </style>

</head>
<body>

<span>Select codec:&nbsp;</span>
% for a_codec in codecs:
    <span><a href="/{{ a_codec }}">{{ a_codec }}</a></span>&nbsp;
% end
<form action="/{{ codec }}" name="endecoder" method="post" enctype="multipart/form-data" >
    <input type="hidden" name="codec" value="{{ codec }}" />
    <input type="hidden" name="codec_name" value="{{ codec_name }}" />
    <h3>{{ codec_name }} Codec</h3>
    <div>
        <span>Decoded data</span><br/>
        <textarea name="decoded" cols="80" rows="10" >{{ decoded }}</textarea><br/>
        <input type="file" name="data" size="40" />
    </div>
    <div style="margin-top: 20px; margin-bottom: 20px;">
        <button type="submit" name="action" value="encode" style="diplay: inline;" >Encode! 👇</button>
        <button type="submit" name="action" value="decode_text" style="diplay: inline;" >Decode as Text! 👆</button>
        <button type="submit" name="action" value="decode" style="diplay: inline;" >Decode as File! 💾</button>
    </div>
    <div>
        <span>Encoded data</span><br/>
        <textarea name="encoded" cols="80" rows="10" >{{ encoded }}</textarea><br/>
        <span class="label">Filename:&nbsp;<input name="filename" value="{{ filename }}" /></span>
    </div>

</form>

<div class="copyright">
    © 2019 chiflux
</div>

</body>
</html>
