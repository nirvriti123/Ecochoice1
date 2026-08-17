from flask import Flask, render_template, request, redirect, jsonify, session

import product_display as p

app = Flask(__name__)
app.secret_key='secret_key#!.4357810'

@app.route('/')
def home():
    print('home')
    return render_template('index.html')

product_selection=[]
@app.route('/selected-product', methods=['POST'])
def get_selected_text():
    print("received post")
    product=request.get_json().get('product_name')
    category=request.get_json().get('category_name')
    session['product']=product
    session['category']=category
    return jsonify({"status": "success", "redirect_url": "/results-page"})


@app.route('/results-page')
def display_products():
    product_category=session.get('product')
    category=session.get('category')
    product_data={}
    product_data[product_category]=p.products(category,product_category)
    print(product_data)

    return render_template('products.html', categories=product_data)




if __name__ == '__main__':
    app.run(port=5001, debug=False)
