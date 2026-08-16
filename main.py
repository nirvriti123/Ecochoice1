from flask import Flask, render_template, request, redirect, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    print('home')
    return render_template('index.html')

@app.route('/selected-product', methods=['POST'])
def get_selected_text():
    print("received post")
    product=request.get_json().get('product_name')
    category=request.get_json().get('category_name')
    print(product,category)
    return jsonify({"status": "success", "redirect_url": "/results-page"})


@app.route('/results-page')
def show_results():

    #sql stuff here


    return render_template('products.html')


if __name__ == '__main__':
    app.run(port=5001, debug=False)
