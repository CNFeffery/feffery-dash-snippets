@app.server.route('/stream')
def stream():

    def _stream():
        for i in range(999):
            time.sleep(0.5)
            yield 'data: {}\n\n'.format(time.time())

    return Response(_stream(), mimetype='text/event-stream')