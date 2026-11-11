from django.contrib import admin
from .models import (
    Navbar,
    NavigationItem,
    HeroSlide,
    AboutSection,
    AboutFeature,
    ServiceSection,
    ServiceCard,
    WhyChooseUsItem,
    WhyChooseUsSection,
    HowItWorksSection,
    HowItWorksStep,
    TestimonialSection,
    Testimonial,
    BookTodaySection,
    BookTodayContact,
    FooterSection,
    FooterQuickLink,
    FooterService,
    FooterContact,
    FooterSocialLink,
)


class NavigationItemInline(admin.TabularInline):
    model = NavigationItem
    extra = 1
    fields = (
        "label",
        "link",
        "display_order",
        "is_active",
    )
    ordering = ("display_order",)


@admin.register(Navbar)
class NavbarAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "logo_alt_text",
        "button_text",
        "background_color",
        "is_active",
    )

    list_filter = ("is_active",)

    fieldsets = (
        (
            "Company Logo",
            {
                "fields": (
                    "logo",
                    "logo_alt_text",
                )
            },
        ),
        ("Navbar Appearance", {"fields": ("background_color",)}),
        (
            "Book a Service Button",
            {
                "fields": (
                    "button_text",
                    "button_link",
                    "button_background_color",
                    "button_text_color",
                )
            },
        ),
        ("Status", {"fields": ("is_active",)}),
    )

    inlines = [NavigationItemInline]


@admin.register(HeroSlide)
class HeroSlideAdmin(admin.ModelAdmin):

    list_display = (
        "display_order",
        "badge_text",
        "heading",
        "is_active",
    )

    list_filter = (
        "is_active",
        "display_order",
    )

    list_editable = ("is_active",)

    ordering = ("display_order",)

    fieldsets = (
        (
            "Slide Background",
            {
                "fields": (
                    "background_image",
                    "image_alt_text",
                )
            },
        ),
        (
            "Badge and Content",
            {
                "fields": (
                    "badge_text",
                    "heading",
                    "description",
                )
            },
        ),
        (
            "Primary Button",
            {
                "fields": (
                    "primary_button_text",
                    "primary_button_link",
                )
            },
        ),
        (
            "Secondary Button",
            {
                "fields": (
                    "secondary_button_text",
                    "secondary_button_link",
                )
            },
        ),
        (
            "Slide Settings",
            {
                "fields": (
                    "display_order",
                    "is_active",
                )
            },
        ),
    )


# =========================
# ABOUT US ADMIN
# =========================


class AboutFeatureInline(admin.TabularInline):

    model = AboutFeature
    extra = 3
    max_num = 3

    fields = (
        "icon_class",
        "title",
        "display_order",
        "is_active",
    )

    ordering = ("display_order",)


@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "label",
        "heading",
        "experience_number",
        "is_active",
    )

    list_filter = ("is_active",)

    fieldsets = (
        (
            "About Us Image",
            {
                "fields": (
                    "image",
                    "image_alt_text",
                )
            },
        ),
        (
            "About Us Content",
            {
                "fields": (
                    "label",
                    "heading",
                    "description_one",
                    "description_two",
                )
            },
        ),
        (
            "Experience Badge",
            {
                "fields": (
                    "experience_number",
                    "experience_label",
                )
            },
        ),
        (
            "Section Settings",
            {"fields": ("is_active",)},
        ),
    )

    inlines = [AboutFeatureInline]


# =========================
# SERVICES ADMIN
# =========================


class ServiceCardInline(admin.TabularInline):

    model = ServiceCard

    extra = 10
    max_num = 10

    fields = (
        "image",
        "image_alt_text",
        "title",
        "description",
        "price",
        "button_text",
        "button_link",
        "display_order",
        "is_active",
    )

    ordering = ("display_order",)


@admin.register(ServiceSection)
class ServiceSectionAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "label",
        "heading",
        "is_active",
    )

    list_filter = ("is_active",)

    fieldsets = (
        (
            "Services Section Heading",
            {
                "fields": (
                    "label",
                    "heading",
                    "description",
                )
            },
        ),
        (
            "Section Settings",
            {"fields": ("is_active",)},
        ),
    )

    inlines = [ServiceCardInline]


# =========================
# WHY CHOOSE US ADMIN
# =========================


class WhyChooseUsItemInline(admin.TabularInline):

    model = WhyChooseUsItem
    extra = 4
    max_num = 4

    fields = (
        "icon_class",
        "title",
        "description",
        "display_order",
        "is_active",
    )

    ordering = ("display_order",)


@admin.register(WhyChooseUsSection)
class WhyChooseUsSectionAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "label",
        "heading",
        "is_active",
    )

    list_filter = ("is_active",)

    fieldsets = (
        (
            "Section Content",
            {
                "fields": (
                    "label",
                    "heading",
                )
            },
        ),
        (
            "Section Settings",
            {"fields": ("is_active",)},
        ),
    )

    inlines = [WhyChooseUsItemInline]


# =========================
# HOW IT WORKS ADMIN
# =========================


class HowItWorksStepInline(admin.TabularInline):

    model = HowItWorksStep

    extra = 4
    max_num = 4

    fields = (
        "icon_class",
        "title",
        "description",
        "display_order",
        "is_active",
    )

    ordering = ("display_order",)


@admin.register(HowItWorksSection)
class HowItWorksSectionAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "label",
        "heading",
        "is_active",
    )

    list_filter = ("is_active",)

    fieldsets = (
        (
            "Section Content",
            {
                "fields": (
                    "label",
                    "heading",
                )
            },
        ),
        (
            "Section Settings",
            {"fields": ("is_active",)},
        ),
    )

    inlines = [HowItWorksStepInline]


class TestimonialInline(admin.TabularInline):
    model = Testimonial
    extra = 4
    max_num = 4
    fields = (
        "name",
        "description",
        "display_order",
        "is_verified",
        "is_active",
    )
    ordering = ("display_order",)


@admin.register(TestimonialSection)
class TestimonialSectionAdmin(admin.ModelAdmin):
    list_display = ("id", "label", "heading", "is_active")
    list_editable = ("is_active",)
    inlines = [TestimonialInline]


class BookTodayContactInline(admin.TabularInline):
    model = BookTodayContact
    extra = 4
    max_num = 4
    fields = (
        "icon_class",
        "label",
        "value",
        "display_order",
        "is_active",
    )
    ordering = ("display_order",)


@admin.register(BookTodaySection)
class BookTodaySectionAdmin(admin.ModelAdmin):
    list_display = ("id", "label", "heading", "is_active")
    list_editable = ("is_active",)
    fields = (
        "label",
        "heading",
        "description",
        "primary_button_text",
        "primary_button_url",
        "secondary_button_text",
        "whatsapp_url",
        "is_active",
    )
    inlines = [BookTodayContactInline]


class FooterQuickLinkInline(admin.TabularInline):
    model = FooterQuickLink
    extra = 1
    fields = ("title", "url", "display_order", "is_active")
    ordering = ("display_order",)


class FooterServiceInline(admin.TabularInline):
    model = FooterService
    extra = 1
    fields = ("title", "url", "display_order", "is_active")
    ordering = ("display_order",)


class FooterContactInline(admin.TabularInline):
    model = FooterContact
    extra = 1
    fields = (
        "icon_class",
        "value",
        "url",
        "display_order",
        "is_active",
    )
    ordering = ("display_order",)


class FooterSocialLinkInline(admin.TabularInline):
    model = FooterSocialLink
    extra = 1
    fields = (
        "platform",
        "icon_class",
        "url",
        "display_order",
        "is_active",
    )
    ordering = ("display_order",)


@admin.register(FooterSection)
class FooterSectionAdmin(admin.ModelAdmin):
    list_display = ("id", "quick_links_heading", "is_active")
    list_editable = ("is_active",)

    fields = (
        "logo",
        "description",
        "quick_links_heading",
        "services_heading",
        "contact_heading",
        "copyright_text",
        "is_active",
    )

    inlines = [
        FooterQuickLinkInline,
        FooterServiceInline,
        FooterContactInline,
        FooterSocialLinkInline,
    ]
