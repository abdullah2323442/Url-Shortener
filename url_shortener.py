from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dictionary to store mapping between custom short keys and original URLs
custom_url_mapping = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten():
    long_url = request.form.get('long_url')
    custom_key = request.form.get('custom_key')

    if custom_key:
        # Check if the custom key is already in use
        if custom_key in custom_url_mapping:
            return render_template('index.html', error="Custom key is already in use. Please choose another.")

        # Store the mapping between custom short key and original URL
        custom_url_mapping[custom_key] = long_url
        short_url = request.host_url + custom_key
    else:
        # Generate a unique short key (you may use a library or other method for this)
        short_key = str(hash(long_url))
        
        # Store the mapping between short and original URLs
        custom_url_mapping[short_key] = long_url
        short_url = request.host_url + short_key

    return render_template('result.html', short_url=short_url)

@app.route('/<custom_key>')
def redirect_to_custom(custom_key):
    # Retrieve the original URL from the mapping
    original_url = custom_url_mapping.get(custom_key)
    
    if original_url:
        # Redirect to the original URL
        return redirect(original_url)
    else:
        # Handle the case when the custom key is not found
        return render_template('not_found.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
