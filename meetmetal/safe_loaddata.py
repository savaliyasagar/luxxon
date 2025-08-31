import json
from home.models import CatalogPage

with open('data.json', encoding='utf-8') as f:
    data = json.load(f)

for obj in data:
    if obj['model'] == 'home.catalogpage':
        fields = obj['fields']
        page_number = fields.get('page_number')

        print(f"Handling CatalogPage page_number={page_number}...")

        CatalogPage.objects.update_or_create(
    page_number=page_number,
    defaults={
        "front_image": fields.get("front_image", "default.jpg"),
        "back_image": fields.get("back_image", "default.jpg"),
    }
)

