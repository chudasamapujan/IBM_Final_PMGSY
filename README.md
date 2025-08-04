# 🏗️ Infrastructure Prediction Dashboard - PMGSY

A web-based dashboard for predicting infrastructure project metrics using IBM Watson AutoAI and time series forecasting, specifically designed for PMGSY (Pradhan Mantri Gram Sadak Yojana) infrastructure analysis.

## 🔗 GitHub Repository
**Live Repository**: [https://github.com/chudasamapujan/IBM_Final_PMGSY](https://github.com/chudasamapujan/IBM_Final_PMGSY)

## 📋 Project Overview

This project transforms an IBM Watson AutoAI Jupyter notebook into an interactive web dashboard that predicts infrastructure project outcomes for rural road connectivity under the PMGSY scheme. The dashboard forecasts road works, bridge construction, and project completion rates using advanced time series analysis.

## 🎯 Key Features

- **🔮 Predictive Analytics**: Time series forecasting for infrastructure project completion
- **📊 Interactive Dashboard**: Real-time visualizations with Bootstrap 5 and Plotly.js
- **🤖 AutoAI Integration**: IBM Watson AutoAI model connectivity
- **📱 Responsive Design**: Works seamlessly on desktop and mobile devices
- **📈 Data Visualization**: Interactive charts showing historical trends and future predictions
- **⚡ Quick Setup**: Simple installation with minimal dependencies

## 🚀 Quick Start Guide

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Modern web browser

### Installation Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/chudasamapujan/IBM_Final_PMGSY.git
   cd IBM_Final_PMGSY
   ```

2. **Install dependencies:**
   ```bash
   pip install -r dashboard/requirements.txt
   ```

3. **Start the dashboard:**
   ```bash
   cd dashboard
   python app_simple.py
   ```

4. **Access the dashboard:**
   Open your browser and navigate to: `http://localhost:5000`

## 🎮 Dashboard Applications

### 🌟 `app_simple.py` (Recommended for Quick Start)
- **Purpose**: Demonstration and testing
- **Dependencies**: Minimal Flask requirements
- **Features**: Mock predictions with sample PMGSY data
- **Best for**: Quick demos, development, and learning

### 🚀 `app.py` (Production Version)
- **Purpose**: Full production deployment
- **Dependencies**: Complete IBM Watson AutoAI stack
- **Features**: Real AutoAI model integration and live predictions
- **Best for**: Production environments with trained models

## 📁 Project Structure

```
IBM_Final_PMGSY/
├── 📊 dashboard/              # Main web application
│   ├── app.py                # Production version with AutoAI
│   ├── app_simple.py         # Quick start demonstration version
│   ├── model_integration.py  # AutoAI model wrapper
│   ├── templates/            # HTML templates (Bootstrap 5)
│   │   └── index.html        # Main dashboard interface
│   ├── static/               # CSS, JavaScript, images
│   ├── requirements.txt      # Python dependencies
│   └── README.md            # Dashboard-specific documentation
├── 📓 notebooks/             # AutoAI experiment files
│   └── AutoAI_Experiment.ipynb  # Original IBM Watson AutoAI notebook
├── 📈 data/                  # Data management
│   ├── sample/               # Sample PMGSY datasets
│   ├── raw/                  # Original data files
│   └── processed/            # Cleaned datasets
├── 🤖 models/                # Trained model storage
├── 📄 Final_Project.pdf      # Complete project documentation
├── 📄 README.md             # This file
├── 📄 LICENSE               # MIT License
└── 📄 .gitignore            # Git exclusion rules
```

## 🔧 Technical Architecture

- **Backend Framework**: Python Flask web server
- **Frontend Technology**: Bootstrap 5, Plotly.js for interactive visualizations
- **Machine Learning**: IBM Watson AutoAI for time series forecasting
- **Data Processing**: Pandas and NumPy for data manipulation
- **Deployment**: Compatible with local, Docker, and cloud environments

## 📊 PMGSY Prediction Variables

The dashboard forecasts these critical PMGSY infrastructure metrics:

| Variable | Description | Impact |
|----------|-------------|--------|
| **Road Works Sanctioned** | Number of approved road construction projects | Planning & Budget Allocation |
| **Bridges Sanctioned** | Number of approved bridge construction projects | Connectivity Improvement |
| **Road Works Completed** | Number of completed road projects | Progress Tracking |
| **Bridges Completed** | Number of completed bridge projects | Milestone Achievement |
| **Bridges Balance** | Number of bridge projects currently in progress | Resource Management |

## 🎯 Usage Instructions

### Step-by-Step Guide:

1. **🌐 Open Dashboard**: Start with `app_simple.py` for immediate results
2. **📝 Input Parameters**: Enter current infrastructure project numbers
3. **🔮 Generate Predictions**: Click "Generate Predictions" to see 6-month forecasts
4. **📊 Analyze Results**: Review interactive charts showing trends and predictions
5. **📈 Explore Data**: Examine historical data patterns and model insights

### Dashboard Features:
- **Real-time Input Validation**: Ensures data quality
- **Interactive Charts**: Zoom, pan, and explore predictions
- **Export Functionality**: Download results and charts
- **Mobile Responsive**: Full functionality on all devices

## 🌐 Browser Compatibility

| Browser | Status | Version |
|---------|--------|---------|
| Chrome | ✅ Recommended | Latest |
| Firefox | ✅ Supported | Latest |
| Safari | ✅ Supported | Latest |
| Edge | ✅ Supported | Latest |

## 🛠️ Troubleshooting Guide

### Common Issues & Solutions:

**❌ "Module not found" errors:**
```bash
pip install --upgrade pip
pip install flask plotly pandas numpy
```

**❌ Port already in use:**
```python
# Change port in app.py or app_simple.py
app.run(host='0.0.0.0', port=5001, debug=True)
```

**❌ Charts not loading:**
- Verify internet connection for Plotly.js CDN
- Clear browser cache and refresh
- Check browser console for JavaScript errors

**❌ AutoAI model not loading:**
- Ensure IBM Watson credentials are configured
- Verify model files exist in `models/` directory
- Use `app_simple.py` for testing without AutoAI dependencies

## 📊 Development & Contribution

### Local Development Setup:
```bash
# Clone repository
git clone https://github.com/chudasamapujan/IBM_Final_PMGSY.git

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r dashboard/requirements.txt

# Run development server
cd dashboard
python app_simple.py
```

### Contributing Guidelines:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 Documentation & Resources

- **📖 Project Documentation**: See `Final_Project.pdf`
- **🔗 GitHub Repository**: [IBM_Final_PMGSY](https://github.com/chudasamapujan/IBM_Final_PMGSY)
- **📊 AutoAI Notebook**: Located in `notebooks/AutoAI_Experiment.ipynb`
- **🎯 Dashboard Guide**: See `dashboard/README.md`

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Pujan Chudasama**
- 🔗 GitHub: [@chudasamapujan](https://github.com/chudasamapujan)
- 📧 Repository: [IBM_Final_PMGSY](https://github.com/chudasamapujan/IBM_Final_PMGSY)

## 🎉 Getting Started

Ready to explore PMGSY infrastructure predictions? 

**Quick Start Command:**
```bash
git clone https://github.com/chudasamapujan/IBM_Final_PMGSY.git
cd IBM_Final_PMGSY/dashboard
pip install -r requirements.txt
python app_simple.py
```

Then open `http://localhost:5000` in your browser! 🚀

---

⭐ **Star this repository** if you find it useful for infrastructure analysis and prediction!
