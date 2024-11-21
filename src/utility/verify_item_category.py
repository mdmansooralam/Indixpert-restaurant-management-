



from src.database.collections.default import Default

def verify_item_category(category_id):
    try:
        category_list = Default().item_category

        if(category_list):
            for category in category_list:
                if category['id'] == int(category_id):
                    return category['name']
    except Exception as error:
        return None