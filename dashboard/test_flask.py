"""
Ultra-minimal Flask test to verify the setup works
"""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Infrastructure Dashboard - Test</title>
        <style>
            body { font-family: Arial, sans-serif; padding: 40px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; }
            .container { max-width: 600px; margin: 0 auto; text-align: center; }
            .success { background: rgba(255,255,255,0.1); padding: 20px; border-radius: 10px; margin: 20px 0; }
            .next-steps { background: rgba(255,255,255,0.05); padding: 15px; border-radius: 8px; text-align: left; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 Infrastructure Prediction Dashboard</h1>
            <div class="success">
                <h2>✅ Setup Successful!</h2>
                <p>Flask is working properly on your system.</p>
            </div>
            
            <div class="next-steps">
                <h3>📋 Next Steps:</h3>
                <ol>
                    <li><strong>Stop this test:</strong> Press Ctrl+C in terminal</li>
                    <li><strong>Run the full dashboard:</strong> <code>python app_simple.py</code></li>
                    <li><strong>Or use the startup script:</strong> <code>start_simple.bat</code></li>
                </ol>
            </div>
            
            <div class="next-steps">
                <h3>🔧 Available Files:</h3>
                <ul>
                    <li><strong>test_flask.py</strong> - This basic test (currently running)</li>
                    <li><strong>app_simple.py</strong> - Full dashboard with mock data</li>
                    <li><strong>app.py</strong> - Advanced version for model integration</li>
                </ul>
            </div>
            
            <p style="margin-top: 30px;">
                <em>🎯 The simplified dashboard works with just Flask - no complex dependencies needed!</em>
            </p>
        </div>
    </body>
    </html>
    '''

@app.route('/test')
def test():
    return {'status': 'success', 'message': 'Flask API is working!'}

if __name__ == '__main__':
    print("🧪 Flask Test Server Starting...")
    print("📊 Open your browser to: http://localhost:5000")
    print("🔗 API test endpoint: http://localhost:5000/test")
    print("💡 Press Ctrl+C to stop\n")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
