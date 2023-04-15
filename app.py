from flask import Flask

app = Flask(__name__)
# установим секретный ключ для подписи.
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

import controllers.index
import controllers.data_editor
import controllers.problem_solver



if __name__ == '__main__':
    app.run()
