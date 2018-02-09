import os

from flask import Flask, jsonify, request, render_template


extra_dirs = ['../frontend/dist/', '../frontend/dist/static/']
extra_files = extra_dirs[:]
for extra_dir in extra_dirs:
    for dirname, dirs, files in os.walk(extra_dir):
        for filename in files:
            filename = os.path.join(dirname, filename)
            if os.path.isfile(filename):
                extra_files.append(filename)

app = Flask(__name__, static_folder='../frontend/dist/static',
            template_folder='../frontend/dist')


products = {
    '/cat1': [
        {'id': 1, 'image': 'https://images.unsplash.com/photo-1453831362806-3d5577f014a4', 'name': '商品一', 'description': '一個不錯的商品', 'price': 1000},
        {'id': 2, 'image': 'https://images.unsplash.com/photo-1473093226795-af9932fe5856', 'name': '商品二', 'description': '另一個不錯的商品', 'price': 300},
        {'id': 3, 'image': 'https://images.unsplash.com/photo-1473093226795-af9932fe5856', 'name': '商品一', 'description': 'Lorem ipsum dolor sit, amet consectetur adipisicing elit. Tempora quam quia facilis dolor aliquid veritatis.', 'price': 2000},
        {'id': 4, 'image': 'https://images.unsplash.com/photo-1453831362806-3d5577f014a4', 'name': '商品二', 'description': '另一個不錯的商品', 'price': 200},
        {'id': 5, 'image': 'https://images.unsplash.com/photo-1473093226795-af9932fe5856', 'name': '商品一', 'description': 'Lorem ipsum dolor sit, amet consectetur adipisicing elit. Tempora quam quia facilis dolor aliquid veritatis.', 'price': 50}
    ],
    '/cat2': [
        {'id': 1, 'image': 'https://images.unsplash.com/photo-1453831362806-3d5577f014a4', 'name': '商品一', 'description': '一個不錯的商品', 'price': 500},
        {'id': 2, 'image': 'https://images.unsplash.com/photo-1473093226795-af9932fe5856', 'name': '商品二', 'description': '另一個不錯的商品', 'price': 6000}
    ]
}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/product', methods=['GET'])
def product():
    cat = request.args.get('url')
    return jsonify(data=products[cat])


if __name__ == '__main__':
    app.run(host='0.0.0.0', use_reloader=True, use_debugger=True, extra_files=extra_files)
