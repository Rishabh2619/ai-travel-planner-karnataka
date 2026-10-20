# Karnataka AI Travel Planner

**Problem Statement #6: AI Travel Planner for Karnataka**  
*Kannada Digital Innovation Hackathon 2026*

## Overview
An intelligent, full-stack web application that generates personalized day-by-day itineraries for travelers visiting Karnataka, India. The app combines user preferences (region, duration, budget, interests) with localized knowledge to create culturally rich travel plans featuring authentic food recommendations, insider tips in Kannada with English translations, and budget estimates.

## Architecture Overview
```
Frontend (HTML/CSS/Tailwind) 
        ↓
Flask Backend (Python)
        ↓
Trip Generation Engine (Modular Algorithm)
        ↓
Personalized Itinerary Results
```

### Key Components:
1. **Input Dashboard** (`index.html`): Clean, responsive form for user inputs
2. **Backend Logic** (`app.py`): 
   - Flask routes for handling requests
   - Modular trip generation engine with Karnataka-specific data
   - Dynamic day-by-day itinerary structuring (Morning/Afternoon/Evening)
3. **Results View** (`result.html`): 
   - Glassmorphic UI cards for modern aesthetics
   - Timeline-based itinerary visualization
   - Budget breakdown and packing essentials
   - Interactive elements (Print/PDF, Regenerate Day, Kannada phrase-of-the-day)
4. **Styling** (`static/style.css`): Custom utilities for glassmorphism, animations, and responsive design

## Tech Stack
- **Backend**: Python 3.x, Flask 3.0.3
- **Frontend**: HTML5, CSS3, Tailwind CSS (via CDN), Custom CSS
- **Production Server**: Gunicorn 22.0.0
- **Design Principles**: Glassmorphism, smooth transitions, mobile-first responsive layout

## Features
- ✅ Multi-region Karnataka coverage (Mysuru, Coorg, Hampi, Bengaluru, Udupi, Chikmagalur, Gokarna, Badami)
- ✅ Duration flexibility (1-7 days)
- ✅ Budget tiers (Backpacking, Mid-Range, Luxury)
- ✅ Interest-based filtering (Heritage, Nature, Coastal, Food, Adventure)
- ✅ Authentic local food recommendations per region
- ✅ Insider travel tips in Kannada with English translations
- ✅ Daily budget estimation
- ✅ Beautiful glassmorphic UI with smooth animations
- ✅ Print/Save as PDF functionality
- ✅ Mobile-responsive design

## Local Setup & Deployment

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation
```bash
# Clone the repository (if applicable)
git clone <repository-url>
cd kannada_travel_planner

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Running Locally
```bash
# Set environment variables (optional)
export FLASK_APP=app.py
export FLASK_ENV=development

# Start the Flask development server
flask run
# Or alternatively:
python app.py
```

Visit `http://localhost:5000` in your browser.

### Production Deployment
```bash
# Using Gunicorn (recommended for production)
gunicorn --bind 0.0.0.0:8000 app:app
```

### Docker Deployment (Optional)
```dockerfile
# Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]
```

Build and run:
```bash
docker build -t karnataka-travel-planner .
docker run -p 8000:8000 karnataka-travel-planner
```

## Hackathon Submission Notes
- **Zero Placeholders**: All data fields are populated with realistic, region-specific information
- **Production Ready**: Includes proper error handling, responsive design, and scalable architecture
- **Cultural Authenticity**: Kannada phrases and local insights sourced from cultural knowledge
- **Innovation**: AI-driven itinerary generation with modular algorithm for easy extension
- **Accessibility**: Semantic HTML, ARIA labels (via Tailwind), and high-contrast UI elements

## Future Enhancements
1. Integration with real-time weather and event APIs
2. Multi-regional trip planning (cross-district itineraries)
3. User authentication and saved trips
4. Machine learning for preference prediction
5. Offline functionality with PWA capabilities
6. Local business integration for bookings

## Credits
Developed for the Kannada Digital Innovation Hackathon 2026 by [Your Name/Team]  
Problem Statement #6: AI Travel Planner for Karnataka

> "Traveling – it leaves you speechless, then turns you into a storyteller." – Ibn Battuta