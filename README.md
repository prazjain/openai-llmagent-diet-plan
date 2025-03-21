
#### Steps for Developers to run this app
* Create virtual environment `python3 -m venv venv`  
* Activate the env `source venv/bin/activate`  
* Install dependencies `pip install -r requirements.txt`  


#### Sample output generated from this app 

```
python main.py  
OPENAI_API_KEY is not set, skipping trace export  
Nutritionist output:  diet_plan="### Breakfast:\n- **Avocado Smoothie**: \n  - 1 avocado\n  - 1 cup unsweetened almond milk\n  - 1 tablespoon chia seeds\n  - 1 tablespoon almond butter\n  - Stevia to taste (optional)\n  - Blend until smooth.\n  \n### Mid-Morning Snack:\n- **Nuts and Seeds Mix**:\n  - 20 g of mixed almonds, walnuts, and sunflower seeds.\n  \n### Lunch:\n- **Zucchini Noodles with Pesto**:\n  - 2 zucchinis (spiralized into noodles)\n  - 2 tablespoons homemade basil pesto (made with basil, pine nuts, nutritional yeast, olive oil)\n  - Grated Parmesan cheese or nutritional yeast (for added flavor, use sparingly)\n  - Toss noodles with pesto and top with cheese.\n\n### Afternoon Snack:\n- **Olive Tapenade with Cucumber Slices**:\n  - 10-15 green and black olives\n  - 1 tablespoon olive oil\n  - 1 tablespoon capers\n  - Blend into a tapenade\n  - Serve with sliced cucumber.\n\n### Dinner:\n- **Stuffed Bell Peppers**:\n  - 2 medium bell peppers, halved and deseeded\n  - 1 cup diced mushrooms\n  - 1/2 cup spinach, chopped\n  - 1/4 cup pine nuts\n  - 1/4 cup crumbled feta cheese\n  - Sauté mushrooms and spinach, mix in pine nuts and feta\n  - Fill pepper halves with mixture and bake for 20 minutes at 190°C (375°F).\n\n### Evening Snack/ Dessert:\n- **Coconut Fat Bombs**:\n  - 2 tablespoons coconut oil\n  - 2 tablespoons unsweetened cocoa powder\n  - Stevia or monk fruit sweetener to taste\n  - Mix and form into small balls\n  - Refrigerate until solid.\n\n---\n\n**Notes:**\n- Drink plenty of water throughout the day.\n- Monitor your body's response and adjust portion sizes as needed for sustainability.\n- Ensure to maintain proper hydration and consider supplementing with electrolytes."  
Diet plan generated, sending to validator...  
OPENAI_API_KEY is not set, skipping trace export  
Diet Validator output:  feedback="This vegetarian keto meal plan aligns with keto principles by prioritizing high fats, moderate proteins, and low carbohydrates. It includes a variety of nutrient-dense foods and maintains a good balance of macro nutrients necessary for ketosis while respecting dietary preferences.* However, as with any diet, it's advised to consult with a healthcare provider or a registered dietitian to ensure all nutritional needs are met and that it suits your individual health conditions and lifestyle." plan_approved=True  
Diet plan approved!  
```