from django.shortcuts import render
from django.db.models import Prefetch
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


def home(request):

    # NAVBAR
    navbar = Navbar.objects.filter(is_active=True).first()

    navigation_items = (
        NavigationItem.objects.filter(navbar=navbar, is_active=True).order_by(
            "display_order"
        )
        if navbar
        else []
    )

    # HERO CAROUSEL
    hero_slides = HeroSlide.objects.filter(is_active=True).order_by("display_order")[:3]

    # ABOUT US
    about_section = (
        AboutSection.objects.filter(is_active=True)
        .prefetch_related(
            Prefetch(
                "features",
                queryset=AboutFeature.objects.filter(is_active=True).order_by(
                    "display_order"
                ),
                to_attr="active_features",
            )
        )
        .first()
    )

    # SERVICES SECTION
    service_section = (
        ServiceSection.objects.filter(is_active=True)
        .prefetch_related(
            Prefetch(
                "service_cards",
                queryset=ServiceCard.objects.filter(is_active=True).order_by(
                    "display_order"
                ),
                to_attr="active_service_cards",
            )
        )
        .first()
    )

    # WHY CHOOSE US SECTION
    why_choose_us = (
        WhyChooseUsSection.objects.filter(is_active=True)
        .prefetch_related(
            Prefetch(
                "items",
                queryset=WhyChooseUsItem.objects.filter(is_active=True).order_by(
                    "display_order"
                ),
                to_attr="active_items",
            )
        )
        .first()
    )

    # HOW IT WORKS SECTION
    how_it_works = (
        HowItWorksSection.objects.filter(is_active=True)
        .prefetch_related(
            Prefetch(
                "steps",
                queryset=HowItWorksStep.objects.filter(is_active=True).order_by(
                    "display_order"
                ),
                to_attr="active_steps",
            )
        )
        .first()
    )

    # TESTIMONIALS SECTION
    testimonials = (
        TestimonialSection.objects.filter(is_active=True)
        .prefetch_related(
            Prefetch(
                "testimonials",
                queryset=Testimonial.objects.filter(is_active=True).order_by(
                    "display_order"
                ),
                to_attr="active_testimonials",
            )
        )
        .first()
    )

    # BOOK TODAY SECTION
    book_today = (
        BookTodaySection.objects.filter(is_active=True)
        .prefetch_related(
            Prefetch(
                "contact_items",
                queryset=BookTodayContact.objects.filter(is_active=True).order_by(
                    "display_order"
                ),
                to_attr="active_contact_items",
            )
        )
        .first()
    )

    footer = (
        FooterSection.objects.filter(is_active=True)
        .prefetch_related(
            Prefetch(
                "quick_links",
                queryset=FooterQuickLink.objects.filter(is_active=True).order_by(
                    "display_order"
                ),
                to_attr="active_quick_links",
            ),
            Prefetch(
                "footer_services",
                queryset=FooterService.objects.filter(is_active=True).order_by(
                    "display_order"
                ),
                to_attr="active_footer_services",
            ),
            Prefetch(
                "footer_contacts",
                queryset=FooterContact.objects.filter(is_active=True).order_by(
                    "display_order"
                ),
                to_attr="active_footer_contacts",
            ),
            Prefetch(
                "social_links",
                queryset=FooterSocialLink.objects.filter(is_active=True).order_by(
                    "display_order"
                ),
                to_attr="active_social_links",
            ),
        )
        .first()
    )

    context = {
        "navbar": navbar,
        "navigation_items": navigation_items,
        "hero_slides": hero_slides,
        "about_section": about_section,
        "service_section": service_section,
        "why_choose_us": why_choose_us,
        "how_it_works": how_it_works,
        "testimonials": testimonials,
        "book_today": book_today,
        "footer": footer,
    }

    return render(request, "index.html", context)
