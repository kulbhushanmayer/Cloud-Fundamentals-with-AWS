from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    # HTML code written directly in the Flask app without images
    html_content = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Welcome to Thinknyx Technologies</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                padding: 20px;
                background-color: #f0f0f0;
            }
            h1 {
                color: #4CAF50;
                margin-bottom: 20px;
            }
            p {
                color: #333;
                font-size: 18px;
            }
            .services {
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                gap: 20px;
                margin-top: 30px;
            }
            .service {
                padding: 20px;
                background-color: white;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            }
            .service h3 {
                color: #4CAF50;
            }
            footer {
                margin-top: 50px;
                font-size: 14px;
                color: #777;
            }
        </style>
    </head>
    <body>

        <h1>Welcome to Thinknyx Technologies!</h1>
        <p>We specialize in providing innovative solutions to make your business thrive. Explore our services below:</p>

        <div class="services">
            <div class="service">
                <h3>Web Development</h3>
                <p>Building responsive and functional websites to meet your business needs.</p>
            </div>
            <div class="service">
                <h3>Cloud Solutions</h3>
                <p>Harnessing the power of cloud computing to drive scalability and efficiency.</p>
            </div>
            <div class="service">
                <h3>Mobile Apps</h3>
                <p>Creating user-friendly mobile apps for Android and iOS platforms.</p>
            </div>
        </div>

        <footer>
            <p>From Thinknyx Technologies</p>
        </footer>

    </body>
    </html>
    '''
    # Render the HTML content
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
