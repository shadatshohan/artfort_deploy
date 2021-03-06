from django.shortcuts import render

# Create your views here.
class Product(models.Model):
    status = (
        ('True', 'True'),
        ('False', 'False'),)
    VARIANTS = (
        ('None', 'None'),
        ('Size', 'Size'),
        ('Color', 'Color'),
        ('Size-Color', 'Size-Color'),

    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    keywords = models.CharField(max_length=100,blank=True)
    image = models.ImageField(blank=True, upload_to='product/')
    new_price = models.DecimalField(decimal_places=2, max_digits=15, default=0)
    old_price = models.DecimalField(decimal_places=2, max_digits=15)
    amount = models.IntegerField(default=0) 
    min_amount = models.IntegerField(default=1)
    variant = models.CharField(max_length=10, choices=VARIANTS, default='None')
    detail = models.TextField()
    status = models.CharField(max_length=20, choices=status)
    slug = models.SlugField(null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def ImageUrl(self):
        if self.image:
            return self.image.url
        else:
            return ""

    def image_tag(self):
        if self.image:
            return mark_safe('<img src="{}" heights="70" width="60" />'.format(self.image.url))
        else:
            return ""
    image_tag.short_description = 'Image'


class BannerImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str(self):
        return self.title