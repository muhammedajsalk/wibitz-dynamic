from django.db import models


COMPANY_SIZE=(
    ("1","1-10"),
    ("2","11-50"),
    ("3","51-200"),
    ("4","201-500")
)


INDUSTRY=(
    ("1","Agriculture"),
    ("2","Banking & Finance"),
    ("3","Business Services & Software")
)


JOB_ROLE=(
    ("1","C-Suite"),
    ("2","VP")
)


COUNTRY=(
    ("us","United States"),
    ("albania","Albania")
)


class Subscribe(models.Model):
    email = models.EmailField()

    class Meta:
        db_table = "web_subscribe"
        ordering = ["-id"]
    
    def __str__(self):
        return self.email
    


class Customer(models.Model):
    image = models.FileField(upload_to="customers/")
    white_logo = models.FileField(upload_to="customers/",blank=True,null=True)

    class Meta:
        db_table = "web_customer"
        ordering = ["id"]
    
    def __str__(self):
        return str(self.id)

class Feature(models.Model):
    image = models.ImageField(upload_to="feature/")
    icon = models.FileField(upload_to="feature/")
    icon_background = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    testimonial_description = models.TextField()
    testimonial_author = models.CharField(max_length=255)
    author_designation = models.CharField(max_length=255)
    testimonial_logo = models.FileField(upload_to="feature/")

    class Meta:
        db_table = "web_feature"
        ordering = ["-id"]
    
    def __str__(self):
        return str(self.title)
    

class Videoblog(models.Model):
    image = models.ImageField(upload_to="videoblog/")
    title = models.CharField(max_length=255)
    logo =  models.FileField(upload_to="videoblog/")

    class Meta:
        db_table = "web_videoblog"
        ordering = ["-id"]
    
    def __str__(self):
        return str(self.title)
    

class Testimonial(models.Model):
    image = models.ImageField(upload_to="testimonial/")
    logo =  models.FileField(upload_to="testimonial/")
    description = models.TextField()
    name = models.CharField(max_length=255)
    author_designation = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    is_featured = models.BooleanField(default=True)


    class Meta:
        db_table = "web_testimonial"
        ordering = ["-id"]
    
    def __str__(self):
        return str(self.name)
    

class Marketing(models.Model):
    image = models.FileField(upload_to="marketing/")
    title = models.CharField(max_length=255)
    description = models.TextField()
    

    class Meta:
        db_table = "web_marketing"
        ordering = ["-id"]
    
    def __str__(self):
        return str(self.id)
    

class Product(models.Model):
    logo = models.FileField(upload_to="product/")
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    background_color = models.CharField(max_length=255)
    description = models.TextField()
    image =  models.ImageField(upload_to="product/")
    hero_image =  models.ImageField(upload_to="product/hero_images/")

    class Meta:
        db_table = "web_product"
        ordering = ["-id"]
    
    def __str__(self):
        return str(self.name)
    

class Blog(models.Model):
    BLOG_POST = 'blog post'
    WEBINAR = 'webinar'
    REPORT = 'report'
    
    CONTENT_CHOICES = [
        (BLOG_POST, 'Blog Post'),
        (WEBINAR, 'Webinar'),
        (REPORT, 'Report'),
    ]
    
    image = models.ImageField(upload_to="blog/")
    title = models.CharField(max_length=255)
    content_type = models.CharField(
        max_length=20,
        choices=CONTENT_CHOICES,
        default=BLOG_POST,
    )

    class Meta:
        db_table = "web_blog"
        ordering = ["-id"]
    
    def __str__(self):
        return str(self.title)


class Contact(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    company = models.CharField(max_length=128)
    company_size = models.CharField(max_length=128,choices=COMPANY_SIZE)
    industry = models.CharField(max_length=128,choices=INDUSTRY)
    job_role = models.CharField(max_length=128,choices=JOB_ROLE)
    country = models.CharField(max_length=128,choices=COUNTRY)
    user_agreement = models.BooleanField(default=False)

    class Meta:
        db_table = "web_contact"
        ordering = ["-id"]
    
    def __str__(self):
        return str(self.first_name)