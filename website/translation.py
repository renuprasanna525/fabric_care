from modeltranslation.translator import register, TranslationOptions

from .models import (
    Navbar,
    NavigationItem,
    HeroSlide,
    AboutSection,
    AboutFeature,
    ServiceSection,
    ServiceCard,
    WhyChooseUsSection,
    WhyChooseUsItem,
    HowItWorksSection,
    HowItWorksStep,
    TestimonialSection,
    Testimonial,
    BookTodaySection,
    BookTodayContact,
    FooterSection,
    FooterQuickLink,
    FooterService,
)


@register(Navbar)
class NavbarTranslationOptions(TranslationOptions):
    fields = ("logo_alt_text", "button_text")


@register(NavigationItem)
class NavigationItemTranslationOptions(TranslationOptions):
    fields = ("label",)


@register(HeroSlide)
class HeroSlideTranslationOptions(TranslationOptions):
    fields = (
        "image_alt_text",
        "badge_text",
        "heading",
        "description",
        "primary_button_text",
        "secondary_button_text",
    )


@register(AboutSection)
class AboutSectionTranslationOptions(TranslationOptions):
    fields = (
        "image_alt_text",
        "label",
        "heading",
        "description_one",
        "description_two",
        "experience_label",
    )


@register(AboutFeature)
class AboutFeatureTranslationOptions(TranslationOptions):
    fields = ("title",)


@register(ServiceSection)
class ServiceSectionTranslationOptions(TranslationOptions):
    fields = ("label", "heading", "description")


@register(ServiceCard)
class ServiceCardTranslationOptions(TranslationOptions):
    fields = ("image_alt_text", "title", "description", "button_text")


@register(WhyChooseUsSection)
class WhyChooseUsSectionTranslationOptions(TranslationOptions):
    fields = ("label", "heading")


@register(WhyChooseUsItem)
class WhyChooseUsItemTranslationOptions(TranslationOptions):
    fields = ("title", "description")


@register(HowItWorksSection)
class HowItWorksSectionTranslationOptions(TranslationOptions):
    fields = ("label", "heading")


@register(HowItWorksStep)
class HowItWorksStepTranslationOptions(TranslationOptions):
    fields = ("title", "description")


@register(TestimonialSection)
class TestimonialSectionTranslationOptions(TranslationOptions):
    fields = ("label", "heading")


@register(Testimonial)
class TestimonialTranslationOptions(TranslationOptions):
    fields = ("name", "description")


@register(BookTodaySection)
class BookTodaySectionTranslationOptions(TranslationOptions):
    fields = (
        "label",
        "heading",
        "description",
        "primary_button_text",
        "secondary_button_text",
    )


@register(BookTodayContact)
class BookTodayContactTranslationOptions(TranslationOptions):
    fields = ("label",)


@register(FooterSection)
class FooterSectionTranslationOptions(TranslationOptions):
    fields = (
        "description",
        "quick_links_heading",
        "services_heading",
        "contact_heading",
        "copyright_text",
    )


@register(FooterQuickLink)
class FooterQuickLinkTranslationOptions(TranslationOptions):
    fields = ("title",)


@register(FooterService)
class FooterServiceTranslationOptions(TranslationOptions):
    fields = ("title",)
