from flask import Flask, jsonify, request, render_template


app = Flask(__name__)


products = {
    '/cat1': [
        {'id': 1, 'image': 'https://images.unsplash.com/photo-1453831362806-3d5577f014a4', 'name': '商品一', 'description': '一個不錯的商品'},
        {'id': 2, 'image': 'https://images.unsplash.com/photo-1473093226795-af9932fe5856', 'name': '商品二', 'description': '另一個不錯的商品'},
        {'id': 3, 'image': '', 'name': '商品一', 'description': 'Lorem ipsum dolor sit, amet consectetur adipisicing elit. Tempora quam quia facilis dolor aliquid veritatis.'},
        {'id': 4, 'image': 'https://images.unsplash.com/photo-1453831362806-3d5577f014a4', 'name': '商品二', 'description': '另一個不錯的商品'},
        {'id': 5, 'image': 'https://images.unsplash.com/photo-1473093226795-af9932fe5856', 'name': '商品一', 'description': 'Lorem ipsum dolor sit, amet consectetur adipisicing elit. Tempora quam quia facilis dolor aliquid veritatis.'}
    ],
    '/cat2': [
        {'id': 1, 'image': 'https://images.unsplash.com/photo-1453831362806-3d5577f014a4', 'name': '商品一', 'description': '一個不錯的商品'},
        {'id': 2, 'image': 'https://images.unsplash.com/photo-1473093226795-af9932fe5856', 'name': '商品二', 'description': '另一個不錯的商品'}
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
    app.run(host='0.0.0.0')
