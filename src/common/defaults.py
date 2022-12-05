from user.choices import CategoryTitle, RoleTitle
from user.models import CategoryModel


def create_category(apps, schema_editor):                              
    category = apps.get_model('user', 'CategoryModel')
    obj = category(title=CategoryTitle.managers.value)
    obj.save()

def create_role(apps, schema_editor):
    from user.registry.models import CategoryModel
    category =  CategoryModel.objects.first()
    role = apps.get_model('user', 'RoleModels')
    obj = role(title=RoleTitle.importer.value, category=category)
    obj.save()
    

# def create_user(apps, schema_editor):
#     ManageTablePrices = apps.get_model('management', 'ManageTablePrices')
#     obj = ManageTablePrices()
#     obj.save()
