from rest_framework import serializers
from drf_recaptcha.fields import ReCaptchaV2Field, ReCaptchaV3Field
from web.models import Slider, SliderSlidesThroughModel, Configuration, Setting, Slide
from sorl.thumbnail import get_thumbnail
from django.contrib.sites.models import Site

REASON_CHOICES = [
    'Urgent: Change Order detail or Address',
    'Question about order or Delivery',
    'Press Contact & Media',
    'Wholesale, Discount, promo code query',
    'Product Question',
    'Other'
]


class ContactFormSerializer(serializers.Serializer):
    email = serializers.EmailField()
    name = serializers.CharField(max_length=200)
    address = serializers.CharField(max_length=200)
    subject = serializers.CharField(max_length=200, required=False)
    reason = serializers.ChoiceField(choices=REASON_CHOICES,)
    message = serializers.CharField()
    recaptcha = ReCaptchaV2Field()


class SlideSerializer(serializers.ModelSerializer):
    desktop_resized = serializers.SerializerMethodField()   
    desktop_webp = serializers.SerializerMethodField()
    mobile_webp = serializers.SerializerMethodField()

    def get_desktop_resized(self, obj):
            request = self.context.get("request")
            resize_w = request.query_params.get('resize_w',None)
            resize_h = request.query_params.get('resize_h',None)
            domain = Site.objects.get_current().domain
            if resize_h is None and resize_w is None:
                resize_w = "1440"
            if resize_w is None:
                resize_w = ""
            if resize_h is None:
                height = ""
            else:
                height = f"x{resize_h}"
            if obj.slide.desktop_image:
                return domain+get_thumbnail(obj.slide.desktop_image, f'{resize_w}{height}', quality=100, format="PNG").url

    def get_desktop_webp(self, obj):
            request = self.context.get("request")
            resize_w = request.query_params.get('resize_w',None)
            resize_h = request.query_params.get('resize_h',None)
            domain = Site.objects.get_current().domain
            if resize_h is None and resize_w is None:
                resize_w = "1440"
            if resize_w is None:
                resize_w = ""
            if resize_h is None:
                height = ""
            else:
                height = f"x{resize_h}"
            if obj.slide.desktop_image:
                return domain+get_thumbnail(obj.slide.desktop_image, f'{resize_w}{height}', quality=100, format="WEBP").url
    
    def get_mobile_webp(self, obj):
            # request = self.context.get("request")
            # resize_w = request.query_params.get('resize_w',None)
            # resize_h = request.query_params.get('resize_h',None)
            domain = Site.objects.get_current().domain
            # if resize_h is None and resize_w is None:
            #     resize_w = "600"
            # if resize_w is None:
            #     resize_w = ""
            # if resize_h is None:
            #     height = ""
            # else:
            #     height = f"x{resize_h}"
            if obj.slide.mobile_image:
                return domain+get_thumbnail(obj.slide.mobile_image,f"640", quality=100, format="WEBP").url
    class Meta:
        model = SliderSlidesThroughModel
        fields = '__all__'
        depth = 2


class SliderSerializer(serializers.ModelSerializer):
    # slides = serializers.SerializerMethodField()
    slider_slides = SlideSerializer(many=True, read_only=True)

    class Meta:
        model = Slider
        fields = '__all__'
        depth = 2


class ConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Configuration
        fields = '__all__'
        lookup_field = 'key'