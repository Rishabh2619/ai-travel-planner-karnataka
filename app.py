from flask import Flask, render_template, request
import json

app = Flask(__name__)

# Enhanced data for Karnataka regions with attractions tagged by interest
KARNATAKA_DATA = {
    "Mysuru": {
        "attractions": {
            "Morning": [
                {"name": "Mysore Palace", "interests": ["Heritage & History", "Food & Culture"]},
                {"name": "Chamundi Hills", "interests": ["Nature & Wildlife", "Adventure Sports"]},
                {"name": "Mysore Zoo", "interests": ["Nature & Wildlife", "Food & Culture"]},
                {"name": "St. Philomena's Cathedral", "interests": ["Heritage & History"]},
                {"name": "Railway Museum", "interests": ["Heritage & History", "Food & Culture"]}
            ],
            "Afternoon": [
                {"name": "Brindavan Gardens", "interests": ["Nature & Wildlife", "Food & Culture"]},
                {"name": "Kukkarahalli Lake", "interests": ["Nature & Wildlife"]},
                {"name": "Devaraja Market", "interests": ["Food & Culture", "Heritage & History"]},
                {"name": "Mysore Sand Sculpture Museum", "interests": ["Heritage & History"]},
                {"name": "Jaganmohan Palace", "interests": ["Heritage & History"]}
            ],
            "Evening": [
                {"name": "Mysore Palace (Light & Sound Show)", "interests": ["Heritage & History", "Food & Culture"]},
                {"name": "Karanji Lake", "interests": ["Nature & Wildlife"]},
                {"name": "Chamundi Hills Sunset View", "interests": ["Nature & Wildlife", "Adventure Sports"]},
                {"name": "Mysore Zoo (Evening Safari)", "interests": ["Nature & Wildlife"]},
                {"name": "Lalitha Mahal Palace", "interests": ["Heritage & History"]}
            ]
        },
        "food": ["Mysore Masala Dosa", "Mysore Pak", "Ragi Mudde", "Bisi Bele Bath", "Mysore Bonda"],
        "tips": {
            "kn": "ಮೈಸೂರು ಪಾಲ-Éನ ನೂತನ ಬೆಳಕು ಮಂಡಲದಲ್ಲಿ ನющи ಅಲಕರ್ನ تصویğanjan",
            "en": "Visit Mysore Palace early morning to avoid crowds and enjoy the best light for photos."
        }
    },
    "Coorg": {
        "attractions": {
            "Morning": [
                {"name": "Abbey Falls", "interests": ["Nature & Wildlife", "Adventure Sports"]},
                {"name": "Raja's Seat", "interests": ["Nature & Wildlife", "Food & Culture"]},
                {"name": "Madikeri Fort", "interests": ["Heritage & History"]},
                {"name": "Omkareshwara Temple", "interests": ["Heritage & History"]},
                {"name": "Coffee Plantation Tour", "interests": ["Food & Culture", "Nature & Wildlife"]}
            ],
            "Afternoon": [
                {"name": "Dubare Elephant Camp", "interests": ["Nature & Wildlife", "Adventure Sports", "Food & Culture"]},
                {"name": "Golden Temple (Namdroling Monastery)", "interests": ["Heritage & History", "Food & Culture"]},
                {"name": "Talakaveri", "interests": ["Nature & Wildlife", "Adventure Sports"]},
                {"name": "Nagarhole National Park", "interests": ["Nature & Wildlife", "Adventure Sports"]},
                {"name": "Iruppu Falls", "interests": ["Nature & Wildlife", "Adventure Sports"]}
            ],
            "Evening": [
                {"name": "Mandalpatti Viewpoint", "interests": ["Nature & Wildlife", "Adventure Sports"]},
                {"name": "Tadiandamol Peak Trek", "interests": ["Adventure Sports", "Nature & Wildlife"]},
                {"name": "Dinner at a Coorgi Homestay", "interests": ["Food & Culture"]},
                {"name": "Campfire at Resort", "interests": ["Food & Culture", "Adventure Sports"]},
                {"name": "Stargazing at Raja's Seat", "interests": ["Nature & Wildlife"]}
            ]
        },
        "food": ["Coorg Pandi Curry", "Kadambuttu", "Bamboo Shoot Curry", "Coorgi Wine", "Kolathu"],
        "tips": {
            "kn": "ಕೊಡಗುಗೆ ಹೋಗುವಾಗ ಮಳೆಕ costume ತಂದು ಹೋಗundosln",
            "en": "Carry raincoat when visiting Coorg as weather can change rapidly."
        }
    },
    "Hampi": {
        "attractions": {
            "Morning": [
                {"name": "Virupaksha Temple", "interests": ["Heritage & History"]},
                {"name": "Vittala Temple", "interests": ["Heritage & History"]},
                {"name": "Hampi Bazaar", "interests": ["Heritage & History", "Food & Culture"]},
                {"name": "Lotus Mahal", "interests": ["Heritage & History"]},
                {"name": "Elephant Stables", "interests": ["Heritage & History"]}
            ],
            "Afternoon": [
                {"name": "Queen's Bath", "interests": ["Heritage & History"]},
                {"name": "Achutaraya Temple", "interests": ["Heritage & History"]},
                {"name": "Royal Enclosure", "interests": ["Heritage & History"]},
                {"name": "Matanga Hill", "interests": ["Nature & Wildlife", "Adventure Sports"]},
                {"name": "Hemakuta Hill Temples", "interests": ["Heritage & History"]}
            ],
            "Evening": [
                {"name": "Matanga Hill Sunset", "interests": ["Nature & Wildlife", "Adventure Sports"]},
                {"name": "Virupaksha Temple Evening Aarti", "interests": ["Heritage & History", "Food & Culture"]},
                {"name": "Sanapur Lake Coracle Ride", "interests": ["Adventure Sports", "Nature & Wildlife"]},
                {"name": "Hippie Island Chillout", "interests": ["Food & Culture", "Nature & Wildlife"]},
                {"name": "Hampi Sunset Point", "interests": ["Nature & Wildlife"]}
            ]
        },
        "food": ["Hampi Thali", "Bisi Bele Bath", "Jolada Rotti", "Badagi", "Kesaribath"],
        "tips": {
            "kn": "ಹಂಪಿಯ ಶಿಲ್ಪಗಳು ನೋಡிச колалаллр",
            "en": "Hire a guide to understand the historical significance of Hampi's ruins."
        }
    },
    "Bengaluru": {
        "attractions": {
            "Morning": [
                {"name": "Lalbagh Botanical Garden", "interests": ["Nature & Wildlife", "Food & Culture"]},
                {"name": "Bangalore Palace", "interests": ["Heritage & History"]},
                {"name": "Tipu Sultan's Summer Palace", "interests": ["Heritage & History"]},
                {"name": "Cubbon Park", "interests": ["Nature & Wildlife", "Food & Culture"]},
                {"name": "Vidhana Soudha", "interests": ["Heritage & History"]}
            ],
            "Afternoon": [
                {"name": "National Gallery of Modern Art", "interests": ["Heritage & History", "Food & Culture"]},
                {"name": "Bangalore Palace Grounds", "interests": ["Heritage & History"]},
                {"name": "Innovative Film City", "interests": ["Adventure Sports", "Food & Culture"]},
                {"name": "Ulsoor Lake", "interests": ["Nature & Wildlife"]},
                {"name": "Bannerghatta Biological Park", "interests": ["Nature & Wildlife", "Adventure Sports"]}
            ],
            "Evening": [
                {"name": "MG Road Brigade Road", "interests": ["Food & Culture", "Adventure Sports"]},
                {"name": "Commercial Street Shopping", "interests": ["Food & Culture"]},
                {"name": "Rooftop Dinner at UB City", "interests": ["Food & Culture"]},
                {"name": "Bangalore Palace Grounds Light Show", "interests": ["Heritage & History"]},
                {"name": "Lalbagh Botanical Garden Evening Walk", "interests": ["Nature & Wildlife"]}
            ]
        },
        "food": ["Bengaluru Biryani", "Ragi Mudde", "Mangalorean Fish Curry", "Kori Rotti", "Benne Dose"],
        "tips": {
            "kn": "ಬೆಂಗಳೂರಿನಲ್ಲಿ ಟ್ರಾಫಿಕದ ಬψε ಜneapolisเช้าวันนี้นี้",
            "en": "Avoid traveling during peak hours (8-10 AM and 6-8 PM) in Bengaluru due to traffic."
        }
    },
    "Udupi": {
        "attractions": {
            "Morning": [
                {"name": "Sri Krishna Temple", "interests": ["Heritage & History", "Food & Culture"]},
                {"name": "Malpe Beach", "interests": ["Nature & Wildlife", "Adventure Sports", "Food & Culture"]},
                {"name": "St. Mary's Island", "interests": ["Nature & Wildlife", "Adventure Sports"]},
                {"name": "Manipal End Point", "interests": ["Nature & Wildlife", "Adventure Sports"]},
                {"name": "Kaup Beach", "interests": ["Nature & Wildlife", "Adventure Sports"]}
            ],
            "Afternoon": [
                {"name": "Krishna Temple Madhyaahna Pooja", "interests": ["Heritage & History", "Food & Culture"]},
                {"name": "Malpe Fishing Harbor", "interests": ["Food & Culture", "Nature & Wildlife"]},
                {"name": "Padubidri Beach", "interests": ["Nature & Wildlife", "Adventure Sports"]},
                {"name": "Katukukke Shiva Temple", "interests": ["Heritage & History"]},
                {"name": "Udupi Saree Weaving Center", "interests": ["Heritage & History", "Food & Culture"]}
            ],
            "Evening": [
                {"name": "Kapu Beach Sunset", "interests": ["Nature & Wildlife", "Adventure Sports"]},
                {"name": "Malpe Beach Sunset", "interests": ["Nature & Wildlife", "Adventure Sports"]},
                {"name": "Dinner at a Udupi Restaurant", "interests": ["Food & Culture"]},
                {"name": "Paryaya Festival (if in season)", "interests": ["Heritage & History", "Food & Culture"]},
                {"name": "Beachside Bonfire", "interests": ["Food & Culture", "Adventure Sports"]}
            ]
        },
        "food": ["Udupi Sambar", "Masala Dosa", "Goli Baje", "Patrode", "Udupi Halu"],
        "tips": {
            "kn": "ಉಡುಪಿ hooten ಬ árbol veg ಕ ನೀಲಿ ದೊ 삐이",
            "en": "Try the authentic Udupi vegetarian cuisine at local temples for a divine experience."
        }
    },
    "Chikmagalur": {
        "attractions": {
            "Morning": [
                {"name": "Mullayanagiri Peak", "interests": ["Nature & Wildlife", "Adventure Sports"]},
                {"name": "Baba Budangiri", "interests": ["Nature & Wildlife", "Adventure Sports"]},
                {"name": "Hebbe Falls", "interests": ["Nature & Wildlife", "Adventure Sports"]},
                {"name": "Coffee Museum", "interests": ["Food & Culture", "Heritage & History"]},
                {"name": "Kalhatti Falls", "interests": ["Nature & Wildlife", "Adventure Sports"]}
            ],
            "Afternoon": [
                {"name": "Hirekolale Lake", "interests": ["Nature & Wildlife"]},
                {"name": "Z Point", "interests": ["Nature & Wildlife", "Adventure Sports"]},
                {"name": "Kudremukh National Park (entry point)", "interests": ["Nature & Wildlife", "Adventure Sports"]},
                {"name": "Coffee Plantation Tour", "interests": ["Food & Culture", "Nature & Wildlife"]},
                {"name": "Yagachi River", "interests": ["Nature & Wildlife", "Adventure Sports"]}
            ],
            "Evening": [
                {"name": "Sunset at Mullayanagiri", "interests": ["Nature & Wildlife", "Adventure Sports"]},
                {"name": "Dinner at a Coffee Estate", "interests": ["Food & Culture"]},
                {"name": "Campfire at Homestay", "interests": ["Food & Culture", "Adventure Sports"]},
                {"name": "Night Trek to Bababudangiri", "interests": ["Adventure Sports", "Nature & Wildlife"]},
                {"name": "Stargazing at Hirekolale Lake", "interests": ["Nature & Wildlife"]}
            ]
        },
        "food": ["Chikkmagalur Coffee Kadubu", "Akki Roti", "Koli Saaru", "Bread Bendi", "Filter Coffee"],
        "tips": {
            "kn": "ಚಿಕ್ಕಮಗಳurus Coffee Estate ದರ್ಶನ ಮಾಡ� 아침에 이크를 방문하세요",
            "en": "Book a plantation stay for an immersive coffee experience from bean to cup."
        }
    },
    "Gokarna": {
        "attractions": {
            "Morning": [
                {"name": "Om Beach", "interests": ["Nature & Wildlife", "Adventure Sports", "Food & Culture"]},
                {"name": "Kudle Beach", "interests": ["Nature & Wildlife", "Adventure Sports"]},
                {"name": "Half Moon Beach", "interests": ["Nature & Wildlife", "Adventure Sports"]},
                {"name": "Paradise Beach", "interests": ["Nature & Wildlife", "Adventure Sports"]},
                {"name": "Mahabaleshwar Temple", "interests": ["Heritage & History"]}
            ],
            "Afternoon": [
                {"name": "Gokarna Beach Trek", "interests": ["Adventure Sports", "Nature & Wildlife"]},
                {"name": "Mirjan Fort", "interests": ["Heritage & History"]},
                {"name": "Yana Caves", "interests": ["Nature & Wildlife", "Adventure Sports"]},
                {"name": "Venkataramana Temple", "interests": ["Heritage & History"]},
                {"name": "Beachside Yoga Session", "interests": ["Nature & Wildlife", "Food & Culture"]}
            ],
            "Evening": [
                {"name": "Sunset at Lighthouse Beach", "interests": ["Nature & Wildlife", "Adventure Sports"]},
                {"name": "Beachside Dinner", "interests": ["Food & Culture"]},
                {"name": "Night Stroll on Gokarna Beach", "interests": ["Nature & Wildlife", "Food & Culture"]},
                {"name": "Bioluminescence Watching (seasonal)", "interests": ["Nature & Wildlife"]},
                {"name": "Campfire on Beach", "interests": ["Food & Culture", "Adventure Sports"]}
            ]
        },
        "food": ["Gokarna Fish Thali", "Kane Fry", "Coconut Rice", "Banana Buns", "Pomfret Fry"],
        "tips": {
            "kn": "ಗೋಕರ್ಣ beaches night camping ನিষೇದ humanas",
            "en": "Beach camping is prohibited after sunset; plan your stay in authorized accommodations."
        }
    },
    "Badami": {
        "attractions": {
            "Morning": [
                {"name": "Badami Cave Temples", "interests": ["Heritage & History"]},
                {"name": "Agastya Lake", "interests": ["Nature & Wildlife", "Food & Culture"]},
                {"name": "Bhutanatha Temple", "interests": ["Heritage & History"]},
                {"name": "Malaprabha River", "interests": ["Nature & Wildlife", "Food & Culture"]},
                {"name": "Badami Fort", "interests": ["Heritage & History"]}
            ],
            "Afternoon": [
                {"name": "Banashankari Temple", "interests": ["Heritage & History"]},
                {"name": "Pattadakal", "interests": ["Heritage & History"]},
                {"name": "Aihole", "interests": ["Heritage & History"]},
                {"name": "Mahakuta Group of Temples", "interests": ["Heritage & History"]},
                {"name": "Archaeological Museum Badami", "interests": ["Heritage & History"]}
            ],
            "Evening": [
                {"name": "Sunset at Badami Cave Temples", "interests": ["Heritage & History", "Nature & Wildlife"]},
                {"name": "Dinner at a Local Restaurant", "interests": ["Food & Culture"]},
                {"name": "Night Visit to Bhutanatha Temple", "interests": ["Heritage & History"]},
                {"name": "Stargazing at Agastya Lake", "interests": ["Nature & Wildlife"]},
                {"name": "Cultural Dance Performance", "interests": ["Food & Culture", "Heritage & History"]}
            ]
        },
        "food": ["Badami Holige", "Jolada Rotti", "Enne Gai", "Shenga Chutney", "Jowar Roti"],
        "tips": {
            "kn": "ಬದಾಮಿ gupta period sculpture ಗೇಲರಿ ಭೇಟಿ answerx",
            "en": "Hire a local guide to explain the intricate Chalukya architecture and symbolism."
        }
    }
}

# Budget tiers (estimated daily expenditure in USD)
BUDGET_TIERS = {
    "Budget Backpacking": 30,
    "Mid-Range Explorer": 70,
    "Luxury Heritage": 150
}

def filter_attractions_by_interests(attractions, selected_interests):
    """
    Filter attractions based on selected interests.
    If no interests selected or no matches, return all attractions.
    """
    if not selected_interests:
        return attractions

    filtered = []
    for attraction in attractions:
        # Check if any of the attraction's interests matches selected interests
        if any(interest in selected_interests for interest in attraction["interests"]):
            filtered.append(attraction)

    # If no matches fall back to all attractions
    return filtered if filtered else attractions

def select_attraction(attractions):
    """
    Select an attraction from a list (used for time slots).
    Uses simple round-robin based on day number to distribute selections.
    In a real app, we might use more sophisticated logic.
    """
    if not attractions:
        return None
    # We'll use a static index for simplicity; in production, we might use day number
    # For now, we'll just return the first one (could be improved with random or based on day)
    return attractions[0]["name"]  # Simple selection; can be enhanced

def generate_itinerary(region, duration, budget_tier, interests, start_point):
    """
    Generate a day-by-day itinerary for the given region and parameters.
    Returns a list of dictionaries, each representing a day.
    """
    if region not in KARNATAKA_DATA:
        # Default to first region if region not found
        region = list(KARNATAKA_DATA.keys())[0]

    data = KARNATAKA_DATA[region]
    daily_budget = BUDGET_TIERS.get(budget_tier, 70)  # Default to mid-range

    itinerary = []

    for day in range(1, duration + 1):
        # For each time slot, filter attractions by interests and select one
        morning_attractions = data["attractions"]["Morning"]
        afternoon_attractions = data["attractions"]["Afternoon"]
        evening_attractions = data["attractions"]["Evening"]

        # Filter by interests
        morning_filtered = filter_attractions_by_interests(morning_attractions, interests)
        afternoon_filtered = filter_attractions_by_interests(afternoon_attractions, interests)
        evening_filtered = filter_attractions_by_interests(evening_attractions, interests)

        # Select attractions (simple selection - can be enhanced with day-based rotation)
        morning_attraction = select_attraction(morning_filtered)
        afternoon_attraction = select_attraction(afternoon_filtered)
        evening_attraction = select_attraction(evening_filtered)

        # Food suggestions (rotate through the list)
        food_suggestion = data["food"][day % len(data["food"])]

        # Tips (we'll use the same tip each day for simplicity, but could vary)
        tip_kn = data["tips"]["kn"]
        tip_en = data["tips"]["en"]

        day_plan = {
            "day": day,
            "morning": {
                "activity": morning_attraction or "Explore local surroundings",
                "food": None,  # Morning food is usually breakfast at hotel
                "tip": None
            },
            "afternoon": {
                "activity": afternoon_attraction or "Visit local market",
                "food": food_suggestion,
                "tip": None
            },
            "evening": {
                "activity": evening_attraction or "Relax at accommodation",
                "food": None,  # Evening food could be dinner or snack
                "tip": {"kn": tip_kn, "en": tip_en}
            },
            "estimated_budget": daily_budget,
            "region": region
        }
        itinerary.append(day_plan)

    return itinerary

@app.route('/')
def index():
    """Render the input form."""
    regions = list(KARNATAKA_DATA.keys())
    budget_tiers = list(BUDGET_TIERS.keys())
    interests = [
        "Heritage & History",
        "Nature & Wildlife",
        "Coastal & Beaches",
        "Food & Culture",
        "Adventure Sports"
    ]
    return render_template('index.html', regions=regions, budget_tiers=budget_tiers, interests=interests)

@app.route('/result', methods=['POST'])
def result():
    """Process form data and generate itinerary."""
    # Get form data
    region = request.form.get('region')
    duration = int(request.form.get('duration'))
    budget_tier = request.form.get('budget_tier')
    interests = request.form.getlist('interests')  # Returns list of selected checkboxes
    start_point = request.form.get('start_point')

    # Generate itinerary
    itinerary = generate_itinerary(region, duration, budget_tier, interests, start_point)

    # Calculate total estimated budget
    daily_budget = BUDGET_TIERS.get(budget_tier, 70)
    total_budget = daily_budget * duration

    # Prepare data for template
    template_data = {
        'region': region,
        'duration': duration,
        'budget_tier': budget_tier,
        'interests': interests,
        'start_point': start_point,
        'itinerary': itinerary,
        'total_budget': total_budget,
        'daily_budget': daily_budget
    }

    return render_template('result.html', **template_data)

if __name__ == '__main__':
    app.run(debug=True)