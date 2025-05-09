from django.core.management.base import BaseCommand
from customer.models import Customer, Medicine
from customer.models import SuggestedMedicine
from collections import defaultdict
from sklearn.neighbors import NearestNeighbors
import numpy as np

class Command(BaseCommand):
    help = 'Generate top 3 medicine suggestions for each customer'

    def handle(self, *args, **kwargs):
        customers = Customer.objects.all()
        medicines = list(Medicine.objects.all())

        med_index = {med.id: i for i, med in enumerate(medicines)}
        customer_vectors = []
        customer_ids = []

        for customer in customers:
            vector = [0] * len(medicines)
            sales = customer.sale_set.prefetch_related('items')
            for sale in sales:
                for item in sale.items.all():
                    idx = med_index.get(item.medicine_id)
                    if idx is not None:
                        vector[idx] += item.quantity
            customer_vectors.append(vector)
            customer_ids.append(customer.id)

        if not customer_vectors:
            return

        model = NearestNeighbors(n_neighbors=3, metric='cosine')
        model.fit(np.array(customer_vectors))

        SuggestedMedicine.objects.all().delete()

        for idx, customer_id in enumerate(customer_ids):
            distances, indices = model.kneighbors([customer_vectors[idx]])
            score_dict = defaultdict(float)

            for neighbor_idx in indices[0]:
                if neighbor_idx == idx:
                    continue
                neighbor_vector = customer_vectors[neighbor_idx]
                for i, qty in enumerate(neighbor_vector):
                    score_dict[i] += qty

            top_items = sorted(score_dict.items(), key=lambda x: x[1], reverse=True)[:3]
            for i, score in top_items:
                SuggestedMedicine.objects.create(
                    customer_id=customer_id,
                    medicine=medicines[i],
                    score=score
                )

        self.stdout.write(self.style.SUCCESS('Suggestions generated successfully.'))
