from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline

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

# =========================
# NAVBAR ADMIN
# =========================


class NavigationItemInline(TranslationTabularInline):
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
class NavbarAdmin(TranslationAdmin):
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


# =========================
# HERO SLIDE ADMIN
# =========================


@admin.register(HeroSlide)
class HeroSlideAdmin(TranslationAdmin):

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


class AboutFeatureInline(TranslationTabularInline):

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
class AboutSectionAdmin(TranslationAdmin):

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


class ServiceCardInline(TranslationTabularInline):

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
class ServiceSectionAdmin(TranslationAdmin):

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


class WhyChooseUsItemInline(TranslationTabularInline):

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
class WhyChooseUsSectionAdmin(TranslationAdmin):

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


class HowItWorksStepInline(TranslationTabularInline):

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
class HowItWorksSectionAdmin(TranslationAdmin):

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


# =========================
# TESTIMONIAL ADMIN
# =========================


class TestimonialInline(TranslationTabularInline):
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
class TestimonialSectionAdmin(TranslationAdmin):
    list_display = ("id", "label", "heading", "is_active")
    list_editable = ("is_active",)
    inlines = [TestimonialInline]


# =========================
# BOOK TODAY ADMIN
# =========================


class BookTodayContactInline(TranslationTabularInline):
    model = BookTodayContact
    extra = 4
    max_num = 4
    fields = (
        "icon_class",
        "label",
        "value",
        "link_url",
        "display_order",
        "is_active",
    )
    ordering = ("display_order",)


@admin.register(BookTodaySection)
class BookTodaySectionAdmin(TranslationAdmin):
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


# =========================
# FOOTER ADMIN
# =========================


class FooterQuickLinkInline(TranslationTabularInline):
    model = FooterQuickLink
    extra = 1
    fields = ("title", "url", "display_order", "is_active")
    ordering = ("display_order",)


class FooterServiceInline(TranslationTabularInline):
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
class FooterSectionAdmin(TranslationAdmin):
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
