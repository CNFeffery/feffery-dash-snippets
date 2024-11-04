@app.server.route('/upload', methods=['POST'])
def upload():

    uploadId = request.values.get('uploadId')
    filename = request.files['file'].filename

    try:
        os.mkdir(os.path.join('caches', uploadId))
    except FileExistsError:
        pass
    with open(os.path.join('caches', uploadId, filename), 'wb') as f:
        for chunk in iter(lambda: request.files['file'].read(1024 * 1024 * 10), b''):
            f.write(chunk)

    return {'filename': filename}