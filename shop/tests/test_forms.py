from django.test import TestCase
from shop.forms import CategoryCreateForm

class CategoryCreateFormTestCase(TestCase):
    def test_field_label(self):
        form = CategoryCreateForm()
        self.assertTrue(form.fields['name'].label == None or form.files['name'].label== 'Категория')


    def test_form_value(self):
        form_data = {'name': 'phones'}
        form = CategoryCreateForm(data=form_data)
        CategoryCreateForm(data=form_data)
        self.assertTrue((form.is_valid()))

    def test_form_not_value(self):
        form_data = {'name': ''}
        form = CategoryCreateForm(data=form_data)
        CategoryCreateForm(data=form_data)
        self.assertTrue(form.is_valid())