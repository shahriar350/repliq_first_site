import random
from django.core.management import BaseCommand
from django.db import transaction
from faker import Faker

from admin_app.models import District, Category, Manufacturer, Supplier, MedicinePhysicalState, RouteOfAdministration, \
    Brand, Ingredient
from auth_app.models import Users, MerchantInformation, UserAddress
from client_app.models import Tenant
from customer_app.models import Cart, CartProduct, Checkout, CheckoutProduct
from pharmaco_backend.utils import generate_image
from product_app.models import BaseProduct, Product, ProductImage

# Create an instance of Faker
fake = Faker()


class Command(BaseCommand):
    help = 'Create dummy information...'

    def handle(self, *args, **options):
        Users.objects.all().delete()
        Tenant.objects.all().delete()
        BaseProduct.objects.all().delete()
        Product.objects.all().delete()
        Category.objects.all().delete()
        Manufacturer.objects.all().delete()
        Supplier.objects.all().delete()
        MedicinePhysicalState.objects.all().delete()
        RouteOfAdministration.objects.all().delete()
        Brand.objects.all().delete()
        Ingredient.objects.all().delete()
        Cart.objects.all().delete()
        CartProduct.objects.all().delete()
        Checkout.objects.all().delete()
        CheckoutProduct.objects.all().delete()

        dhaka = District.objects.create(name='dhaka')
        rajshahi = District.objects.create(name='rajshahi')
        chittagong = District.objects.create(name='chittagong')
        disc = [dhaka, rajshahi, chittagong]

        # user ids
        users_id = []
        merchants_id = []
        admins_id = []

        def create_address(user: Users):

            UserAddress.objects.create(
                user=user,
                label=fake.name(),
                house=fake.text(15),
                street=fake.text(15),
                post_office=fake.text(15),
                police_station=fake.text(15),
                country=fake.text(15),
                state=fake.text(15),
                district=random.choice(disc),
            )

        # Create 60 users

        self.stdout.write("creating user")
        # creating real user
        user1 = Users.objects.create_user("Saifullah Shahen", "+8801521475690", "123456")
        user1.image = generate_image()
        user1.save()
        create_address(user=user1)
        users_id.append(user1.id)

        for i in range(60):
            self.stdout.write(f'{i + 1}', ending=" ")
            name = fake.name()  # Generate a fake name
            phone_number = fake.phone_number()
            password = "123456"
            user = Users.objects.create_user(name, phone_number, password)
            user.image = generate_image()
            user.save()
            create_address(user=user)
            users_id.append(user.id)

        # Create 60 merchants
        self.stdout.write("\n")
        self.stdout.write("creating merchant")
        # creating real user
        merchant1 = Users.objects.create_merchant_owner("Mr Sajjadul Islam", "+8801752495466", "123456")
        merchant1.image = generate_image()
        merchant1.save()
        tenant1 = Tenant.objects.create(
            url=merchant1.name
        )
        MerchantInformation.objects.create(
            user=merchant1,
            merchant_domain=tenant1,
            company_name=fake.name(),
        )
        create_address(user=merchant1)
        merchants_id.append(merchant1.id)

        for i in range(60):
            self.stdout.write(f'{i + 1}', ending=" ")
            name = fake.name()
            phone_number = fake.phone_number()
            password = "123456"
            merchant = Users.objects.create_merchant_owner(name, phone_number, password)
            merchant.image = generate_image()
            merchant.save()

            tenant = Tenant.objects.create(
                url=merchant.name
            )

            MerchantInformation.objects.create(
                user=merchant,
                merchant_domain=tenant,
                company_name=fake.name(),
            )

            create_address(user=merchant)
            merchants_id.append(merchant.id)

        # Create 60 admins
        self.stdout.write("\n")
        self.stdout.write("creating superuser")
        # creating real user
        admin1 = Users.objects.create_superuser("James Clear", "+8801752495467", "123456")
        admin1.image = generate_image()
        admin1.save()
        create_address(user=admin1)
        admins_id.append(admin1.id)

        for i in range(60):
            self.stdout.write(f'{i + 1}', ending=" ")
            name = fake.name()
            phone_number = fake.phone_number()
            password = "123456"
            admin = Users.objects.create_superuser(name, phone_number, password)
            admin.image = generate_image()
            admin.save()

            create_address(user=admin)
            admins_id.append(admin.id)

        # create product attribute

        categories_id = []
        Manufacturer_id = []
        suppliers_id = []
        medicinePhysicalStates_id = []
        routeOfAdministrations_id = []
        brands_id = []
        ingredients_id = []
        base_prod_id = []
        product_id = []

        categories = ["Analgesics", "Analgesics", "Antianxiety Drugs", "Antiarrhythmics"]
        ingredients = ["Clonazepam", "Minoxidil", "ingredient1", "ingredient2"]
        brands = ["Square Pharmaceuticals", "Incepta Pharmaceutical Ltd.", "Beximco Pharmaceuticals LTD.",
                  "Opsonin Pharma Ltd."]
        manufacturers = ["manufacturers1", "manufacturers2", "manufacturers3", "manufacturers4"]
        suppliers = ["suppliers1", "suppliers2", "suppliers3", "suppliers4", "suppliers5"]
        medicinePhysicalStates = ["medicinePhysicalStates", "medicinePhysicalStates1", "medicinePhysicalStates2",
                                  "medicinePhysicalStates3", "medicinePhysicalStates4"]
        routeOfAdministrations = ["routeOfAdministrations", "routeOfAdministrations1", "routeOfAdministrations3",
                                  "routeOfAdministrations2", "routeOfAdministrations4"]
        with transaction.atomic():
            self.stdout.write("Creating product attributes")
            for category in categories:
                cat = Category.objects.create(
                    name=category
                )
                categories_id.append(cat.id)
            for i in manufacturers:
                manu = Manufacturer.objects.create(
                    name=i
                )
                Manufacturer_id.append(manu.id)
            for i in suppliers:
                supp = Supplier.objects.create(
                    name=i
                )
                suppliers_id.append(supp.id)
            for i in medicinePhysicalStates:
                mps = MedicinePhysicalState.objects.create(
                    name=i
                )
                medicinePhysicalStates_id.append(mps.id)
            for i in routeOfAdministrations:
                roa = RouteOfAdministration.objects.create(
                    name=i
                )
                routeOfAdministrations_id.append(roa.id)
            for brand in brands:
                brands = Brand.objects.create(
                    name=brand
                )
                brands_id.append(brands.id)
            for ingredient in ingredients:
                ing = Ingredient.objects.create(
                    name=ingredient
                )
                ingredients_id.append(ing.id)

            self.stdout.write("Creating base products")

            for i in range(100):
                base_product = BaseProduct.objects.create(
                    superadmin_id=random.choice(admins_id),
                    name=fake.name(),
                    description=fake.name(),
                    dosage_form=fake.name(),
                    manufacturer_id=random.choice(Manufacturer_id),
                    brand_id=random.choice(brands_id),
                    route_of_administration_id=random.choice(routeOfAdministrations_id),
                    medicine_physical_state_id=random.choice(medicinePhysicalStates_id)
                )
                base_prod_id.append(base_product.id)
                cate_add = random.sample(categories_id, k=2)
                ing_add = random.sample(ingredients_id, k=2)
                self.stdout.write("Creating base product categories and ingredients")
                for j in range(2):
                    base_product.category.add(cate_add[j])
                    base_product.active_ingredient.add(ing_add[j])

                for _ in range(3):
                    ProductImage.objects.create(
                        base_product=base_product,
                        image=generate_image()
                    )

            self.stdout.write("Creating merchant products")
            for i in base_prod_id:
                for merchant in random.sample(merchants_id, k=20):
                    user = Users.objects.get(pk=merchant)
                    buying = random.randint(100, 1000)
                    selling = buying + random.randint(10, 100)
                    product = Product.objects.create(
                        base_product_id=i,
                        merchant=user,
                        merchant_domain=user.get_user_information.merchant_domain,
                        stock=random.randint(100, 1000),
                        selling_price=selling,
                        buying_price=buying
                    )
                    product_id.append(product.id)

            carts_id = []
            self.stdout.write("Creating user carts")
            for user in random.sample(users_id, k=50):
                cart = Cart.objects.create(
                    customer_id=user
                )
                carts_id.append(cart.id)

                for product in random.sample(product_id, k=50):
                    prod = Product.objects.get(pk=product)
                    CartProduct.objects.create(
                        cart=cart,
                        product=prod,
                        quantity=random.randint(1, 10),
                        merchant=prod.merchant
                    )

            self.stdout.write("Creating checkout")
            for cart in random.sample(carts_id, k=40):
                cart_obj = Cart.objects.prefetch_related('get_cart_products').get(pk=cart)
                add = UserAddress.objects.get(user=cart_obj.customer)
                checkout = Checkout.objects.create(
                    customer=cart_obj.customer,
                    cart=cart_obj,
                    total_price=cart_obj.total_price + 100,
                    location=add,
                    delivery_charge=100,
                    payment_method=0,
                )
                for prod in cart_obj.get_cart_products.all():
                    CheckoutProduct.objects.create(
                        checkout=checkout,
                        product=prod.product,
                        quantity=prod.quantity,
                        selling_price=prod.product.selling_price,
                        merchant=prod.product.merchant
                    )
