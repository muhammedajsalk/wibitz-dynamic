from django.db import models


class Subscribe(models.Model):
    email = models.EmailField()

    class Meta:
        db_table = "web_subscribe"
        ordering = ["-id"]
    
    def __str__(self):
        return self.email
    


class Customer(models.Model):
    image = models.FileField(upload_to="customers/")

    class Meta:
        db_table = "web_customer"
        ordering = ["-id"]
    
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
    description = models.TextField()
    image =  models.ImageField(upload_to="product/")

    class Meta:
        db_table = "web_product"
        ordering = ["-id"]
    
    def __str__(self):
        return str(self.title)
    

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