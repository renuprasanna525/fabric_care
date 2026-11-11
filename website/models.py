from django.db import models
from django.core.exceptions import ValidationError


class Navbar(models.Model):
    logo = models.ImageField(upload_to="logo/", help_text="Upload the company logo")
    logo_alt_text = models.CharField(max_length=150, default="Iron Me Ka Logo")

    background_color = models.CharField(max_length=20, default="#FFFFFF")

    button_text = models.CharField(max_length=100, default="Book a Service")
    button_link = models.CharField(max_length=200, default="#contact")
    button_background_color = models.CharField(max_length=20, default="#741F3F")
    button_text_color = models.CharField(max_length=20, default="#FFFFFF")

    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Navbar Settings"
        verbose_name_plural = "Navbar Settings"

    def __str__(self):
        return "Iron Me Ka Navbar"


class NavigationItem(models.Model):
    navbar = models.ForeignKey(
        Navbar, on_delete=models.CASCADE, related_name="navigation_items"
    )
    label = models.CharField(max_length=100)
    link = models.CharField(
        max_length=200, help_text="Example: #home, #about, #services"
    )
    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["display_order"]
        verbose_name = "Navigation Link"
        verbose_name_plural = "Navigation Links"

    def __str__(self):
        return self.label


class HeroSlide(models.Model):
    background_image = models.ImageField(
        upload_to="hero/", help_text="Upload the background image for this slide"
    )
    image_alt_text = models.CharField(max_length=200, default="Iron Me Ka Fabric Care")
    badge_text = models.CharField(max_length=150, default="Saree Care")
    heading = models.CharField(max_length=250)
    description = models.TextField()
    primary_button_text = models.CharField(max_length=100, default="Book a Service")
    primary_button_link = models.CharField(max_length=200, default="#contact")
    secondary_button_text = models.CharField(max_length=100, default="View Services")
    secondary_button_link = models.CharField(max_length=200, default="#services")
    display_order = models.PositiveSmallIntegerField(
        default=1, help_text="Select slide order: 1, 2 or 3"
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["display_order"]
        verbose_name = "Hero Slide"
        verbose_name_plural = "Hero Slides"

    def clean(self):
        super().clean()

        if self.display_order not in (1, 2, 3):
            raise ValidationError({"display_order": "Slide order must be 1, 2 or 3."})

        duplicate = HeroSlide.objects.filter(display_order=self.display_order).exclude(
            pk=self.pk
        )

        if duplicate.exists():
            raise ValidationError(
                {"display_order": "This slide order is already in use."}
            )

    def __str__(self):
        return f"Hero Slide {self.display_order}: {self.heading}"


# =========================
# ABOUT US SECTION
# =========================


class AboutSection(models.Model):

    image = models.ImageField(
        upload_to="about/", help_text="Upload the main About Us image"
    )

    image_alt_text = models.CharField(
        max_length=200, default="Iron Me Ka professional fabric care"
    )

    label = models.CharField(max_length=100, default="ABOUT US")

    heading = models.CharField(
        max_length=250, default="Care That Makes Every Fabric Feel Special"
    )

    description_one = models.TextField(help_text="First About Us paragraph")

    description_two = models.TextField(help_text="Second About Us paragraph")

    experience_number = models.CharField(max_length=30, default="12+")

    experience_label = models.CharField(max_length=100, default="YEARS OF CARE")

    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "About Us Section"
        verbose_name_plural = "About Us Section"

    def __str__(self):
        return self.heading


class AboutFeature(models.Model):

    about_section = models.ForeignKey(
        AboutSection, on_delete=models.CASCADE, related_name="features"
    )

    icon_class = models.CharField(
        max_length=100,
        default="bi-award",
        help_text="Bootstrap Icon class. Example: bi-award",
    )

    title = models.CharField(max_length=150)

    display_order = models.PositiveSmallIntegerField(default=1)

    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["display_order"]
        verbose_name = "About Feature"
        verbose_name_plural = "About Features"

    def __str__(self):
        return self.title


# =========================
# SERVICES SECTION
# =========================


class ServiceSection(models.Model):

    label = models.CharField(max_length=100, default="WHAT WE DO")

    heading = models.CharField(max_length=250, default="Our Fabric Care Services")

    description = models.TextField(
        default="Specialized care and finishing for your everyday wear and traditional fabrics."
    )

    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Services Section"
        verbose_name_plural = "Services Section"

    def __str__(self):
        return self.heading


class ServiceCard(models.Model):

    service_section = models.ForeignKey(
        ServiceSection, on_delete=models.CASCADE, related_name="service_cards"
    )

    image = models.ImageField(
        upload_to="services/", help_text="Upload the service card image"
    )

    image_alt_text = models.CharField(
        max_length=200, default="Iron Me Ka Fabric Care Service"
    )

    title = models.CharField(max_length=200)

    description = models.TextField()

    price = models.CharField(max_length=50, help_text="Example: ₹60")

    button_text = models.CharField(max_length=50, default="Book Now")

    button_link = models.CharField(max_length=200, default="#contact")

    display_order = models.PositiveSmallIntegerField(
        default=1, help_text="Enter a unique service order from 1 to 10"
    )

    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["display_order"]
        verbose_name = "Service Card"
        verbose_name_plural = "Service Cards"
        constraints = [
            models.UniqueConstraint(
                fields=["service_section", "display_order"],
                name="unique_service_section_display_order",
            )
        ]

    def clean(self):
        super().clean()

        if self.display_order not in range(1, 11):
            raise ValidationError(
                {"display_order": "Service order must be between 1 and 10."}
            )

    def __str__(self):
        return f"{self.display_order:02d} - {self.title}"


# =========================
# WHY CHOOSE US SECTION
# =========================


class WhyChooseUsSection(models.Model):

    label = models.CharField(max_length=100, default="WHY CHOOSE US")

    heading = models.CharField(max_length=250, default="The Vastra Care Difference")

    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Why Choose Us Section"
        verbose_name_plural = "Why Choose Us Section"

    def __str__(self):
        return self.heading


class WhyChooseUsItem(models.Model):

    section = models.ForeignKey(
        WhyChooseUsSection, on_delete=models.CASCADE, related_name="items"
    )

    icon_class = models.CharField(
        max_length=100,
        default="bi-award",
        help_text="Bootstrap Icon class. Example: bi-award",
    )

    title = models.CharField(max_length=150)

    description = models.TextField()

    display_order = models.PositiveSmallIntegerField(default=1)

    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["display_order"]
        verbose_name = "Why Choose Us Item"
        verbose_name_plural = "Why Choose Us Items"
        constraints = [
            models.UniqueConstraint(
                fields=["section", "display_order"],
                name="unique_why_choose_us_display_order",
            )
        ]

    def clean(self):
        super().clean()

        if self.display_order not in range(1, 5):
            raise ValidationError(
                {"display_order": "Feature order must be between 1 and 4."}
            )

    def __str__(self):
        return f"{self.display_order:02d} - {self.title}"


# =========================
# HOW IT WORKS SECTION
# =========================


class HowItWorksSection(models.Model):

    label = models.CharField(max_length=100, default="HOW IT WORKS")

    heading = models.CharField(max_length=250, default="Simple, Careful, Complete")

    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "How It Works Section"
        verbose_name_plural = "How It Works Section"

    def __str__(self):
        return self.heading


class HowItWorksStep(models.Model):

    section = models.ForeignKey(
        HowItWorksSection, on_delete=models.CASCADE, related_name="steps"
    )

    icon_class = models.CharField(
        max_length=100,
        default="bi-calendar-check",
        help_text="Bootstrap Icon class. Example: bi-calendar-check",
    )

    title = models.CharField(max_length=150)

    description = models.TextField()

    display_order = models.PositiveSmallIntegerField(default=1)

    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["display_order"]
        verbose_name = "How It Works Step"
        verbose_name_plural = "How It Works Steps"

        constraints = [
            models.UniqueConstraint(
                fields=["section", "display_order"],
                name="unique_how_it_works_step_order",
            )
        ]

    def clean(self):
        super().clean()

        if self.display_order not in range(1, 5):
            raise ValidationError(
                {"display_order": "Step order must be between 1 and 4."}
            )

    def __str__(self):
        return f"{self.display_order:02d} - {self.title}"


class TestimonialSection(models.Model):
    label = models.CharField(max_length=100, default="TESTIMONIALS")
    heading = models.CharField(max_length=250, default="Loved by Our Customers")
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Testimonials Section"
        verbose_name_plural = "Testimonials Section"

    def __str__(self):
        return self.heading


class Testimonial(models.Model):
    section = models.ForeignKey(
        TestimonialSection, on_delete=models.CASCADE, related_name="testimonials"
    )
    name = models.CharField(max_length=150)
    description = models.TextField()
    display_order = models.PositiveSmallIntegerField(default=1)
    is_verified = models.BooleanField(
        default=True, help_text="Display the Verified Customer label."
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["display_order"]
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"
        constraints = [
            models.UniqueConstraint(
                fields=["section", "display_order"],
                name="unique_testimonial_display_order",
            )
        ]

    def clean(self):
        super().clean()

        if self.display_order not in range(1, 5):
            raise ValidationError(
                {"display_order": "Testimonial order must be between 1 and 4."}
            )

    def __str__(self):
        return f"{self.display_order:02d} - {self.name}"


class BookTodaySection(models.Model):
    label = models.CharField(max_length=100, default="BOOK TODAY")
    heading = models.CharField(
        max_length=250, default="Give Your Clothes the Care They Deserve"
    )
    description = models.TextField(
        default=(
            "From everyday ironing to delicate saree and traditional "
            "wear care, we make every piece look its best."
        )
    )
    primary_button_text = models.CharField(max_length=100, default="Book a Service")
    primary_button_url = models.CharField(max_length=300, default="#booking")
    secondary_button_text = models.CharField(max_length=100, default="WhatsApp Us")
    whatsapp_url = models.URLField(max_length=500, default="https://wa.me/919790263322")
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Book Today Section"
        verbose_name_plural = "Book Today Section"

    def __str__(self):
        return self.heading


class BookTodayContact(models.Model):
    section = models.ForeignKey(
        BookTodaySection, on_delete=models.CASCADE, related_name="contact_items"
    )
    icon_class = models.CharField(
        max_length=100,
        default="bi-telephone",
        help_text="Bootstrap Icon class. Example: bi-telephone",
    )
    label = models.CharField(max_length=100)
    value = models.TextField()
    link_url = models.CharField(
        max_length=500,
        blank=True,
        help_text="Examples: tel:+919514242834, https://wa.me/919514242834, or Google Maps URL.",
    )
    display_order = models.PositiveSmallIntegerField(default=1)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["display_order"]
        verbose_name = "Book Today Contact"
        verbose_name_plural = "Book Today Contacts"
        constraints = [
            models.UniqueConstraint(
                fields=["section", "display_order"],
                name="unique_book_today_contact_order",
            )
        ]

    def clean(self):
        super().clean()

        if self.display_order not in range(1, 5):
            raise ValidationError(
                {"display_order": "Contact order must be between 1 and 4."}
            )

    def __str__(self):
        return f"{self.display_order:02d} - {self.label}"


class FooterSection(models.Model):
    logo = models.ImageField(
        upload_to="footer/",
        blank=True,
        null=True,
        help_text="Upload your Vastra Care logo.",
    )
    description = models.TextField(
        default=(
            "Premium saree and fabric care — rolling, pleating, "
            "polishing, starching and steaming, done by hand with precision."
        )
    )
    quick_links_heading = models.CharField(max_length=100, default="Quick Links")
    services_heading = models.CharField(max_length=100, default="Services")
    contact_heading = models.CharField(max_length=100, default="Contact")
    copyright_text = models.CharField(
        max_length=250, default="© 2026 Vastra Care. All rights reserved."
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Footer Section"
        verbose_name_plural = "Footer Section"

    def __str__(self):
        return "Website Footer"


class FooterQuickLink(models.Model):
    section = models.ForeignKey(
        FooterSection, on_delete=models.CASCADE, related_name="quick_links"
    )
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=300, help_text="Example: #home or /about/")
    display_order = models.PositiveSmallIntegerField(default=1)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["display_order"]
        verbose_name = "Footer Quick Link"
        verbose_name_plural = "Footer Quick Links"

    def __str__(self):
        return self.title


class FooterService(models.Model):
    section = models.ForeignKey(
        FooterSection, on_delete=models.CASCADE, related_name="footer_services"
    )
    title = models.CharField(max_length=150)
    url = models.CharField(
        max_length=300, blank=True, help_text="Optional link, for example #services"
    )
    display_order = models.PositiveSmallIntegerField(default=1)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["display_order"]
        verbose_name = "Footer Service"
        verbose_name_plural = "Footer Services"

    def __str__(self):
        return self.title


class FooterContact(models.Model):
    section = models.ForeignKey(
        FooterSection, on_delete=models.CASCADE, related_name="footer_contacts"
    )
    icon_class = models.CharField(
        max_length=100,
        default="bi-telephone",
        help_text="Bootstrap Icon class. Example: bi-telephone",
    )
    value = models.TextField()
    url = models.CharField(
        max_length=500,
        blank=True,
        help_text="Optional link, such as tel:+919790263322 or mailto:hello@example.com",
    )
    display_order = models.PositiveSmallIntegerField(default=1)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["display_order"]
        verbose_name = "Footer Contact"
        verbose_name_plural = "Footer Contacts"

    def __str__(self):
        return self.value[:60]


class FooterSocialLink(models.Model):
    section = models.ForeignKey(
        FooterSection, on_delete=models.CASCADE, related_name="social_links"
    )
    platform = models.CharField(max_length=50)
    icon_class = models.CharField(
        max_length=100, help_text="Example: bi-instagram, bi-facebook, bi-youtube"
    )
    url = models.URLField(max_length=500)
    display_order = models.PositiveSmallIntegerField(default=1)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["display_order"]
        verbose_name = "Footer Social Link"
        verbose_name_plural = "Footer Social Links"

    def __str__(self):
        return self.platform
