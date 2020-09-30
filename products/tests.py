from mixer.backend.django import mixer
from rest_framework.reverse import reverse

from tech_shop.tests import BaseAPITest
from products.models import Product


class TestCashierProductViewSet(BaseAPITest):

    def setUp(self):
        self.user = self.create_and_login()
        self.user.is_cashier = True
        self.user.save()

        self.product = mixer.blend(Product, user=self.user)
        self.data = {
            'name': 'Product 1',
            'description': 'Product description',
            'status': 'NEW',
            'price': 100,
            'is_billed': False,

        }

    def test_list_product(self):
        resp = self.client.get(reverse('v1:products:products-list'))

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.data['results']), 1)
        self.assertEqual(resp.data['results'][0]['id'], self.product.id)
        self.assertEqual(resp.data['results'][0]['name'], self.product.name)
        self.assertEqual(resp.data['results'][0]['description'], self.product.description)
        self.assertEqual(resp.data['results'][0]['status'], self.product.status)

    def test_list_product_of_other_user_status(self):
        self.user.is_cashier = False
        self.user.is_seller = True
        self.user.save()
        resp = self.client.get(reverse('v1:products:products-list'))
        self.assertEqual(resp.status_code, 403)

    def test_retrieve_product(self):
        resp = self.client.get(reverse('v1:products:products-detail', args=(self.product.id,)))

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data['id'], self.product.id)
        self.assertEqual(resp.data['name'], self.product.name)
        self.assertEqual(resp.data['description'], self.product.description)
        self.assertEqual(resp.data['status'], self.product.status)

    def test_retrieve_product_of_other_user_status(self):
        self.user.is_cashier = False
        self.user.is_seller = True
        self.user.save()
        resp = self.client.get(reverse('v1:products:products-detail', args=(self.product.id,)))
        self.assertEqual(resp.status_code, 403)

    def test_create_product(self):
        resp = self.client.post(reverse('v1:products:products-list'), data=self.data)

        self.assertEqual(resp.status_code, 201)
        product = Product.objects.get(name=self.data['name'], user=self.user)
        self.assertEqual(resp.data['id'], product.id)

        self.assertEqual(product.name, self.data['name'])
        self.assertEqual(product.description, self.data['description'])
        self.assertEqual(product.status, self.data['status'])
        self.assertEqual(product.price, self.data['price'])
        self.assertEqual(product.is_billed, self.data['is_billed'])

    def test_create_product_of_other_user_status(self):
        self.user.is_cashier = False
        self.user.is_seller = True
        self.user.save()
        resp = self.client.post(reverse('v1:products:products-list'), data=self.data)
        self.assertEqual(resp.status_code, 403)

    def test_update_product(self):
        new_data = {
            'name': 'Product 2',
            'description': 'Product description 2',
            'status': 'COMPLETED',
            'price': 200,
            'is_billed': False,

        }
        resp = self.client.put(reverse('v1:products:products-detail', args=(self.product.id,)),
                               data=new_data)
        self.assertEqual(resp.status_code, 200)
        self.assertNotEqual(resp.data['name'], self.data['name'])
        self.assertNotEqual(resp.data['description'], self.data['description'])
        self.assertNotEqual(resp.data['status'], self.data['status'])

        self.product.refresh_from_db()
        self.assertEqual(self.product.name, new_data['name'])
        self.assertEqual(self.product.description, new_data['description'])
        self.assertEqual(self.product.status, new_data['status'])
        self.assertEqual(self.product.price, new_data['price'])
        self.assertEqual(self.product.is_billed, new_data['is_billed'])

    def test_update_product_of_other_user_status(self):
        new_data = {
            'name': 'Product 2',
            'description': 'Product description 2',
            'status': 'COMPLETED',
            'price': 200,
            'is_billed': False,

        }
        self.user.is_cashier = False
        self.user.is_seller = True
        self.user.save()
        resp = self.client.put(reverse('v1:products:products-detail', args=(self.product.id,)),
                               data=new_data)
        self.assertEqual(resp.status_code, 403)

    def test_destroy_product(self):
        resp = self.client.delete(reverse('v1:products:products-detail', args=(self.product.id,)))
        self.assertEqual(resp.status_code, 204)
        self.assertFalse(Product.objects.filter(id=self.product.id).exists())

    def test_destroy_scenario_of_other_user(self):
        self.user.is_cashier = False
        self.user.is_seller = True
        self.user.save()
        resp = self.client.delete(reverse('v1:products:products-detail', args=(self.product.id,)))
        self.assertEqual(resp.status_code, 403)
        self.assertTrue(Product.objects.filter(id=self.product.id).exists())


class TestCashierBillProductViewSet(BaseAPITest):

    def setUp(self):
        self.user = self.create_and_login()
        self.user.is_cashier = True
        self.user.save()

        self.product = mixer.blend(Product, user=self.user)
        self.data = {
            'status': 'New',
            'is_billed': False,
        }

    def test_list_product(self):
        resp = self.client.get(reverse('v1:products:product-bill-list'))

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.data['results']), 1)
        self.assertEqual(resp.data['results'][0]['id'], self.product.id)
        self.assertEqual(resp.data['results'][0]['status'], self.product.status)

    def test_list_product_of_other_user_status(self):
        self.user.is_cashier = False
        self.user.is_seller = True
        self.user.save()
        resp = self.client.get(reverse('v1:products:product-bill-list'))
        self.assertEqual(resp.status_code, 403)

    def test_retrieve_product(self):
        resp = self.client.get(reverse('v1:products:product-bill-detail', args=(self.product.id,)))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data['id'], self.product.id)

    def test_retrieve_product_of_other_user_status(self):
        self.user.is_cashier = False
        self.user.is_seller = True
        self.user.save()
        resp = self.client.get(reverse('v1:products:product-bill-detail', args=(self.product.id,)))
        self.assertEqual(resp.status_code, 403)

    def test_update_product(self):
        new_data = {
            'status': 'PAID',
            'is_billed': True,

        }
        resp = self.client.put(reverse('v1:products:product-bill-detail', args=(self.product.id,)),
                               data=new_data)
        self.assertEqual(resp.status_code, 200)

        self.product.refresh_from_db()
        self.assertEqual(self.product.status, new_data['status'])
        self.assertEqual(self.product.is_billed, new_data['is_billed'])

    def test_update_product_of_other_user_status(self):
        new_data = {
            'status': 'NEW',
            'is_billed': False,

        }
        self.user.is_cashier = False
        self.user.is_seller = True
        self.user.save()
        resp = self.client.put(reverse('v1:products:products-detail', args=(self.product.id,)),
                               data=new_data)
        self.assertEqual(resp.status_code, 403)


class TestSellerProductViewSet(BaseAPITest):

    def setUp(self):
        self.user = self.create_and_login()
        self.user.is_seller = True
        self.user.save()

        self.product = mixer.blend(Product, user=self.user)
        self.data = {
            'status': 'NEW',
        }

    def test_list_product(self):
        resp = self.client.get(reverse('v1:products:product-status-list'))

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.data['results']), 1)
        self.assertEqual(resp.data['results'][0]['id'], self.product.id)
        self.assertEqual(resp.data['results'][0]['status'], self.product.status)

    def test_list_product_of_other_user_status(self):
        self.user.is_seller = False
        self.user.is_cashier = True
        self.user.save()
        resp = self.client.get(reverse('v1:products:product-status-list'))
        self.assertEqual(resp.status_code, 403)

    def test_retrieve_product(self):
        resp = self.client.get(reverse('v1:products:product-status-detail', args=(self.product.id,)))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data['id'], self.product.id)

    def test_retrieve_product_of_other_user_status(self):
        self.user.is_seller = False
        self.user.is_cashier = True
        self.user.save()
        resp = self.client.get(reverse('v1:products:product-status-detail', args=(self.product.id,)))
        self.assertEqual(resp.status_code, 403)

    def test_update_product(self):
        new_data = {
            'status': 'COMPLETED',

        }
        resp = self.client.put(reverse('v1:products:product-status-detail', args=(self.product.id,)),
                               data=new_data)
        self.assertEqual(resp.status_code, 200)

        self.product.refresh_from_db()
        self.assertEqual(self.product.status, new_data['status'])

    def test_update_product_of_other_user_status(self):
        new_data = {
            'status': 'COMPLETED',

        }
        self.user.is_seller = False
        self.user.is_cashier = True
        self.user.save()
        resp = self.client.put(reverse('v1:products:product-status-detail', args=(self.product.id,)),
                               data=new_data)
        self.assertEqual(resp.status_code, 403)


class TestAccountantProductViewSet(BaseAPITest):

    def setUp(self):
        self.user = self.create_and_login()
        self.user.is_accountant = True
        self.user.save()

        self.product = mixer.blend(Product, user=self.user)
        self.data = {
            'name': 'Product 1',
            'description': 'Product description',
            'status': 'NEW',
            'price': 100,
            'is_billed': False,

        }

    def test_list_product(self):
        resp = self.client.get(reverse('v1:products:product-account-list'))

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.data['results']), 1)
        self.assertEqual(resp.data['results'][0]['id'], self.product.id)
        self.assertEqual(resp.data['results'][0]['name'], self.product.name)
        self.assertEqual(resp.data['results'][0]['description'], self.product.description)
        self.assertEqual(resp.data['results'][0]['status'], self.product.status)
        self.assertEqual(resp.data['results'][0]['is_billed'], self.product.is_billed)

    def test_list_product_of_other_user_status(self):
        self.user.is_accountant = False
        self.user.is_seller = True
        self.user.save()
        resp = self.client.get(reverse('v1:products:product-account-list'))
        self.assertEqual(resp.status_code, 403)

