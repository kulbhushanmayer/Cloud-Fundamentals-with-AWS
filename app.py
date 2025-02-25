from flask import Flask, render_template_string, request, redirect, url_for
import datetime
import uuid
import socket
import os

app = Flask(__name__)

# Ensure the 'data' folder exists to store uploaded files
os.makedirs('data', exist_ok=True)

@app.route('/')
def home():
    # Get the current date
    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Get the unique system identifier (UUID)
    system_id = str(uuid.uuid4())  # Generates a random unique system identifier

    # Get the private IP address
    private_ip = socket.gethostbyname(socket.gethostname())  # Get the local IP address

    # HTML content for the home page
    html_content = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Welcome to Thinknyx Technologies</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                text-align: center;
                padding: 20px;
                background-color: #f0f0f0;
            }}
            h1 {{
                color: #4CAF50;
                margin-bottom: 20px;
            }}
            p {{
                color: #333;
                font-size: 18px;
            }}
            .services {{
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                gap: 20px;
                margin-top: 30px;
            }}
            .service {{
                padding: 20px;
                background-color: white;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            }}
            .service h3 {{
                color: #4CAF50;
            }}
            footer {{
                margin-top: 50px;
                font-size: 14px;
                color: #777;
            }}
            .system-info {{
                position: fixed;
                bottom: 20px;
                right: 20px;
                font-size: 14px;
                color: #333;
                background-color: #fff;
                padding: 10px;
                border-radius: 8px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            }}
            .nav-link {{
                position: absolute;
                top: 20px;
                left: 20px;
                font-size: 16px;
                color: #4CAF50;
            }}
        </style>
    </head>
    <body>

        <!-- Careers Link -->
        <a href="{{ url_for('careers') }}" class="nav-link">Careers</a>

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

        <!-- Display current date, unique system ID, and private IP -->
        <div class="system-info">
            <p><strong>Current Date:</strong> {current_date}</p>
            <p><strong>System ID:</strong> {system_id}</p>
            <p><strong>Private IP:</strong> {private_ip}</p>
        </div>

    </body>
    </html>
    '''
    # Render the HTML content
    return render_template_string(html_content)

@app.route('/careers', methods=['GET', 'POST'])
def careers():
    if request.method == 'POST':
        # Handle file upload
        if 'file' not in request.files:
            return "No file part", 400
        
        file = request.files['file']
        
        if file.filename == '':
            return "No selected file", 400
        
        # Save the file in the 'data' folder
        file_path = os.path.join('data', file.filename)
        file.save(file_path)
        return f"File '{file.filename}' uploaded successfully to {file_path}"

    # HTML content for the careers page
    html_content = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Careers - Thinknyx Technologies</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                text-align: center;
                padding: 20px;
                background-color: #f0f0f0;
            }}
            h1 {{
                color: #4CAF50;
            }}
            .upload-form {{
                margin-top: 30px;
                background-color: #fff;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                display: inline-block;
            }}
            .upload-form input {{
                margin-top: 10px;
            }}
            footer {{
                margin-top: 50px;
                font-size: 14px;
                color: #777;
            }}
        </style>
    </head>
    <body>

        <h1>Careers at Thinknyx Technologies</h1>
        <p>We are always looking for talented individuals to join our team! Upload your resume below:</p>

        <!-- File Upload Form -->
        <form method="POST" enctype="multipart/form-data" class="upload-form">
            <label for="file">Choose a file to upload:</label><br><br>
            <input type="file" name="file" id="file" required><br><br>
            <button type="submit">Upload</button>
        </form>

        <footer>
            <p>From Thinknyx Technologies</p>
        </footer>

    </body>
    </html>
    '''
    # Render the HTML content for the careers page
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
