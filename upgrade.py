with open('jamo.pydict', 'rb') as f:
    jamodict = pickle.load(f)

def encode_review(text):
    text = decompose_string(text)
    print(text)
    text = to_index_array(text, jamodict)
    print(text)
    text = padding(text, MAX_LEN)
    print(text)
    return text


def predict(text):
    model = tf.keras.models.load_model('models/latest-yok-detect-model.h5')
    graph = tf.get_default_graph()
    indices = encode_review(text)
    indices = np.array([indices])
    with graph.as_default():
        result = model.predict_classes(indices)
    poornag = ''
    if result == 0:
        poornag = '욕아님'
    else:
        poornag = '욕'
    return poornag

@app.route('/chk', methods=['POST'])
def upload_train():
    data = request.get_json()
    print(data['text'])
    sample = data['text']
    sample.split(' ')
    answer = []
    for part in sample:
        poornag = predict(part)
        if poornag != 0:
            answer.append(part)
    response = Response()
    response.headers[
        'Access-Control-Allow-Headers'] = 'Access-Control-Allow-Headers, Origin, X-Requested-With, Content-Type, Accept, Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS, HEAD'

    return answer, 200

@app.route('/')
def index():
    return render_template('index.html')

app.run(port=5000, host='0.0.0.0', debug=True, threaded=True)
