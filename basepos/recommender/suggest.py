import os
import django
import pandas as pd
from sklearn.neighbors import NearestNeighbors
import sys

# Add project base to Python path
#sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set correct settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "basepos.settings")

# Setup Django
django.setup()

# Now you can import your models
from customer.models import SaleItem


# Step 1: Load purchase data
data = SaleItem.objects.select_related('sale__customer', 'medicine').values(
    'sale__customer__id',
    'sale__customer__name',
    'medicine__name',
    'quantity'
)
df = pd.DataFrame(data)

if df.empty:
    print("No sales data found.")
    exit()

# Step 2: Pivot for customer-medicine matrix
pivot = df.pivot_table(
    index='sale__customer__name',
    columns='medicine__name',
    values='quantity',
    aggfunc='sum',
    fill_value=0
)

# Step 3: Train ML model
model = NearestNeighbors(metric='cosine', algorithm='brute')
model.fit(pivot)

# Step 4: Suggest medicines for each customer
print("\nSuggestions:")
for customer in pivot.index:
    customer_index = pivot.index.get_loc(customer)
    distances, indices = model.kneighbors([pivot.iloc[customer_index]], n_neighbors=3)
    neighbors = pivot.iloc[indices[0][1:]]  # Skip self
    suggested = neighbors.mean().sort_values(ascending=False).head(3)
    print(f"\n🧑‍⚕️ {customer}'s suggested medicines:")
    for med, score in suggested.items():
        print(f"  • {med} (score: {score:.2f})")
