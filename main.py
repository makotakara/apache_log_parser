from flask import Flask
from flask import render_template
from collections import Counter
from flask import request
import re


app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    data = open('/var/log/apache2/access.log').read()
    # data = open('access.log').read()

    pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    ips = re.findall(pattern, data)

    result = Counter(ips).most_common(100)

    ban = []
    for key, value in result:
        if value > 1:
            ban.append({'ip': key, 'frequency': value})

    return render_template('index2.html', ips=ban)


if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0')
