@app.server.route('/download')
def download():

    path = request.args.get('path')

    if '..' in path:
        abort(403)

    filename = request.args.get('filename')

    return send_from_directory(path, filename)